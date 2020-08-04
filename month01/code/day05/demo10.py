"""
    深拷贝
"""
# 准备一个拷贝工具
import copy

list01 = [10, [20, 30], [40, 50]]
list02 = list01 # 赋值
list03 = list01[:] # 浅拷贝
list04 = copy.deepcopy(list01)# 深拷贝