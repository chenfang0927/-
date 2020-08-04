"""
    返回列表中所有数字的个位
    方式1:传统思想
        定义函数,创建列表,循环计算每个元素的个位,存入列表
    方式2:生成器思想
        定义函数,循环计算每个元素的个位,通过yield返回
    体会:惰性操作/延迟操作/推算数据
"""

def find_number_unit(list_target):
    list_result = []
    for number in list_target:
        unit = number % 10
        list_result.append(unit)
    return list_result

# 测试
list01 = [54,55,36,67,28,69,90]
result = find_number_unit(list01)
for item in result:
    print(item)



def find_number_unit(list_target):
    for number in list_target:
        unit = number % 10
        yield unit

# 测试
list01 = [54,55,36,67,28,69,90]
# 调用不执行,延迟/惰性
result = find_number_unit(list01)
for item in result:
    print(item)


