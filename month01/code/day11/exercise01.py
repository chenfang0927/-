"""
    小明请保洁打扫卫生
         1. 识别对象
            小明     保洁
         2. 分配职责
            通知     打扫
         3. 建立交互
            小明调用保洁的打扫方法

        要求：使用三种写法实现，说出不同的语义.
"""

# 写法一：小明每次请一个新保洁
"""
class Client:
    def __init__(self, name=""):
        self.name = name

    def notify(self):
        print(self.name,"发出通知")
        cleaner = Cleaner()
        cleaner.cleaning()

class Cleaner:
    def cleaning(self):
        print("保洁打扫卫生")

xm = Client("小明")
xm.notify()
"""

# 写法二：小明请自己的保洁
"""
class Client:
    def __init__(self, name=""):
        self.name = name
        self.cleaner = Cleaner()

    def notify(self):
        print(self.name,"发出通知")
        self.cleaner.cleaning()

class Cleaner:
    def cleaning(self):
        print("保洁打扫卫生")

xm = Client("小明")
xm.notify()
"""

# 写法三：小明请家政服务(参数  保洁)
class Client:
    def __init__(self, name=""):
        self.name = name

    def notify(self, household_service):
        print(self.name, "发出通知")
        household_service.cleaning()


class Cleaner:
    def cleaning(self):
        print("保洁打扫卫生")


xm = Client("小明")
bj = Cleaner()
xm.notify(bj)
