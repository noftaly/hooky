import os
import sys
import pathlib

def get_asset(name):
    base_path = pathlib.Path(__file__).parent.absolute()
    # If running PyInstaller
    if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
        return os.path.join(base_path, "Assets", name)
    return os.path.join(base_path, "..", "Assets", name)
