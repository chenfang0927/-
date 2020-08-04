"""
    生成器函数
        给其他人用
    生成器表达式
        给自己使用

"""
list01 = [54, 65.5, True, "a", False, "b", 3, "c"]
# 查找所有字符串
# list_result = []
# for item in list01:
#     if type(item) == str:
#         list_result.append(item)
# print(list_result)

# 列表推导式
list_result = [item for item in list01 if type(item) == str]
for item in list_result:
    print(item)

# 生成器表达式
list_result = (item for item in list01
               if type(item) == str)
for item in list_result:
    print(item)
