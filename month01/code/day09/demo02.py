"""
    函数参数
        形式参数
            默认形参：实参可选
    练习:exercise01
"""

# 注意：必须从右到左依次存在
def func01(p1= "", p2 = 0, p3 = 1):
    print(p1)
    print(p2)
    print(p3)

# 全部传递
func01(1, 2)
# 指定某一个形参
func01(p2=2)
func01(1, p3=3)
