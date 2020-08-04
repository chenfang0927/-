"""
    总结Python所有变量
"""
# 全局变量:存储文件中
a = 10

def func01():
    # 局部变量:存储栈帧中
    b = 20

class MyClass:
    # 类变量:存储类中    【大家：饮水机】
    d = 40
    def __init__(self):
        # 实例变量:存储对象中
        self.c = 30 # 【自己：杯子】

