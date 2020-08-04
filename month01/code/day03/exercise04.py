# 练习:在终端中获取性别,
# 打印"您好先生" "您好女士" "性别未知"

sex = input("请输入性别：")
if sex == "男":
    print("您好先生")
elif sex == "女":
    print("您好女士")
else:
    print("性别未知")
