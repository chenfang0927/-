"""
    类成员
        类变量
            创建：在类中
            使用：用类名   类名.类变量
        类方法
    练习:exercise02
"""


class ICBC:
    # 类变量：总行的钱
    total_money = 1000000

    @classmethod
    def print_total_money(cls):
        # print("总行的钱是", ICBC.total_money)
        print("总行的钱是", cls.total_money)

    def __init__(self, name="", money=0):
        self.name = name
        # 实例变量：支行的钱
        self.money = money
        # 总行的钱减少
        ICBC.total_money -= money


tt = ICBC("天坛支行", 100000)
trt = ICBC("陶然亭支行", 200000)
# print("总行的钱：", ICBC.total_money)
ICBC.print_total_money()# print_total_money(ICBC)