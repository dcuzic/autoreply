from pathlib import Path
import json

def get_config_path():
    return Path(__file__).resolve().parent / "config.json"

def read_config():
    config_path = get_config_path()
    with open(config_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data

data = read_config()
print(data)
from pathlib import Path
import json

def get_config_path():
    return Path(__file__).resolve().parent / "config.json"

def read_config():
    config_path = get_config_path()
    with open(config_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data

data = read_config()
print(data)
