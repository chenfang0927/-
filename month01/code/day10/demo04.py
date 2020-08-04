"""
    封装行为

    需求：类的定义者保障数据的有效性
        年龄：  25 ～ 30
    练习：exercise04
"""

class Wife:
    def __init__(self, name="", age=0):
        self.name = name
        self.age = age  # 2

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):  # 3
        if 25 <= value <= 30:
            self.__age = value
        else:
            raise Exception("不行")



w01 = Wife("双儿", 25)  # 1
print(w01.name)
print(w01.age)  #
