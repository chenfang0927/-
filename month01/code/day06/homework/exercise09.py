"""
    1. 在终端中录入秒数,  80
       计算几分钟零几秒存入列表[分,秒]   [1,20]

    2. 将第一步重复3次,将每个列表再存入列表
        请输入秒：80
        请输入秒：90
        请输入秒：100
        [[1, 20], [1, 30], [1, 40]]

    3. 打印第二步所有时间,一行一个,格式:x分零x秒
        1分零20秒
        1分零30秒
        1分零40秒
"""
# 1.
# total_second = int(input("请输入秒："))
# minute = total_second // 60
# second = total_second % 60
# time = [minute, second]
# print(time)

# 2.
list_times = []
for __ in range(3):
    total_second = int(input("请输入秒："))
    minute = total_second // 60
    second = total_second % 60
    # 每次循环产生一个新列表
    time = [minute, second]
    list_times.append(time)


# 3.
for time in list_times:
    print(f"{time[0]}分零{time[1]}秒")
