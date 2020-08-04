"""
    common/
        iterable_tools.py
    可迭代对象工具
"""
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
    def find_single(iterable,func):
        for emp in iterable:
            if func(emp):
                return emp

    @staticmethod
    def select(iterable,func):
        for emp in iterable:
            yield func(emp)

# for item in IterableHelper.find(列表,函数):
#  ...

"""
class Wife:
    def __init__(self, name):
        self.name = name

    def work(self):
        print(self.name, "在工作")


w01 = Wife("双儿")
w01.work()  # 实例方法自动传递对象,是因为方法内需要访问实例成员
"""
