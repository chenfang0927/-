"""
    for + range

    整数生成器　range
        字面意思：范围
        价值：生成一个范围内的整数
    练习:exercise07
"""
# 写法１：range(开始,结束,间隔)
#        不包含结束值
for number in range(0, 5, 1):  # 0 1 2 3 4
    print(number)

# 写法2：range(开始,结束)
#        间隔 默认为１
for number in range(0, 5):  # 0 1 2 3 4
    print(number)

# 写法3：range(结束)
#       开始 默认为0
for number in range(5):  # 0 1 2 3 4
    print(number)
