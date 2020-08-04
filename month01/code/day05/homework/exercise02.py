"""
    在终端中循环录入5个人的年龄,
    最后打印平均年龄(总年龄除以人数)
"""
sum_of_ages = 0
count_of_person = 5
for __ in range(count_of_person):
    age = int(input("请输入年龄："))
    sum_of_ages += age
# print("平均年龄是:%.2f岁" % (sum_of_ages / count_of_person))
print(f"平均年龄是:{sum_of_ages / count_of_person:.2f}岁")
