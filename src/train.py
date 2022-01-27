import pandas as pd
from sklearn.linear_model import ElasticNet
from read_config import read_config_file
import argparse
from evaluate import save_metrics, save_model

def train(config_path) -> None:
    """load the train & test files and train model"""

    config = read_config_file(config_path)
    train_path = config["data"]["processed"]["test"]
    test_path = config["data"]["processed"]["test"]
    random_state = config["data"]["processed"]["random_state"]
    model_dir = config["model_dir"]
    label = config["data"]["processed"]["label"]
    alpha = config["models"]["ElasticNet"]["params"]["alpha"]
    l1_ratio = config["models"]["ElasticNet"]["params"]["l1_ratio"]

    train_data = pd.read_csv(train_path, sep=",", encoding="utf8")
    test_data = pd.read_csv(test_path, sep=",", encoding="utf8")

    train_X = train_data.drop(label, axis=1)
    test_X = test_data.drop(label, axis=1)
    train_y = train_data[label]
    test_y = test_data[label]

    model = ElasticNet(alpha=alpha, l1_ratio=l1_ratio, random_state=random_state)
    model.fit(train_X, train_y)

    predictions = model.predict(test_X)

    # metrics & model save
    save_metrics(config_path, test_y, predictions)
    save_model(config_path, model)

if __name__=="__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config_file", default="config.yaml")
    parsed_args = args.parse_args()
    train(parsed_args.config_file)