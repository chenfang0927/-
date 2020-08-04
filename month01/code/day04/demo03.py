"""
    累计运算
        步骤：
            循环前 -- 创建
            循环中 -- 累加
            循环后 -- 结果
    练习:exercise03~05

"""
# 打印结果：1 2 3 4 5
# 运算：1  + 2 + 3 + 4 + 5
# 核心思想：  之前      累加   当前
#         sum_value  +=   count
sum_value = 0  # 之前
count = 1
while count < 6:
    sum_value += count
    count += 1  # 当前
print(sum_value)
