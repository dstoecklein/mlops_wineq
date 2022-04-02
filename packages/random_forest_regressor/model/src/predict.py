import typing as t

import pandas as pd

from model import __version__ as _version
from model.config.core import config
from model.src.data_manager import load_pipeline

pipeline = load_pipeline()


def predict(input_data: t.Union[pd.DataFrame, dict]) -> dict:
    data = pd.DataFrame(input_data)
    prediction_list = list()
    predictions = pipeline.predict(X=data[config.model_config.features])

    for pred in predictions:
        prediction_list.append(pred)

    result = {"predictions": prediction_list, "version": _version}

    return result
