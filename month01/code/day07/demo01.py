"""
    for for 嵌套
        1. 在思想上讲，从内到外编写
        2. 在执行过程，外层执行一次执行多次
        3. 在行列控制，外层决定行内层决定列
    练习:exercise01~03
"""

"""
print("老王",end = " ")
print("老王",end = " ")
print("老王",end = " ")
print("老王",end = " ")
print("老王",end = " ")
# 换行
print()

print("老王",end = " ")
print("老王",end = " ")
print("老王",end = " ")
print("老王",end = " ")
print("老王",end = " ")
# 换行
print()
"""

# 外层循环控制行
for r in range(2):  # 0       1
    # 内层循环控制列
    for c in range(5):  # 01234   01234
        print("老王", end=" ")
    print()
