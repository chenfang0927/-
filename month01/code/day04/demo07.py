"""
    continue
    练习:exercise08
"""
# 需求：累加1--100之间所有整数
# sum_value = 0
# for number in range(1, 101):
#     sum_value += number
# print(sum_value)

# 要求：能被3整除的数字
# 思想：满足条件，累加.
# sum_value = 0
# for number in range(1, 101):
#     if number % 3 == 0:
#         sum_value += number
# print(sum_value)

# 思想：不满足条件，跳过.
sum_value = 0
for number in range(1, 101):
    if number % 3 != 0:
        continue  # 跳过　
    sum_value += number
print(sum_value)
