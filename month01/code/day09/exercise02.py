# 练习：定义多个数值累乘的函数
def multiply(*args):
    sum = 1
    for number in args:
        sum *= number
    return sum


print(multiply())
print(multiply(12, 3, 342, 35, 6, 75, 8))
