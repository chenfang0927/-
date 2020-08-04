"""
    中心思想：
        类：有行为需要承担
        对象：表达数据不同
        类与类行为不同,对象与对象数据不同.

    小明使用手机打电话
    1. 识别对象
        小明    手机
    2. 分配职责
        打电话  通话
    3. 建立交互
        人 调用 手机
            (1)直接创建对象调用
            (2)在构造函数中创建对象
            (3)通过参数传递对象
"""

class Person:
    def __init__(self, name=""):
        self.name = name

    def call(self, communication):
        print(self.name, "打电话")
        communication.dialing()


class MobilePhone:
    def dialing(self):
        print("呼叫")


xm = Person("小明")
xm.call(MobilePhone())
