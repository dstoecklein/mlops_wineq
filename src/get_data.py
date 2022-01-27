import yaml
import pandas as pd
import argparse

# reads the config file (default=params.yaml) and returns dict
def read_config_file(config_path) -> dict:
    with open(config_path) as f:
        config_file = yaml.safe_load(f)
    return config_file

def get_data(config_path) -> pd.DataFrame:
    config_file = read_config_file(config_path)
    data_path = config_file["data_remote"]["gdrive"]
    df = pd.read_csv(data_path, sep=",", encoding="utf8")
    return df

if __name__=="__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config_file", default="config.yaml")
    parsed_args = args.parse_args()
    get_data(parsed_args.config_file)