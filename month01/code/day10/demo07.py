"""
    属性各种写法
"""
"""
# 写法1：读写(能够对外提供读取和设置功能)
# 快捷键：props + 回车
class Wife:
    def __init__(self, age=0):
        self.age = age# 执行设置函数

    @property
    def age(self):  # 读取函数
        return self.__age

    @age.setter
    def age(self, value):  # 设置函数
        self.__age = value


w01 = Wife(25)
print(w01.age)# 执行读取函数
"""

"""
# 写法2：只读(只对外提供读取功能,类外不能修改)
# 快捷键：prop + 回车
class Wife:
    def __init__(self, age=0):
        self.__age = age# 为私有变量赋值

    @property
    def age(self):
        return self.__age

w01 = Wife(25)
print(w01.age)# 执行读取函数
# w01.age  = 10
"""


# 写法3：只写(只能够对外提供设置功能)
# 快捷键： 无
class Wife:
    def __init__(self, age=0):
        self.age = age  # 执行设置函数

    age = property()
    @age.setter
    def age(self, value):  # 设置函数
        self.__age = value


w01 = Wife(25)
# print(w01.age)  # 执行读取函数
print(w01.__dict__)
