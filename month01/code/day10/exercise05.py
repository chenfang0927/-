"""
    创建鼠标类
    创建实例变量并保证数据在有效范围内
        品牌、      单价、   重量、    颜色
        字符小于6  0-10000、100-1000
"""


class Mouse:
    def __init__(self, brand, unit_price, weight, colour):
        self.brand = brand
        self.unit_price = unit_price
        self.weight = weight
        self.colour = colour

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, value):
        if len(value) <= 6:
            self.__brand = value
        else:
            raise Exception("不行")

    @property
    def unit_price(self):
        return self.__unit_price

    @unit_price.setter
    def unit_price(self, value):
        if 0 <= value <= 10000:
            self.__unit_price = value
        else:
            raise Exception("不行")

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, value):
        if value < 100:
            value = 100
        elif value > 1000:
            value = 1000
        self.__weight = value


m01 = Mouse("双飞燕", 100, 150, "白色")
print(m01.brand)
print(m01.unit_price)
print(m01.weight)
print(m01.colour)
