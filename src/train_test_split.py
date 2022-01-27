import argparse
import pandas as pd
from sklearn.model_selection import train_test_split
from read_config import read_config_file

def split_and_save(config_path) -> None:
    """split the raw data and save it in data/processed"""
    config = read_config_file(config_path)
    raw_path = config["data"]["raw"]
    train_path = config["data"]["processed"]["train"]
    test_path = config["data"]["processed"]["test"]
    split_ratio = config["data"]["processed"]["split_ratio"]
    random_state = config["data"]["processed"]["random_state"]

    # read raw data
    df = pd.read_csv(raw_path, sep=",", encoding="utf8")

    # train test split
    train_data, test_data = train_test_split(df, test_size=split_ratio, random_state=random_state)

    # save train, test data
    train_data.to_csv(train_path, sep=",", encoding="utf8", index=False)
    test_data.to_csv(test_path, sep=",", encoding="utf8", index=False)

if __name__=="__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config_file", default="config.yaml")
    parsed_args = args.parse_args()
    split_and_save(parsed_args.config_file)