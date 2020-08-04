"""
    lambda 表达式
        匿名函数:
            lambda 参数: 函数体

            def不能转换为lambda写法
                1. lambda表达式不能赋值
                2. lambda 函数体只能有一条语句

            应用:作为实参
"""

# 写法1:有参数,有返回值
# def func01(p1, p2):
#     return p1 > p2
#
# print(func01(10, 5))

func01 = lambda p1, p2: p1 > p2
print(func01(10, 5))

# 写法2:有参数,无返回值
# def func02(p1):
#     print("参数是:",p1)
#
# func02(10)

func02 = lambda p1: print("参数是:", p1)
func02(10)

# 写法3:无参数,有返回值
# def func03():
#     return "结果"
#
# result = func03()
# print(result)

func03 = lambda: "结果"
result = func03()
print(result)

# 写法4:无参数,无返回值
# def func04():
#     print("func04执行喽")
#
# func04()

func04 = lambda: print("func04执行喽")
func04()

# def不能转换为lambda写法
def func05(p1):
    p1[0] = 100

list01 = [10]
func05(list01)
print(list01[0]) # 100

# 1. lambda表达式不能赋值
# func05 = lambda p1:p1[0] = 100


def func06():
    for i in range(5):
        print(i)

func06()

# 2. lambda 函数体只能有一条语句
# func06 = lambda :for i in range(5):
#                     print(i)


