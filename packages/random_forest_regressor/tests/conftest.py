import pytest

from model.config.core import config
from model.src.data_manager import get_train_test_data


@pytest.fixture()
def sample_input_data():
    _, y = get_train_test_data()
    return y[config.model_config.features]
