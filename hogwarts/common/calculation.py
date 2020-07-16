import decimal
decimal.getcontext().prec = 3


def is_Numbe(number):
    if not isinstance(number, int) or isinstance(number, float):
        raise ValueError("输入类型错误")


class Calculator:
    @classmethod
    def add_sum(cls, number):
        sum = 0
        for i in range(len(number)):
            sum = number[i] + sum
        print("{}相加结果: {}".format(number, sum))
        return sum

    @classmethod
    def sub_sum(cls, number):
        sum = 0
        sum = number[0] - sum
        for i in range(1, len(number)):
            sum = sum - number[i]
        print("{}相减结果: {}".format(number, sum))
        return sum

    @classmethod
    def mul_sum(cls, number):
        sum = 1
        for i in range(len(number)):
            sum = number[i] * sum
            print(number[i], end=" ")
        print("{}相乘结果: {}".format(number, sum))
        return sum

    @classmethod
    def div_sum(cls, number):
        sum = 1
        try:
            sum = decimal.Decimal(number[0]) / decimal.Decimal(sum)
            for i in range(1, len(number)):
                sum = decimal.Decimal(sum) / decimal.Decimal(number[i])
            print("{}相除结果: {}".format(number, sum))
            return float(sum)
        except Exception as error:
            print("计算error:{}, 请检查".format(error))


