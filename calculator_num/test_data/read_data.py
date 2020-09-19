import yaml
from pathlib import Path
import jsonpath


def get_value(obj, expr):
    data = jsonpath.jsonpath(obj, expr)
    return data


data_path = Path.cwd().parent / 'test_data' / 'data.yaml'
yaml_data_path = Path.cwd().parent / 'test_data' / 'yaml_data.yaml'


def get_testParams(expr):
    data_all = yaml.safe_load(open(data_path, "r", encoding='utf-8'))
    data = get_value(data_all, expr)[0]
    return data


print(get_testParams("$.."))
