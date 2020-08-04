"""
    5. 在终端中循环录入年龄,如果录入空,则退出循环.
       最后打印平均年龄(总年龄除以人数)
"""
sum_of_ages = 0
count_of_person = 0
while True:
    age = input("请输入年龄:")
    if age == "":
        break
    sum_of_ages += int(age)
    count_of_person += 1

# print("平均年龄是:%.2f岁" % (sum_of_ages / count_of_person))
print(f"平均年龄是:{sum_of_ages / count_of_person:.2f}岁")
