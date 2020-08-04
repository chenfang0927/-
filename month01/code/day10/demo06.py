"""
    property 属性
        价值：保护实例变量
            1. 属性名与实例变量名称相同（拦截）
            2. 属性中操作私有变量（需要被保护）
        核心：拦截
"""

class Wife:
    def __init__(self, name="", age=0):
        self.name = name
        # 属性
        self.age = age

    #  age = property(读取函数)
    #  (1) 创建属性对象property()
    #  (2) 将下面的函数作为参数property(读取函数)
    #  (3) 将属性对象交给变量名关联age
    @property
    def age(self):# 读取函数
        return self.__age

    # age.setter(设置函数)
    # (1) 调用属性的setter函数
    # (2) 将下面的函数作为参数setter(设置函数)
    @age.setter
    def age(self, value): # 设置函数
        if 25 <= value <= 30:
            self.__age = value
        else:
            raise Exception("不行")

w01 = Wife("双儿", 25)  # 1
print(w01.name)
print(w01.age)  #
