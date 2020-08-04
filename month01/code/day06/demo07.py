"""
    集合set
        价值1：去重复
"""

# 1. 创建
set01 = {"悟空", "八戒", "唐三藏"}

list01 = [10, 20, 30, 20, 30, 40]
set02 = set(list01)
print(set02)

# 2. 添加  集合名.add(元素)
set01.add("qtx")

# 3. 删除  集合名.remove(元素)
set01.remove("八戒")

# 4. 遍历
for item in set01:
    print(item)


