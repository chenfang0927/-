"""
    列表基础操作
        遍历
    练习:exercise04
"""
list_names = ["谭锦岳", "杨淮靖", "张昆鹏", "佩琪"]

# 1. 从头到尾　获取所有元素
for item in list_names:
    print(item)

# 修改的是循环遍历item,并不是列表中的元素
# for item in list_names:
#     item = ""

# 2. 通过索引(for + range)定位
# -- 顺序 0 1 2 3
for i in range(len(list_names)):
    if len(list_names[i]) > 2:
        list_names[i] = ""

# -- 倒序 3 2 1 0
# range(开始,结束,间隔)    不包含结束值
#      最大索引 得到0  倒着
# range(总数-1,  -1,  -1)
for i in range(len(list_names) - 1, -1, -1):  #
    print(list_names[i])
