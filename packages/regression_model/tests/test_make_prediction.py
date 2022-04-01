import numpy as np
from random_forest_regressor.src.predict import predict
from random_forest_regressor import __version__ as _version


def test_make_predictions(sample_input_data):
    result = predict(sample_input_data)
    predictions = result.get("predictions")
    assert isinstance(predictions, list)
    assert isinstance(predictions[0], np.float64)

def test_correct_version_in_dict(sample_input_data):
    result = predict(sample_input_data)
    assert result.get("version") == _version  