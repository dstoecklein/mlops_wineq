import yaml

def read_config_file(config_path) -> dict:
    """reads the config file and returns it as dict"""
    with open(config_path) as f:
        config_file = yaml.safe_load(f)
    return config_file
