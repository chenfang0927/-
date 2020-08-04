"""
    装饰器 - 应用
"""
# 需求：不改变func01调用,以及内部的情况下
#      为其增加新功能(打印函数名称)

def print_func_name(func):  # 得到旧功能
    def wrapper(*args, **kwargs):  # 新功能 + 旧功能
        # 新功能：打印传入的函数名称
        print("-----", func.__name__, "-----")
        # 旧功能：执行传入的函数
        return func(*args, **kwargs)

    return wrapper


# @print_func_name # 调用外部函数  绑定下面函数
def func01():
    print("func01执行了")


# 调用外部函数(得到了1000元)
func01 = print_func_name(func01)

# 调用内部函数(花钱)
func01()
func01()
