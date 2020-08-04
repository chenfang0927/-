"""
    练习1: 创建字典,遍历字典,打印索引/键/值
    练习2: 创建列表,将列表中大于10的数字,设置为0
"""
dict01 = {"a": "A", "b": "B"}
# (0, ('a', 'A'))
# for item in enumerate(dict01.items()):
for i, (k, v) in enumerate(dict01.items()):
    print(i, k, v)

list01 = [5, 6, 67, 8, 9, 9, 65, 43, 7]
for i, item in enumerate(list01):
    if item > 10:
        list01[i] = 0

print(list01)
