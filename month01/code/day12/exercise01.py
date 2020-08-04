"""
    1. 打印下列类的对象
        xx车的速度是xx
        编号xx的商品名称是xx,单价xx
        xx鼠标单价xx,宽xx,颜色xx
    2. 拷贝下列类的对象,
       修改拷贝前对象实例变量,
       打印拷贝后对象.
"""


class Car:
    def __init__(self, bread="", speed=0):
        self.bread = bread
        self.speed = speed

    # 适用性：呈现自定义对象
    def __str__(self):
        return f"{self.bread}车的速度是{self.speed}"

    # 适用性：拷贝自定义对象
    def __repr__(self):
        return 'Car("%s", %d)' % (self.bread, self.speed)


class Commodity:
    def __init__(self, cid, name, price):
        self.cid = cid
        self.name = name
        self.price = price

    def __str__(self):
        return "编号%d的商品名称是%s,单价%.2f" % (self.cid, self.name, self.price)


class Mouse:
    def __init__(self, brand, unit_price, weight, colour):
        self.brand = brand
        self.unit_price = unit_price
        self.weight = weight
        self.colour = colour

    def __str__(self) -> str:
        return f"{self.brand}鼠标单价{self.unit_price},宽{self.weight},颜色{self.colour}"


c01 = Car("奥迪", 200)
print(c01)

commodity = Commodity(1005, "口罩", 20)
print(commodity)

c02 = eval(c01.__repr__())
c01.bread = "奥拓"
print(c02)
