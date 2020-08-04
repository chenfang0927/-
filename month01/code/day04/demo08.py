"""
    循环对比：
    while 循环:根据条件重复执行
    　　　　　　例如：纸张对折到珠穆拉玛峰

    for 循环：重复获取容器元素
    for+range：根据次数重复执行
            　　例如：累加１－１００之间数字
    练习:exercise09
"""sum_value = 0
# 因为在循环体中没有需求使用for循环变量,
# 所以建议使用双下划线命名.
for __ in range(5):
    number = input("请输入一个整数")
    sum_value += int(number)
print(sum_value)