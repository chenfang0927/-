# 练习：让下列代码循环执行,输入y键继续.
while True:
    state = "奇数" if int(input("请输入一个整数：")) % 2 else "偶数"
    print(state)
    if input("输入y键继续") != "y":
        break
