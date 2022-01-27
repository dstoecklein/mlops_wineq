import pandas as pd
import argparse
from read_config import read_config_file

def from_gdrive(config_path) -> pd.DataFrame:
    """loads dvc tracked data from remote gdrive"""
    config_file = read_config_file(config_path)
    data_path = config_file["data_remote"]["gdrive"]
    df = pd.read_csv(data_path, sep=",", encoding="utf8")
    return df

if __name__=="__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config_file", default="config.yaml")
    parsed_args = args.parse_args()
    from_gdrive(parsed_args.config_file)