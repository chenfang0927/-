"""
    函数 - 功能
        程序自生而下运行
        创建函数的代码要先加载到内存中
        再去调用函数
"""
# --------------创建(定义)函数-------------------

def single_attack():
    print("摆拳")# 3
    print("勾拳")
    print("侧踹")
    print("正蹬")
    print("直拳")
    print("发大招")

def multiple_attacks(count):
    # count = 10
    for __ in range(count):# 2
       single_attack()

# --------------调用(使用)函数-------------------
multiple_attacks(2) # 1
multiple_attacks(5) # 1