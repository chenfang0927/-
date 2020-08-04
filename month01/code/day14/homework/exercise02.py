"""
    小明使用手机打电话
    要求:增加座机,卫星电话时不影响小明.
    写出案例中体现的面向对象三大特征和六大原则.
        封装:创建人类Person,手机类MobilePhone,座机类Landline
        继承:创建通信工具Communication,隔离人类Person与具体通信工具类(手机类MobilePhone,座机类Landline)
        多态:人类调用通信工具,具体通信工具类重写通信工具dialing,创建手机对象,座机对象
             编码时调用父,                                  运行时执行子.
             彰显子类的个性(变化/具体实现方式)
        开闭原则:增加座机,卫星电话时不影响人类
        单一职责:人类负责xxxx,手机类负责xxx,座机类负责xxx
        依赖倒置:人类调用通信工具,不调用具体通信工具(手机类,座机类)
        组合复用:组合关系连接了人类与通信工具的变化
                继承关系统一了手机类,座机类
        里氏替换:人类打电话函数的形参是通信工具,调用时传递各种具体通信工具.
        迪米特:人类 与 具体通信工具低耦合
              各种通信工具之间低耦合
"""
# 餐厅
# 迎宾 -- 点餐服务员 -- 厨师 -- 配送员


class Person:
    def __init__(self, name=""):
        self.name = name

    def call(self, communication):
        print(self.name, "打电话")
        # 1. 编码时  调用父
        # 运行时  执行子
        communication.dialing()


class Communication:
    def dialing(self):
        pass


class MobilePhone(Communication):
    # 2. 体现个性(实现变化)
    def dialing(self):
        print("手机呼叫")


class Landline(Communication):
    def dialing(self):
        print("座机呼叫")


xm = Person("小明")
# 3. 创建子对象
xm.call(MobilePhone())
xm.call(Landline())
