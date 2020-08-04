"""
    变量交换
        a, b = b, a
"""
# 变量交换通用思想
# bridegroom_name = "武大郎"
# bride_name = "潘金莲"
# temp = bridegroom_name
# bridegroom_name = bride_name
# bride_name = temp
# print("交换后的新郎：" + bridegroom_name)  #
# print("交换后的新娘：" + bride_name)  #

# a = "武大郎"
# b = "潘金莲"
# c = a
# a = b
# b = c
# print(a)  #
# print(b)  #

a = "武大郎"
b = "潘金莲"
a, b = b, a
print(a)  #
print(b)  #
