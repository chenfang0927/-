"""
   在终端中录入一个整数, 打印每位相加和。
"""
number = input("请输入一个整数：")  # "1234"

sum_value = 0
for item in number:  # "1"   "2"   "3"  "4"
    sum_value += int(item)
print(sum_value)
