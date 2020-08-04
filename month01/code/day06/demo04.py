"""
    元组 tuple
    练习:exercise04,05
"""

# 1. 创建
# -- 通过元素创建
tuple01 = (10, 20, 30)
# -- 通过其他容器创建
list01 = [40, 50]
tuple02 = tuple(list01)

# 2. 定位
# -- 索引
print(tuple01[-1])

# -- 切片
print(tuple01[-2:])

# 3. 遍历
for item in tuple01:
    print(item)

for i in range(len(tuple01) - 1, -1, -1):
    print(tuple01[i])

# 4. 特殊
# -- 如果元组只有１个元素,必须写逗号
tuple03 = (50,)
# -- 可以省略小括号
# tuple04 = (50,60,70)
tuple04 = 50, 60, 70
# -- 拆包
# a, b = (80, 90)
# a, b = [80, 90]
# a, b = "悟空"
a, *b = (80, 90, 100)
print(a)  # 80
print(b)  # [90, 100]
