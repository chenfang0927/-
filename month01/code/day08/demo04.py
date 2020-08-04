"""
    函数 -- 返回值 语法
        制作函数 给 使用函数 传递的信息

    def 函数名():
        函数体
        return 数据 # 返回 结果

    变量名 = 函数名()
"""


# 做
def func01():
    print("func01执行喽")
    return 10  # return 数据   返回 结果


# 用
result = func01()
print("函数的返回值是:%d" % result)


# 如果函数没有return,相当于return None
# 如果函数return后面没有数据,也相当于return None
def func02():
    print("func01执行喽")
    # return None
    return


result = func02()
print(result)
