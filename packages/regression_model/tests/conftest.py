from json import load
import pytest
from random_forest_regressor.src.data_manager import get_train_test_data
from random_forest_regressor.config.core import config

@pytest.fixture()
def sample_input_data():
    _, y = get_train_test_data()
    return y[config.model_config.features]