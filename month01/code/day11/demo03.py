"""
    继承
        财产：钱不用儿子挣，但是儿子能花
        皇位：江山不用太子打，但是太子能登基
        编程：代码不用子类写，但是子类能使用
    练习：exercise03
"""


# 从思想讲：先有子再有父
# 从编码讲：先有父再有子

# 多个类有代码的共性，且属于共同一个概念。
class Person:
    def say(self):
        print("说话")

class Student(Person):
    def study(self):
        self.say()
        print("学习")

class Teacher(Person):
    def teach(self):
        print("教学")

# 创建子类对象,可以调用父类方法和子类方法
s01 = Student()
s01.say()
s01.study()

# 创建父类对象,只能调用父类方法
p01 = Person()
p01.say()

# isinstance(对象,类型)  判断关系
# 学生对象  是一种  学生类型
print(isinstance(s01, Student)) # True
# 学生对象  是一种  人类型
print(isinstance(s01, Person)) # True
# 学生对象  是一种  老师类型
print(isinstance(s01, Teacher)) # False
# 人对象  是一种 学生类型
print(isinstance(p01, Student)) # False

# issubclass(类型,类型)  判断关系
# 学生类型  是一种  学生类型
print(issubclass(Student, Student)) # True
# 学生类型  是一种  人类型
print(issubclass(Student, Person)) # True
# 学生类型  是一种  老师类型
print(issubclass(Student, Teacher)) # False
# 人类型  是一种 学生类型
print(issubclass(Person, Student)) # False

# Type
# type(对象) == 类型  相等/相同/一模一样
# 学生对象的类型  是  学生类型
print(type(s01) == Student) # True
# 学生对象的类型  是  人类型
print(type(s01) == Person) # False
# 学生对象的类型  是  老师类型
print(type(s01) == Teacher) # False
# 人对象的类型    是  学生类型
print(type(p01) ==  Student) # False
