"""
    列表基础操作
        删除
"""
list_names = ["谭锦岳", "杨淮靖", "张昆鹏"]
# 1. 根据元素删除
# 列表名.remove(元素)
list_names.remove("杨淮靖")

# 删除不存在的元素，会报错。
# 建议先判断,如果存在再删除.
if "老张" in list_names:
    list_names.remove("老张")

# 2. 根据定位删除
del list_names[0]
del list_names[:]
print(list_names)