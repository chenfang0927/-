"""
    装饰器 - 细节语法
        1. 内部函数返回值是旧功能返回值
"""


def print_func_name(func):
    # *合:将多个位置实参合并为一个元组
    # **合:将多个关键字实参合并为一个字典
    def wrapper(*args, **kwargs):  # 2
        print("-----", func.__name__, "-----")
        # 调用的是func01
        # *拆：将一个序列拆分为多个元素
        # **拆：将一个字典拆分为多个键值对
        return func(*args, **kwargs)  # 3 5

    return wrapper


@print_func_name
def func01(p1, p2):  # 4
    print("func01执行,参数是:", p1, p2)
    return 100


# 调用内部函数wrapper
re = func01(1, p2 = 2)  # 1 6
print(re)  # 100
