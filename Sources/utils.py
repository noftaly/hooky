import os
import pathlib

def get_asset(name):
    base_path = pathlib.Path(__file__).parent.absolute()
    return os.path.join(base_path, "Assets", name)
