"""
    内置可重写函数
"""

# 任何一个类,都直接或间接继承自object类(万类之祖).
# class Dog(object):
class Dog:
    # 时机：创建对象时
    def __init__(self, variety, name, age, weight=0.0):
        self.variety = variety
        self.name = name
        self.age = age
        self.weight = weight

    # 时机：打印对象时
    def __str__(self):# 没有语法限制
        return f"我是{self.name},品种{self.variety},今年{self.age}岁了,体重{self.weight}斤"

    # 时机：拷贝对象时
    def __repr__(self): # Python语法格式
        return f'Dog("{self.variety}", "{self.name}", {self.age}, {self.weight})'

d01 = Dog("拉布拉多", "米咻", 5, 70)
#　我是米咻,品种拉布拉多,今年5岁了,体重70斤
print(d01)
# message = d01.__str__()
# print(message)

# 将字符串作为代码执行
# eval(字符串)  --> eval(input()) 将"无所不能"
d02 = eval(d01.__repr__())
d01.name = "咻咻"

print(d02)



