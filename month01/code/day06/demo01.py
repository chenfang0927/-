"""
    列表 --> 字符串
        将多个字符串拼接为一个列表。
        result = "连接符".join(列表)
    练习：exercise01
"""
list01 = ["孙悟空", "猪八戒", "唐僧"]
# 孙悟空_猪八戒_唐僧
result = "_".join(list01)
print(result)

# 需求：根据xxx逻辑拼接字符串
# 缺点：每次拼接+ 都会产生新字符串对象(之前的数据就成为了垃圾)
# 解决方案核心思想：使用可变对象代替不可变对象

# result = ""
# for number in range(10):
#     + 产生新字符串
#     result = result + str(number)
# print(result)

list_result = []
for number in range(10):
    # append 在原有列表上追加
    list_result.append(str(number))
str_result = "".join(list_result)
print(str_result)
