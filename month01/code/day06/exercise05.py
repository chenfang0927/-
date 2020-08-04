"""
    容器的思想
        统一管理多个数据
"""
# month = int(input("请输入月份:"))
# if month <= 0 or month >= 12:
#     print("输入的月份有误")
# else:
#     if month == 2:
#         print("28天")
#     # elif month == 4 or month == 6 or month == 9 or month == 11:
#     elif month in (4, 6, 9, 11):
#         print("30天")
#     else:
#         print("31天")

month = int(input("请输入月份:"))
tuple_days = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
print(tuple_days[month - 1])