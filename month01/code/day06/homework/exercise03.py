"""
    3. 将列表中整数的个位不是5和3的数字存入另外一个列表
        list03 = [25, 63, 27, 75, 70, 83, 27]
    结果:[27, 70, 27]
"""
list03 = [25, 63, 27, 75, 70, 83, 27]
result = []
for item in list03:
    unit = item % 10
    if unit == 5 or unit == 3:
        continue
    result.append(item)
print(result)
