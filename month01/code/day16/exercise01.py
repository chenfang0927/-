"""
练习1:使用迭代思想，打印元组中所有元素。
练习2:不使用for循环，打印字典中所有记录(键和值)
"""
tuple01 = (43, 4, 5, 67, 87, 89)
iterator = tuple01.__iter__()
while True:
    try:
        item = iterator.__next__()
        print(item)
    except StopIteration:
        break

dict01 = {"a": "A", "b": "B"}
iterator = dict01.__iter__()
while True:
    try:
        key = iterator.__next__()
        value = dict01[key]
        print(key, value)
    except StopIteration:
        break
