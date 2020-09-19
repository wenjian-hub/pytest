import pytest


def is_Numbe(number):
    if isinstance(number, int) or isinstance(number, float):
        raise ValueError("输入类型错误")


@pytest.fixture(scope='function', autouse=True)
def setup():
    print("\n[开始计算]")
    yield
    print('\n[计算结束]')

