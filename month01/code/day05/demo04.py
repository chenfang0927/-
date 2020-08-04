"""
    列表基础操作
        列表创建
        列表添加
    练习:exercise02
"""
# 1. 创建
#   列表名称 = [元素１,元素２,元素３]　
list_names = ["谭锦岳", "杨淮靖", "张昆鹏"]
#   列表名称 = list(其他容器)
list01 = list("孙悟空")

# 2. 添加
# -- 追加
# 列表名称.append(元素)
list_names.append("王韵璇")
# -- 插入
# 列表名称.insert(需要插入的索引,元素)
list_names.insert(0,"张帆")
