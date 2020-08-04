"""
    bool 类型转换

    if 语句真值表达式
"""
# 为false的值： 0   0.0    ""  空None ....
result = bool(None)
print(result)

message = input("请输入：")
# if message != "": # 输入的不是空
# if message != 0:
if message:  # bool(message) 输入的有值
    print("您输入的是:" + message)
else:
    print("您没有输入")
