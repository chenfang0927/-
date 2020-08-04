"""
   计算梯形面积
        在终端中获取上底,下底和高
        输出面积
"""

top_base = float(input("请输入上底："))
bottom_base = float(input("请输入下底："))
height = float(input("请输入高："))
result = (top_base + bottom_base) * height / 2
print("梯形面积是：" + str(result))
