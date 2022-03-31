from random_forest_regressor.config import core

VERSION_PATH = core.ROOT / "VERSION"

with open(VERSION_PATH, "r") as version_file:
    __version__ = version_file.read().strip()