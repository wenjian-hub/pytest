import pytest
order = [
      {
          "addr": "黄金书",
          "city": "shenzhen"
      },
      {
          "addr": "福田",
          "city": "深圳"
      }
  ]
@pytest.fixture(params=order)
def func4(request):
    infor = request.param
    addr = infor["addr"]
    city = infor
