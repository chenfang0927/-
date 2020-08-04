"""
    函数 - 功能
        参数：调用函数  给 制作函数 传递的信息
    练习：exercise01,02
"""


# 做
def single_attack():
    print("摆拳")
    print("勾拳")
    print("侧踹")
    print("正蹬")
    print("直拳")
    print("发大招")


# 形式参数
def multiple_attacks(count):
    # count = 10
    for __ in range(count):
        print("摆拳")
        print("勾拳")
        print("侧踹")
        print("正蹬")
        print("直拳")
        print("发大招")


# 用
# 实际参数
multiple_attacks(10)
multiple_attacks(3)
