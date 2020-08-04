"""
    (1). 创建父子类,添加实例变量
            创建父类:人(姓名,年龄)
            创建子类:学生(成绩)
    (2). 创建父子对象,直接打印.
            格式: 我是xx,今年xx.
                 我是xx,今年xx,成绩是xx.
    (3). 通过eval + __repr__拷贝对象,
         修改拷贝前对象的实例变量,
         打印拷贝后对象的实例变量.
"""


class Person:
    def __init__(self, name="", age=0):
        self.name = name
        self.age = age

    # 重写:彰显子类的个性
    def __str__(self):
        return f"我是{self.name},今年{self.age}."

    def __repr__(self):
        return f'Person("{self.name}",{self.age})'

class Student(Person):
    def __init__(self, name="", age=0, score=0):
        super().__init__(name, age)
        self.score = score

    def __str__(self):
        # return f"我是{self.name},今年{self.age}.成绩是{self.score}."
        return super().__str__() + f"成绩是{self.score}."

    def __repr__(self):
        return f'Student("{self.name}", {self.age}, {self.score})'

s01 = Student("小明", 22, 90)
print(s01)

s02 = eval(s01.__repr__())
s01.name = "明明"
print(s02.name)