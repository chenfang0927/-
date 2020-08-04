"""
    raise
"""


class Wife:
    def __init__(self, age=0):
        self.age = age  # 2

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):  # 3
        if 22 <= value <= 30:
            self.__age = value
        else:
            # 主动抛出异常(快速传递错误消息)
            raise Exception("年龄超过范围",1,2,3)

try:
    w01 = Wife(300)  # 1
    print(w01.age)
except Exception as e: # 通过e变量操作抛出的异常对象
    print(e.args)
    print("出错啦")
