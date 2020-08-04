"""
    定义函数,在终端中打印矩形.
    ×××××
    ×××××
    ×××××
"""


# for r in range(3):
#     for c in range(5):
#         print("×", end="")
#     print()

# 考虑函数的实用性、通用性
def print_rectangular(height, weidth, fill_char, end_char):
    """
        在终端中打印矩形
    :param height: 高度
    :param weidth: 宽度
    :param fill_char: 填充字符
    :param end_char: 填充字符后的结束字符
    """
    for r in range(height):
        for c in range(weidth):
            print(fill_char, end=end_char)
        print()

print_rectangular(3, 5, "x", "")
print_rectangular(4, 6, "*", "")
print_rectangular(5, 5, "#", " ")
