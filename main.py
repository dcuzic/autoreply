import datetime
from pathlib import Path
import json

# БЛОК А 

# reading config.json
def get_config_path():
    return Path(__file__).resolve().parent / "config.json"

def read_config():
    config_path = get_config_path()
    with open(config_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data

data = read_config()

busy_from = data[]

# print(data)

# add a request for the user (do they want to change the intervals?)



def change_intervals():


# busy intervals

busy_from = data(read_config['from'])
busy_to = data["to"]

def is_busy(data):
    for interval in data["busy_intervals"]:
        busy_from = interval["from"]
        busy_to = interval["to"]
    return busy_from, busy_to

print(is_busy(busy_from, busy_to))

