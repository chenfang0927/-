"""
    多继承
        继承不是代码的复用方式
"""

class A:
    def __init__(self,a):
        self.a = a

    def func01(self):
        print("A -- func01,实例变量:",self.a)


class B:
    def __init__(self,a):
        self.b = a

    def func02(self):
        print("B -- func01实例变量:",self.b)


# C 需要使用AB的函数
class C(A, B):
    def func03(self):
        super().func01()
        super().func02()
        print("C -- func01")

# 创建C对象,使用的而是A构造函数,没有执行B构造函数.
c = C("a")
c.func03() # 因为B对象没有执行构造函数,所以不能正常工作
