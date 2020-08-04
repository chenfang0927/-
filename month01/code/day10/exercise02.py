"""
    对象计数器
        统计Wife类创建了多少对象
        画出内存图
            w01 = Wife("建宁")
            w02 = Wife("双儿")
            w03 = Wife("苏荃")
            Wife.print_count() # 3
"""


class Wife:
    count = 0

    @classmethod
    def print_count(cls):
        # print( Wife.count)
        print("我已经娶了%d个了" % cls.count)

    def __init__(self, name):
        self.name = name
        Wife.count += 1


w01 = Wife("建宁")
w02 = Wife("双儿")
w03 = Wife("苏荃")
Wife.print_count()  # 3
