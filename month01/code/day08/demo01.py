"""
    函数 - 功能
        价值1：减少代码的重复
        制作
            def 函数名称():
                函数体

        使用
            函数名称()
"""
# 重复的代码就是万恶之源

# 做 + 用
# print("摆拳")
# print("勾拳")
# print("侧踹")
# print("正蹬")
# print("直拳")
# # ........
# 做 + 用
# print("摆拳")
# print("勾拳")
# print("侧踹")
# print("正蹬")
# print("直拳")

# 做
def attack():
    print("摆拳")
    print("勾拳")
    print("侧踹")
    print("正蹬")
    print("直拳")
    print("发大招")

# 用
attack()
attack()