import os
import script
import yaml

from dagster import DependencyDefinition, GraphDefinition, NodeInvocation, op


@op
def add_one(num: int) -> int:
    return num + 1


@op
def add_two(num: int) -> int:
    return num + 2


@op
def add(left: int, right: int) -> int:
    return left + right


def construct_graph_with_yaml(yaml_file, op_defs) -> GraphDefinition:
    stream = open(yaml_file, "r")
    yaml_data = yaml.load_all(stream, Loader=yaml.FullLoader)
    yaml_dict = list(yaml_data).pop().pop()
    assert isinstance(yaml_dict, dict)

    deps = {}

    for op_yaml_data in yaml_dict["ops"]:
        def_name = op_yaml_data["def"]
        alias = op_yaml_data.get("alias", def_name)
        op_deps_entry = {}
        for input_name, input_data in op_yaml_data.get("deps", {}).items():
            op_deps_entry[input_name] = DependencyDefinition(
                node=input_data["op"], output=input_data.get(
                    "output", "result")
            )
        deps[NodeInvocation(name=def_name, alias=alias)] = op_deps_entry

    return GraphDefinition(
        name=yaml_dict["name"],
        description=yaml_dict.get("description"),
        node_defs=op_defs,
        dependencies=deps,
    )


def define_dep_dsl_graph() -> GraphDefinition:
    script.write_yaml()
    path = os.path.join(os.path.dirname(__file__), "example.yaml")
    return construct_graph_with_yaml(path, [add_one, add_two, add])


local_job = define_dep_dsl_graph().to_job()

# execute job with an initial input of [num] as 0
if __name__ == "__main__":
    job_result = local_job.execute_in_process(
        {'ops': {'A': {'inputs': {'num': 0}}}})
