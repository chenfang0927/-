"""
    小明一次请多个保洁打扫卫生
    效果:调用一次小明通知方法,可以有多个保洁在打扫卫生.
"""


class Client:
    def __init__(self, name=""):
        self.name = name

    # def notify_multiple(self, list_household_service):
    #     print(self.name, "通知")
    #     for service in list_household_service:
    #         service.cleaning()

    def notify_multiple(self, *args):
        print(self.name, "通知")
        for service in args:
            service.cleaning()


class Cleaner:
    def cleaning(self):
        print("打扫卫生")


xm = Client("小明")
# list_cleaners = [
#     Cleaner(),
#     Cleaner(),
#     Cleaner(),
# ]
# xm.notify_multiple(list_cleaners)

xm.notify_multiple(Cleaner(),
                   Cleaner(),
                   Cleaner())

