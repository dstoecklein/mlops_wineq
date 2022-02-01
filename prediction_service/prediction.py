import os
import joblib
import numpy as np
from src.read_config import read_config_file, read_schema_file

config_file = "config.yaml"
schema_file = os.path.join("prediction_service", "schema_input.json")

class OutOfRange(Exception):
    def __init__(self, msg="Input value out of range") -> None:
        self.msg = msg
        super().__init__(self.msg)

class NotInColumn(Exception):
    def __init__(self, msg="Input value not in features") -> None:
        self.msg = msg
        super().__init__(self.msg)

def predict(data):
    config = read_config_file(config_file)
    webapp_model_dir = config["webapp_model_dir"]
    model = joblib.load(webapp_model_dir)
    prediction = model.predict(data).tolist()[0]

    try:
        if 3 <= prediction <= 8:
            return prediction
        else:
            raise OutOfRange
    except OutOfRange:
        return "Unexpected result"

def validate_input(request) -> bool:
    def _validate_cols(col):
        schema = read_schema_file(schema_file)
        true_cols = schema.keys()
        if col not in true_cols:
            raise NotInColumn

    def _validate_vals(col, val):
        schema = read_schema_file(schema_file)
        if not (schema[col]["min"] <= float(request[col]) <= schema[col]["max"]):
            raise OutOfRange

    for col, val in request.items():
        _validate_cols(col)
        _validate_vals(col, val)

    return True
    
def form_response(request):
    if validate_input(request):
        data = request.values()
        data = [list(map(float, data))]
        response = predict(data)
        return response

def api_response(request) -> dict:
    try:
        if validate_input(request):
            data = np.array([list(request.values())])
            response = predict(data)
            response = {"response": response} # convert it as dict
            return response
    except Exception as e:
        response = {"the_expected_rage": read_schema_file(schema_file), "response": str(e)}
        return response