import typing as t
import pandas as pd
from random_forest_regressor import __version__ as _version
from random_forest_regressor.config.core import config
from random_forest_regressor.src.data_manager import load_pipeline

pipeline = load_pipeline()

def predict(input_data: t.Union[pd.DataFrame, dict]) -> dict:
    data = pd.DataFrame(input_data)
    prediction_list = list()
    predictions = pipeline.predict(X=data[config.model_config.features])

    for pred in predictions:
        prediction_list.append(pred)

    result = {
        "predictions": prediction_list,
        "version": _version
    }

    return result
