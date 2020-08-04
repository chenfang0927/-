"""
    while 循环
        语法
            while 条件：
                满足条件执行的循环体
        写法1：延长程序的生命周期
            while True:
                循环体
                if 条件:
                    break
    练习:exercise01
"""
# si循环
while True:
    num = int(input("请输入电梯承载人数:"))
    weight = float(input("请输入电梯承载重量:"))
    if num <= 10 and weight <= 1000:
        print("电梯正常运行")
    else:
        print("电梯超载")
    if input("请输入q键退出：") == "q":
        break  # 跳出循环
