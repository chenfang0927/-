"""
    函数参数 - 应用
        https://docs.python.org/zh-cn/3/
        https://www.runoob.com/python3/python3-tutorial.html
"""
list01 = [432, 545, 6, 7, 6]
print(list01.count(6))
# 扩展(一次追加多个数据)
list01.extend(["a", "b", "c"])
print(list01)

dict02 = {"a": "A"}
dict03 = {"b": "B"}
# 更新(一次增加多个键值对)
dict02.update(dict03)
print(dict02)

str03 = "函数参数"
