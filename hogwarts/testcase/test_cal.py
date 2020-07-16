import allure
from common.calculation import Calculator
from test_data.read_data import get_testParams


@allure.feature("加减乘除")
class TestCal:
    @allure.story("加法运算")
    @allure.title("多位数相加")
    def test_add(self):
       expec_value = get_testParams("$..add_sum")
       actual_value = Calculator.add_sum(get_testParams("$.add_func..test_param"))
       assert expec_value == actual_value, "{} != {}".format(expec_value, actual_value)

    @allure.story("减法运算")
    @allure.title("多位数相减")
    def test_sub(self):
        expec_value = get_testParams("$..sub_sum")
        actual_value = Calculator.sub_sum(get_testParams("$.sub_func..test_param"))
        assert expec_value == actual_value, "{} != {}".format(expec_value, actual_value)

    @allure.story("乘法运算")
    @allure.title("多位数相乘")
    def test_mult(self):
        expec_value = get_testParams("$..mul_sum")
        actual_value = Calculator.mul_sum(get_testParams("$.mul_func..test_param"))
        assert expec_value == actual_value, "{} != {}".format(expec_value, actual_value)

    @allure.story("除法运算")
    @allure.title("多位数相除")
    def test_div(self):
        expec_value = get_testParams("$..div_sum")
        actual_value = Calculator.div_sum(get_testParams("$.sub_func..test_param"))
        assert expec_value == actual_value, "{} != {}".format(expec_value, actual_value)
