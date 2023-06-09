import yaml
import json


def write_yaml():

    with open('custom.json') as json_file:
        dict_file = json.load(json_file)

    with open(r'example.yaml', 'w') as file:
        yaml.dump(dict_file, file)
