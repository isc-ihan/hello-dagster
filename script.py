import yaml
import json


def write_yaml() -> None:

    with open('custom.json') as json_file:
        dict_file = json.load(json_file)["graph"]

    with open(r'example.yaml', 'w') as file:
        yaml.dump(dict_file, file)


def get_config() -> dict:
    with open('custom.json') as json_file:
        return json.load(json_file)["run_config"]
