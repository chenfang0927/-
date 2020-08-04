"""
6.  自定义算法实现下列功能
    list01 = [3,9,34,26,5,6,7,8,9,6]
    (1)在list01中找出最小值
    (2)对liest01进行降序排列
    (3)删除list01中大于10的元素
    (4)删除list01中重复的元素
"""
list01 = [3, 9, 34, 26, 5, 6, 7, 8, 9, 6]
# (1)
min_value = list01[0]
for i in range(1, len(list01)):
    if min_value > list01[i]:
        min_value = list01[i]
print(min_value)
# (2)
for r in range(len(list01) - 1):
    for c in range(r + 1, len(list01)):
        if list01[r] < list01[c]:
            list01[r], list01[c] = list01[c], list01[r]
print(list01)
# (3)
for i in range(len(list01) - 1, -1, -1):
    if list01[i] > 10:
        del list01[i]
print(list01)
# (4)
for r in range(len(list01) - 1, 0, -1):
    for c in range(r):
        if list01[r] == list01[c]:
            del list01[r]
            break
print(list01)
