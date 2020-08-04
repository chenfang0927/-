"""
    字典dict
    练习:exercise06
"""

# 1. 创建
# --使用元素创建
dict01 = {"qtx": 100000, "wk": 100000, "bj": 200000}
# --使用其他容器(该容器内的元素必须能够一分二)
list01 = [("唐僧", 50000), ["猪八戒", 60000], "沙僧"]
# {'唐僧': 50000, '猪八戒': 60000, '沙': '僧'}
dict02 = dict(list01)
print(dict02)

# 2. 添加(字典不存在该key)  字典[键] = 值
if "ss" not in dict01:
    dict01["ss"] = 700000

# 3. 定位  字典名[键]
# -- 读取
print(dict01["wk"])
# -- 修改
if "qtx" in dict01:
    dict01["qtx"] = 500000

# 4. 删除 del 字典名[键]
del dict01["bj"]

# 5. 遍历
# -- 所有键
# for 键名 in 字典:
for key in dict01:
    print(key)

# -- 所有值
# for 值名 in 字典.values():
for value in dict01.values():
    print(value)

# -- 所有键和值
# for 键,值 in 字典.items():
# 不建议
# for item in dict01.items():
#     print(item[0])
#     print(item[1])

for key, value in dict01.items():
    print(key)
    print(value)
