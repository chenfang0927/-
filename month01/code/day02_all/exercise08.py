"""
    古代的秤，一斤十六两。
    在终端中获取两，计算几斤零几两。
"""

amount = int(input("请输入两数:"))
jin = amount // 16
liang = amount % 16
print(str(jin) + "斤零" + str(liang) + "两")
