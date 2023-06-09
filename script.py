import yaml


def write_yaml():

    dict_file = [{'name': 'some_example', 'description': 'example yaml from dagster docs', 'ops':  # noqa: E501
              [{'def': 'add_one', 'alias': 'A'}, {'def': 'add_one', 'alias': 'B', 'deps':  # noqa: E501
                                                  {'num': {'op': 'A'}}}, {'def': 'add_two', 'alias': 'C', 'deps': {'num': {'op': 'A'}}},  # noqa: E501
                  {'def': 'add', 'deps': {'left': {'op': 'B'}, 'right': {'op': 'C'}}}]}]  # noqa: E501

    with open(r'example.yaml', 'w') as file:
        yaml.dump(dict_file, file)
