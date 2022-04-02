from pathlib import Path
from typing import Tuple

import joblib
import numpy as np
import pandas as pd
from sklearn.pipeline import Pipeline

from model import __version__ as _version
from model.config.core import ARTIFACTS_PATH, DATA_PATH, config


def _train_test_split(raw_data: pd.DataFrame) -> None:
    # train test split using pandas
    msk = np.random.rand(len(raw_data)) < config.model_config.test_size
    train_data = raw_data[~msk]
    test_data = raw_data[msk].drop("TARGET", axis=1)
    train_data.to_csv(
        Path(f"{DATA_PATH}/{config.app_config.train_data}"), index=False, sep=","
    )
    test_data.to_csv(
        Path(f"{DATA_PATH}/{config.app_config.test_data}"), index=False, sep=","
    )


def _load_and_transform_data() -> None:
    raw_data = pd.read_csv(Path(f"{DATA_PATH}/{config.app_config.raw_data}"))
    cols = raw_data.columns
    cols = [col.replace(" ", "_") for col in cols]
    raw_data.columns = cols
    _train_test_split(raw_data=raw_data)


def get_train_test_data() -> Tuple[pd.DataFrame, pd.DataFrame]:
    _load_and_transform_data()
    return (
        pd.read_csv(f"{DATA_PATH}/{config.app_config.train_data}"),
        pd.read_csv(f"{DATA_PATH}/{config.app_config.test_data}"),
    )


def _get_pipeline_save_file_path() -> str:
    pipeline_save_file = f"{config.app_config.pipeline_save_file}_{_version}.pkl"
    file_path = f"{ARTIFACTS_PATH}/{pipeline_save_file}"
    return file_path


def save_pipeline(pipeline: Pipeline) -> None:
    pipeline_save_file = _get_pipeline_save_file_path()
    joblib.dump(pipeline, pipeline_save_file)


def load_pipeline() -> Pipeline:
    pipeline_save_file = _get_pipeline_save_file_path()
    trained_model = joblib.load(filename=pipeline_save_file)
    return trained_model
