"""
    面向对象设计思想
    需求：老张开车去东北
    变化：增加飞机、自行车....
    封装：划分类   人类     车类
    继承：隔离     人类     具体交通工具
    重写：彰显子类个性   具体交通工具重写交通工具的方法

    情景：手雷爆炸，可能伤害敌人或者玩家的生命。
    变化：还可能伤害房子、树、鸭子....
    要求：增加新事物，不影响手雷.
    体会：开闭原则
    画出架构设计图

"""


class Person:
    def __init__(self, name=""):
        self.name = name

    def go_to(self, position, vehicle):
        print(self.name, "去", position)
        vehicle.transport()


class Vehicle:
    """
        交通工具虽然没有具体功能代码
        但是在隔离人与具体交通工具
    """

    def transport(self):
        pass


class Car(Vehicle):
    def transport(self):
        print("汽车在行驶")


class Airplane(Vehicle):
    # ctrl+o
    def transport(self):
        print("飞机在飞行")


# 测试.....
lw = Person("老王")
c01 = Car()
a01 = Airplane()
lw.go_to("东北", c01)
