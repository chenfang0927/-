"""

"""


def func01(p1, p2):
    # 修改局部变量
    p1 = 10
    # 2. 修改可变对象(向列表添加元素)
    p2.append(20)


# 1. 传入可变对象(列表、字典、集合)
a = 1
b = []
func01(a, b)
print(a)# 1
print(b)# [20]


def func02(p1):
    p1 = 10
    # 因为传入的是不可变对象
    # 所以p1 = 10 不会影响函数外部
    # 必须通过return返回结果
    return p1

a = 1
b = func02(a)
print(a) # 1
print(b)# 10