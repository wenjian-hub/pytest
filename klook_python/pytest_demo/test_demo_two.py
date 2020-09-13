import pytest
import allure
import random

@allure.feature("hotel pytest 分享")
class TestDemoTwo:
    """
    :params 参数化
    :skip
    :skipif
    :xfail
    :xdist
    :flaky
    """
    @allure.story("pytest 参数化")
    @allure.title("两位数相加")
    @pytest.mark.parametrize("a, b, sum", [(1, 2, 3), (4, 5, 9)])
    def test_params(self, a, b, sum):
        assert a + b == sum


    @pytest.mark.parametrize("a", [1, 2, 3, 4])
    @pytest.mark.parametrize("b", [4, 5, 6])
    @pytest.mark.parametrize("c", [4, 10])
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title("三位数相加：{c}+{b}+{a}")
    def test_add(self, b, a, c):
        sum = a + b + c
        print(sum)
        allure.attach("{}+{}+{}={}".format(c, b, a, sum), "计算结果", allure.attachment_type.TEXT)

    @pytest.mark.skip(reason="错误参数")
    @pytest.mark.parametrize("a, b", [("1", "2")])
    def test_skip(self, a, b):
        sum = a + b

    a = 100
    @pytest.mark.skipif(a > 10, reason="条件不满足")
    def test_skipif(self):
        sum = 10 + 10


    @pytest.mark.xfail(a > 1, reason="异常数据")
    @pytest.mark.parametrize("a, b", [(12, 13)])
    def test_xfail(self, a, b):
        sum = a + b

   
    @pytest.mark.flaky(reruns=5, reruns_delay=3)
     def test_flaky(self):
         number = random.randint(1, 5)
         print(number)
         assert number == 4
