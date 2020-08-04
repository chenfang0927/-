"""
    封装设计思想

        需求：老张开车去东北
            类：承担行为
            对象：承担数据
         1. 识别对象
            老张           车
         2. 分配职责
                去()         行驶()
         3. 建立交互
            老张调用车
    练习:exercise01
"""

# lz = Person("老张")
# ls = Person("老孙")

"""
# 写法1：直接创建对象
# 语义： 老张去东北用一辆新车
class Person:
    def __init__(self, name=""):
        self.name = name

    def go_to(self,position):
        print(self.name,"去",position)
        car = Car()
        car.run()

class Car:
    # 实例方法
    def run(self):
        print("汽车在行驶")

lw = Person("老王")


lw.go_to("东北")
lw.go_to("西北")
"""

"""
# 写法2：在构造函数中创建对象
# 语义： 老张开车自己的车去东北
class Person:
    def __init__(self, name=""):
        self.name = name
        self.car = Car()

    def go_to(self,position):
        print(self.name,"去",position)
        # 第一次.: 从栈帧到人对象
        # 第二次.: 从人到车对象
        self.car.run()

class Car:
    # 实例方法
    def run(self):
        print("汽车在行驶")

lw = Person("老王")
lw.go_to("东北")
lw.go_to("西北")
"""

# 写法3：通过参数传递对象
# 语义：人通过交通工具(参数传递而来)去东北
class Person:
    def __init__(self, name=""):
        self.name = name

    def go_to(self,position,vehicle):
        print(self.name,"去",position)
        vehicle.run()

class Car:
    # 实例方法
    def run(self):
        print("汽车在行驶")

lw = Person("老王")
c01 = Car()
lw.go_to("东北",c01)