"""
    面向对象设计思想
    需求：老张开车去东北
    变化：增加飞机、自行车....
    封装：划分类   人类     车类
    以下代码缺点：违反开闭原则
        增加飞机,还要修改人的代码
"""

class Person:
    def __init__(self, name=""):
        self.name = name

    def go_to(self,position,vehicle):
        print(self.name,"去",position)
        if type(vehicle) == Car:
            vehicle.run()
        elif type(vehicle) == Airplane:
            vehicle.fly()

class Car:
    def run(self):
        print("汽车在行驶")

class Airplane:
    def fly(self):
        print("飞机在飞行")

# 测试.....
lw = Person("老王")
c01 = Car()
a01 = Airplane()
lw.go_to("东北",a01)