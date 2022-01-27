import os
import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from read_config import read_config_file
import joblib
import json
from read_config import read_config_file


def save_metrics(config_path, y, y_hat) -> None:
    """evaluate & save the metrics of trained model"""

    config = read_config_file(config_path)

    params_file = config["reports"]["params"]
    metrics_file = config["reports"]["metrics"]

    alpha = config["models"]["ElasticNet"]["params"]["alpha"]
    l1_ratio = config["models"]["ElasticNet"]["params"]["l1_ratio"]

    rmse = np.sqrt(mean_squared_error(y, y_hat))
    mae = mean_absolute_error(y, y_hat)
    r2 = r2_score(y, y_hat)

    with open(metrics_file, "w") as f:
        metrics = {
            "rmse": rmse,
            "mae": mae,
            "r2": r2
        }
        json.dump(metrics, f, indent=4)

    with open(params_file, "w") as f:
        params = {
            "alpha": alpha,
            "l1_ratio": l1_ratio
        }
        json.dump(params, f, indent=4)


def save_model(config_path, model) -> None:
    """save model as joblibe"""
    config = read_config_file(config_path)
    model_dir = config["model_dir"]
    os.makedirs(model_dir, exist_ok=True)
    model_path = os.path.join(model_dir, "model.joblib")
    joblib.dump(model, model_path)
