import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score


def calc_metrics(y, y_hat) -> list:
    """evaluate the metrics of trained model"""
    rmse = np.sqrt(mean_squared_error(y, y_hat))
    mae = mean_absolute_error(y, y_hat)
    r2 = r2_score(y, y_hat)
    return rmse, mae, r2
