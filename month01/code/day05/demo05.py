"""
    列表基础操作
        定位
            读取
            修改
    练习:exercise03
"""
list_names = ["谭锦岳", "杨淮靖", "张昆鹏"]
# 1. 索引
item = list_names[0]  # 读取第一个元素
list_names[0] = "tjy"  # 修改第一个元素

# 2. 切片
# 通过切片读取元素时会创建新列表
items = list_names[1:]  # 读取后两个元素
# 通过切片修改元素时会遍历右侧数据,依次存入左侧定位的区域
list_names[1:] = ["yhj", "zkp"]  # 修改后两个元素
# list_names[1:] = "行吗" # ['tjy', '行', '吗']

# 左侧切片1个位置   右侧４个数据
list_names[1:1] = ["a", "b", "c", "d"]  # ['tjy', 'a', 'b', 'c', 'd', 'yhj', 'zkp']
# 左侧切片全部位置   右侧０个数据
# list_names[:] = []# 列表没有元素
print(list_names)
