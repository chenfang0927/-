"""
    闭包 - 应用
        逻辑连续
            外部函数调用一次,内部函数调用多次,
            内部函数都可以访问外部函数变量

            从一次得钱,到多次花钱的过程,可以连续不中断
"""


def give_gife_money(money):  # 得钱
    print("得到了%d元压岁钱" % money)

    def child_buy(commodity, price):  # 花钱
        nonlocal money
        money -= price
        print("购买了%s,花了%d元,还剩下%d元" % (commodity, price, money))

    return child_buy

action = give_gife_money(1000)
action("变形金刚",200)
action("遥控飞机",500)
action("糖",100)

