# 累加10 -- 60之间,个位不是3/5/8的整数和。
# 思路：各位是３或者５或者８就跳过
sum_value = 0
for number in range(10, 61):
    unit = number % 10
    if unit == 3 or unit == 5 or unit == 8:
        continue
    sum_value += number
print(sum_value)
