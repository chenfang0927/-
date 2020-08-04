"""
    自定义排序算法
    练习:exercise03
"""
# 核心思想：
# 确定第一个元素是最大值
# 确定第二个元素是最大值
# ...
# 确定第倒数第二个元素是最大值

# 步骤：
# 1.取出前几个数据(不要最后一个)
# 2.与后面元素进行比较
# 3.发现更xx则交换(取出的   比较的)
list01 = [43, 15, 5, 67, 87, 9]
for r in range(len(list01) - 1):  # 0   1
    for c in range(r + 1, len(list01)):
        if list01[r] > list01[c]:
            list01[r], list01[c] = list01[c], list01[r]
print(list01)