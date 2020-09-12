from configparser import ConfigParser
from pathlib import Path
import yaml
from jsonpath import jsonpath


class conf_Data:
    conf_path = Path.cwd().parent / "conf/conf_data.ini"
    config = ConfigParser()
    config.read(conf_path)

    @classmethod
    def agent_host(cls, session, option):
        value = cls.config.get(session, option)
        return value


class conf_data_yaml:
    conf_path = Path.cwd().parent / "conf/conf_data.yaml"
    data = yaml.safe_load(open(conf_path, mode="r", encoding="utf-8"))

    @classmethod
    def agent_host(cls,  expr):
        value = jsonpath(cls.data, expr)[0]
        return value


