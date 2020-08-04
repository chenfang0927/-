"""
    多态
        定义：父类的同一种动作或者行为，在不同的子类上有不同的实现。
        步骤：
            1. 调用父
            2. 子重写
            3. 创建子
        目的：
            彰显子类个性(不同/变化/具体)
            体现开闭原则(目标)
"""

class A:
    def func01(self):
        pass

class B(A):
    # 2. 子重写
    def func01(self):
        print("B -- func01")

class C(A):
    def func01(self):
        print("C -- func01")

def func02(a):
    # 1. 调用父
    a.func01()

b = B()
c = C()
# 3. 创建子
func02(c)
