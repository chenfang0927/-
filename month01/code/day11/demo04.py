"""
    继承数据

        class 儿子(爸爸):
            def __init__(self, 爸爸构造函数参数,儿子构造函数参数):
                super().__init__(爸爸构造函数参数)
                self.数据 = 儿子构造函数参数
    练习：exercise04
"""


class Person:
    def __init__(self, name="", age=0):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name="", age=0, score=0):
        # 通过super()调用父类实例成员
        super().__init__(name, age)
        self.score = score


# 1. 子类没有构造函数,可以直接使用父类的
# s01 = Student()

# 2. 子类有构造函数,会覆盖父类构造函数(好像他不存在)
#    所以子类必须通过super()调用父类构造函数
s01 = Student("小明", 24, 100)
print(s01.name)
print(s01.age)
print(s01.score)
