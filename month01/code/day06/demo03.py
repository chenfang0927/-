"""
    列表推导式
        根据可迭代对象构建列表时

        变量 = [表达式 for 变量 in 可迭代对象 if 条件]
    练习:exercise03
"""
list01 = [34, 45, 5, 65, 76, 8]
# 快捷键：iter + 回车
# list_result = []
# for number in list01:
#     if number > 10:
#         list_result.append(number)
# print(list_result)

list_result = [number for number in list01 if number > 10]

# list_result = []
# for number in list01:
#     list_result.append(number % 10)
# print(list_result)

list_result = [number % 10 for number in list01]
print(list_result)
