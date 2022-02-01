import pandas as pd
from sklearn.linear_model import ElasticNet
from read_config import read_config_file
import argparse
from evaluate import calc_metrics
import mlflow
from urllib.parse import urlparse

def train(config_path) -> None:
    """load the train & test files and train model"""

    config = read_config_file(config_path)
    train_path = config["data"]["processed"]["test"]
    test_path = config["data"]["processed"]["test"]
    random_state = config["data"]["processed"]["random_state"]

    label = config["data"]["processed"]["label"]
    alpha = config["models"]["ElasticNet"]["params"]["alpha"]
    l1_ratio = config["models"]["ElasticNet"]["params"]["l1_ratio"]

    train_data = pd.read_csv(train_path, sep=",", encoding="utf8")
    test_data = pd.read_csv(test_path, sep=",", encoding="utf8")

    train_X = train_data.drop(label, axis=1)
    test_X = test_data.drop(label, axis=1)
    train_y = train_data[label]
    test_y = test_data[label]

    #====MLFLOW====#
    mlflow_config = config["mlflow"]
    remote_server_uri = mlflow_config["remote_server_uri"]
    mlflow.set_tracking_uri(remote_server_uri)
    mlflow.set_experiment(mlflow_config["experiment_name"])

    with mlflow.start_run(run_name=mlflow_config["run_name"]) as mlflow_run:
        model = ElasticNet(alpha=alpha, l1_ratio=l1_ratio,
                        random_state=random_state)
        model.fit(train_X, train_y)

        y_hat = model.predict(test_X)

        # calc metrics 
        (rmse, mae, r2) = calc_metrics(y=test_y, y_hat=y_hat)

        mlflow.log_param("alpha", alpha)
        mlflow.log_param("l1_ratio", l1_ratio)
        mlflow.log_metric("rmse", rmse)
        mlflow.log_metric("mae", mae)
        mlflow.log_metric("r2", r2)

        tracking_url_type_store = urlparse(mlflow.get_artifact_uri()).scheme

        if tracking_url_type_store != "file": # if its not a file, store model to a db
            mlflow.sklearn.log_model( # we have a sklearn model
                model,
                "model", 
                registered_model_name=mlflow_config["registered_model_name"]
                ) 
        else:
            mlflow.sklearn.load_model(model, "model")


if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config_file", default="config.yaml")
    parsed_args = args.parse_args()
    train(parsed_args.config_file)
