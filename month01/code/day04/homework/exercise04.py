"""
    魏老师很不幸买了一箱有虫子(1)的苹果
    虫子吃完一个苹果再吃另外一个苹果
    在终端中输入苹果数量(个),虫子吃苹果的速度(小时/个),经过时间(小时)
    请打印没有被虫子吃过的苹果数量（最小也是0）
"""

total_count = int(input("请输入苹果总数："))
speed = float(input("虫子吃苹果的速度(小时/个):"))
duration = float(input("请输入经过时间(小时):"))
# 虫子吃的苹果数 duration / speed
# 剩下的苹果数 total_count - duration / speed
# 没有被虫子吃过的苹果数量 int(  3.9  )  -->  3
remain_count = int(total_count - duration / speed)
if remain_count > 0:
    print("没有被虫子吃过的苹果数:" + str(remain_count))
else:
    print("没有苹果啦")
