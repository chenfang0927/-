"""
    彩票模拟器
        -- 在终端中购买彩票(提示：号码已经存在,号码超过范围)
"""

list_ticket = []
while len(list_ticket) < 6:
    # len(list_ticket) + 1 : 第一次列表长度是0,但是显示应该是1
    number = int(input("请输入第%d个红球号码：" % (len(list_ticket) + 1)))
    if number in list_ticket:
        print("号码已经存在")
    elif number < 1 or number > 33:
        print("号码不在范围内")
    else:
        list_ticket.append(number)

while len(list_ticket) < 7:
    number = int(input("请输入蓝球号码："))
    if number < 1 or number > 16:
        print("号码不在范围内")
    else:
        list_ticket.append(number)

print(list_ticket)
