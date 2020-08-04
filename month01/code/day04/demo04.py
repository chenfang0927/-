"""
    猜数字游戏2.0版本
        增加最多猜3次的功能
        超过次数提示：游戏失败
        猜对了提示：对了,总共猜了x次

    while 条件:
        循环体
    else:
        循环条件不满足，才执行
        从循环体中的break退出,不执行.
"""
import random

random_number = random.randint(1, 100)
count = 0
while count < 3:
    count += 1
    input_number = int(input("你猜是哪个数字:"))
    if input_number > random_number:
        print("大了")
    elif input_number < random_number:
        print("小了")
    else:
        print("对了,总共猜了" + str(count) + "次")
        break
else:
    print("游戏失败")