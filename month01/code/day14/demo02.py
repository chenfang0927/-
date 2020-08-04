"""
    基本调用
"""

class XXView:
    def __init__(self):
        self.controller = XXController()

    def func01(self):
        self.controller.func02()

class XXController:
    def func02(self):
        print("func02执行喽")

view = XXView()# 内部创建Controller
view.func01() # 内部调用func02

