"""
    请排列出3个色子可以组合的所有数字
    每个色子数字1—6，可以使用range(1,7)表示
"""
# number = []
# for dice01 in range(1, 7):
#     for dice02 in range(1, 7):
#         for dice03 in range(1, 7):
#             number.append((dice01, dice02, dice03))
# print(number)
number = [(dice01, dice02, dice03) for dice01 in range(1, 7) for dice02 in range(1, 7) for dice03 in range(1, 7)]
print(number)
