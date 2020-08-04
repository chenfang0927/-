"""
    彩票模拟器
        -- 创建随机彩票(一个列表,前六个是红球,最后一个是蓝球)
    双色球：
        红球：6个,1-33之间（包含）,不能重复
        蓝色：1个,1--16之间（包含）
"""
import random

list_ticket = []
# for number in range(6): # 不是预定次数循环,因为可能某一次产生的随机数与前面重复
while len(list_ticket) < 6: # 条件:列表元素不足6个
    number = random.randint(1, 33)
    if number not in list_ticket:
        list_ticket.append(number)

list_ticket.append(random.randint(1, 16))
print(list_ticket)
