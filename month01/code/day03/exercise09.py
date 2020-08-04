"""
    在终端中获取月份，打印相应的天数.
    1 3 5 7 8 10 12 有 31天
    2有28天
    4  6  9  11 有 30天
    输入的月份有误
"""
month = int(input("请输入月份:"))
if month <= 0 or month >= 12:
    print("输入的月份有误")
else:
    # 月份输入正确
    if month == 2:
        print("28天")
    elif month == 4 or month == 6 or month == 9 or month == 11:
        print("30天")
    else:  # 1 3 5 7 8 10 12
        print("31天")
