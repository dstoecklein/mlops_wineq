import os

from model.config import core

with open(os.path.join(core.ROOT, "VERSION")) as version_file:
    __version__ = version_file.read().strip()
