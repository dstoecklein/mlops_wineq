from get_remote_data import from_gdrive
from read_config import read_config_file
import argparse


def save_csv(config_path) -> None:
    """Loads the file from data_remote and saves it as .csv in data/raw"""
    config = read_config_file(config_path)
    df = from_gdrive(config_path)
    new_cols = [col.replace(" ", "_") for col in df.columns]
    raw_path = config["data"]["raw"]
    df.to_csv(raw_path, sep=",", encoding="utf8", index=False, header=new_cols)


if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config_file", default="config.yaml")
    parsed_args = args.parse_args()
    save_csv(parsed_args.config_file)
