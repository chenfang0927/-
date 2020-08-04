"""
   练习１：在终端中录入５次数字，然后打印累加和.

   练习２：在终端中录入数字,如果录入空字符串则停止录入,
   最后打印累加和.
"""
# 1
sum_value = 0
# 因为在循环体中没有需求使用for循环变量,
# 所以建议使用双下划线命名.
for __ in range(5):
    number = input("请输入一个整数")
    sum_value += int(number)
print(sum_value)

# 2
sum_value = 0
while True:
    number = input("请输入一个整数:")
    # if number == "":
    #     break
    # else:
    #     sum_value += int(number)
    if number == "":
        break  # 是空跳出循环
    sum_value += int(number)
print(sum_value)
