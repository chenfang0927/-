"""
    common/
        iterable_tools.py
    可迭代对象工具
"""

# 1. 教学意义：深刻掌握函数式编程思想
#            　　分、隔、做
# 2. 实用价值：在开发过程中,不断壮大自定义高阶函数
#               功能更强大
# 3. 利于面试：精通函数式编程
#               常常遇到xx功能,发现实现方式大部分逻辑相同,只是核心xx不同,
#               我就将共性提取到xx类中,放到单独的模块中.
#               在各种项目中,直接导入使用.
#            思想来源于微软Linq技术

class IterableHelper:
    """
        可迭代对象助手
    """

    @staticmethod
    def find_all(iterable, func):
        for item in iterable:
            if func(item):
                yield item

    @staticmethod
    def find_single(iterable, func):
        for emp in iterable:
            if func(emp):
                return emp

    @staticmethod
    def select(iterable, func):
        for emp in iterable:
            yield func(emp)

    @staticmethod
    def delete_all(iterable, func):
        count = 0
        for i in range(len(iterable) - 1, -1, -1):
            # if iterable[i].money < 15000:
            # $调用传入的函数lambda
            if func(iterable[i]):
                del iterable[i]
                count += 1
        return count

    @staticmethod
    def get_max(iterable, func):
        max_value = iterable[0]
        for i in range(1, len(iterable)):
            # if max_value.money < iterable[i].money:
            # if xx(max_value) < xx(iterable[i]):
            if func(max_value) < func(iterable[i]):
                max_value = iterable[i]
        return max_value

    @staticmethod
    def ascending_order(iterable, func):
        for r in range(len(iterable) - 1):
            for c in range(r + 1, len(iterable)):
                # if iterable[r].money > iterable[c].money:
                if func(iterable[r]) > func(iterable[c]):
                    iterable[r], iterable[c] = iterable[c], iterable[r]

# def xx(item):
#     return item.money

# lambda item:item.money
