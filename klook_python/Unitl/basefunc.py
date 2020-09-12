from jsonpath import jsonpath


def getSampleVal(obj, expr) -> str:
    value = jsonpath(obj, expr)
    return value[0]


def getMultVal(obj, expr) -> list:
    value = jsonpath(obj, expr)
    return value