"""
    内置生成器
"""
list01 = [54, 5, 6, 76, 8, 9]
# 遍历元素 -- 读取
for item in list01:
    print(item)

# 遍历索引 -- 修改
# for i in range(len(list01)):
#     list01[i] = 0

# 需求:修改奇数为0
# for i in range(len(list01)):
#     if list01[i] % 2:
#         list01[i] = 0

# (索引, 元素)
# for item in enumerate(list01):
for i, element in enumerate(list01):
    if element % 2:
        list01[i] = 0

print(list01)
