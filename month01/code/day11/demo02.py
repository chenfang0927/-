"""
    总结
        类与类调用语法
"""


# 函数互相调用：通过函数名直接调用
# def func01():
#     func02()
#
# def func02():
#     print("func02")
#
# func01()

# 写法1：直接创建对象调
# class A:
#     def func01(self):
#         b = B()
#         b.func02()
#
# class B:
#     def func02(self):
#         print("func02")
#
# g01 = A()
# g01.func01()


# 写法2：构造函数创建对象调
# class A:
#     def __init__(self):
#         self.b = B()
#
#     def func01(self):
#         self.b.func02()
#
# class B:
#     def func02(self):
#         print("func02")
#
# g01 = A()
# g01.func01()

# 写法3：构造函数创建对象调
class A:
    def func01(self, c):
        c.func02()


class B:
    def func02(self):
        print("func02")


g01 = A()
g02 = B()
g01.func01(g02)
