"""
    多继承
         同名方法解析顺序
            类.mro()
"""


class A:
    def func01(self):
        print("A -- func01")


class B(A):
    def func01(self):
        print("B -- func01")


class C(A):
    def func01(self):
        print("C -- func01")


class D(B, C):
    def func01(self):
        super().func01()  # 继承列表第一个父类
        print("D -- func01")


d = D()
d.func01()
# 解析顺序：类.mro()
# [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
print(D.mro())
