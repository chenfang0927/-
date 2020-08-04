"""
    总结容器：统一管理数据
        字符串str:储存字符编码值,不可变,序列
        列表list:储存变量,可变,序列
        元组tuple:储存变量,不可变,序列
        字典dict:储存键值对,可变,散列
            键不能重复且不可变
        集合set:储存键,可变,散列

        不可变：数据在内存中本质都是不可变,采用按需分配的存储机制
        可变：具有扩容能力,采用预留空间的存储机制
        序列：相邻有序,定位灵活(索引、切片)
        散列：分散无序,定位迅速(键)
        列表:存储单一维度的数据,例如:治愈人数列表,地区列表
        字典：存储多个维度的数据,例如:学生信息,疫情列表
"""
# 1. 创建
dict01 = {"a": "A", "b": "B"}
list01 = [10, 20, 30]
list02 = list(dict01)  # ['a', 'b']
list03 = list(dict01.values())  # ['A', 'B']
list04 = list(dict01.items())  # [('a', 'A'), ('b', 'B')]

# 列表转换为字典的格式要求：列表中元素必须能够一分二
list05 = [('a', 'A'), ('b', 'B')]
dict02 = dict(list05)  # {'a': 'A', 'b': 'B'}

# 2.添加
list01.append(40)
list01.insert(1, 50)

dict01["c"] = "C"

# 3. 定位  容器名称[整数]   容器名称[开始:结束:间隔]
print(list01[0])
list01[-1] = 100

print(list01[:2])
# 遍历右侧,依次存入左侧
list01[-2:] = "悟空"

# import random
# # 包含开始结束
# random.randint(1,10)

# 删除
list01.remove(20)
del list01[0]
print(list01)

# 遍历
# 从头到尾读取
for item in list01:
    print(item)
# 根据索引定位
for i in range(len(list01)):
    print(list01[i])

# 键值对
for k,v in dict01.items():
    print(k)
    print(v)
# 键
for k in dict01:
    print(k)
# 值
for v in dict01.values():
    print(v)