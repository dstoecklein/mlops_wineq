import pytest
import yaml
import os
import json

@pytest.fixture
def read_config_file(config_path="config.yaml") -> dict:
    """reads the config file and returns it as dict"""
    with open(config_path) as f:
        config_file = yaml.safe_load(f)
    return config_file

@pytest.fixture
def read_schema_file(schema_path="schema_input.json") -> dict:
    """reads the schema file and returns it as dict"""
    with open(schema_path) as f:
        schema_file = json.load(f)
    return schema_file
