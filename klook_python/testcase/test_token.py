from comm.Base import BaseApi
from conf.read_conf import conf_Data, conf_data_yaml
import yaml
from Unitl.basefunc import getSampleVal
import allure

host = conf_Data.agent_host("host", "agent_host")
print(host)


@allure.severity(allure.severity_level.BLOCKER)
class TestToken(BaseApi):
    def test_get_token(self):
        self.params["host"] = conf_Data.agent_host("host", "agent_host")
        data = yaml.safe_load(open("token.yaml", mode="r", encoding="utf-8"))
        res = self.send(data["token"])
        assert getSampleVal(res, "$..success") == True




