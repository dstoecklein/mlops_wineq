from src.read_config import read_config_file
import argparse
import mlflow
from mlflow.tracking import MlflowClient
from pprint import pprint
import joblib

def log_production_model(config_path):
    config = read_config_file(config_path)

    mlflow_config = config["mlflow"]

    model_name = mlflow_config["registered_model_name"]

    remote_server_uri = mlflow_config["remote_server_uri"]
    mlflow.set_tracking_uri(remote_server_uri)

    runs = mlflow.search_runs(experiment_ids=1) # dataframe. search for runs that we have done, experiment_ids -> look artifacts folder
    lowest_mae = runs["metrics.mae"].sort_values(ascending=True)[0]
    lowest_mae_run_id = runs[runs["metrics.mae"] == lowest_mae]["run_id"][0] # lowest run_id of lowest mae

    client = MlflowClient()

    for model_version in client.search_model_versions(f"name='{model_name}'"):
        model_version = dict(model_version) # convert to dict

        if model_version["run_id"] == lowest_mae_run_id:
            current_version = model_version["version"]
            logged_model = model_version["source"]
            pprint(model_version, indent=4)
            client.transition_model_version_stage( # function to change stage of a model
                name=model_name,
                version=current_version,
                stage="Production"
            )
        else: # put rest of the models to staging stage, otherwise we would have 2 production models -> error
            current_version = model_version["version"]
            client.transition_model_version_stage( # function to change stage of a model
                name=model_name,
                version=current_version,
                stage="Staging"
            )

    # put model in prediction service as joblib
    loaded_model = mlflow.pyfunc.load_model(logged_model)
    model_path = config["webapp_model_dir"]
    joblib.dump(loaded_model, model_path)

if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="config.yaml")
    parsed_args = args.parse_args()
    data = log_production_model(config_path=parsed_args.config)