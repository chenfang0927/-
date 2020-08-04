"""
    创建手机类
        数据：品牌、价格、颜色
        行为：通话
    实例化两个对象并调用其函数
    画出内存图
"""


class Phone:
    def __init__(self, brand, price, color):
        self.brand = brand
        self.price = price
        self.color = color

    def call(self):
        print(self.brand, "通话")

p01 = Phone("华为", 5000, "白色")
p01.call()

p02 = Phone("苹果", 8000, "黑色")
p02.call()
