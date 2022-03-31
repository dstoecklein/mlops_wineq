from typing import List
from pathlib import Path
from pydantic import BaseModel
from strictyaml import YAML, load
import random_forest_regressor

ROOT = Path(random_forest_regressor.__file__).resolve().parent
CONFIG_PATH = ROOT / "config"
DATA_PATH = ROOT / "data"
ARTIFACTS_PATH = ROOT / "artifacts"

# config files
CONFIG_FILE = CONFIG_PATH / "config.yml"

class AppConfig(BaseModel):
    package_name: str
    pipeline_name: str
    pipeline_save_file: str
    raw_data: str
    processed_data: str

class ModelConfig(BaseModel):
    target: str
    test_size: float
    seed: int
    n_estimators: int
    features: List[str]

class MasterConfig(BaseModel):
    app_config: AppConfig
    model_config: ModelConfig

def get_config_path() -> Path:
    if CONFIG_FILE.is_file():
        return CONFIG_FILE
    else:
        raise Exception(f"Invalid path or file {CONFIG_FILE}")

def read_config_file(config_path: Path = None) -> YAML:
    if not config_path:
        config_path = get_config_path()

    if config_path:
        with open(config_path, "r") as file:
            config_file = load(file.read())
            return config_file
    else:
        raise Exception(f"No config file found at {config_path}")

def create_and_validate_config(config_file: YAML = None) -> MasterConfig:
    if config_file is None:
        config_file = read_config_file()

    _config = MasterConfig(
        app_config=AppConfig(**config_file.data),
        model_config=ModelConfig(**config_file.data)
    )
    return _config

config = create_and_validate_config()