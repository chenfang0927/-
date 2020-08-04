"""
    条件表达式
        根据条件给变量赋值
"""
# if input("请输入性别:") == "男":
#     value = 1
# else:
#     value = 0

value = 1 if input("请输入性别:") == "男" else 0

print("性别编号：" + str(value))
