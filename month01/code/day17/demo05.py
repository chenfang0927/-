"""
    函数式编程 - 思想
        面向对象
            封装：分
            继承: 隔
        函数式编程
            分：将变化点分为多个函数
            隔: 使用参数隔离具体变化的函数
    练习:exercise05
"""

list01 = [42,45,5,66,7,89]

# 需求：定义函数,获取所有大于10的数字
def find01():
    for item in list01:
        if item > 10:
            yield item

# 需求：定义函数,获取所有偶数
def find02():
    for item in list01:
        if item % 2 == 0:
            yield item

for number in find01():
    print(number)

for number in find02():
    print(number)


# －－－－－－－－－－－－－－－－－－

# 提取变化函数
def condition01(item):
    return item > 10

def condition02(item):
    return item % 2 == 0

# 提取通用函数 -- 万能查找
def find(func):#　创建了钩子
    for item in list01:
        # if item % 2 == 0:
        # if condition02(item):
        if func(item):# 拉起钩子(执行条件)
            yield item

for number in find(condition02):# 向钩子上挂条件
    print(number)


from common.iterable_tools import IterableHelper

for number in IterableHelper.find_all(list01, condition01):
    print(number)