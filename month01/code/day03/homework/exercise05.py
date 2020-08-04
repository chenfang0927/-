"""
    画出内存图
"""
data01 = 100  # 创建变量关联数据100
data02 = 200
data03 = data01 + data02
data01 = 200  # 修改变量存储的数据地址
print(data03)  # ?
