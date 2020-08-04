"""
    逻辑运算符
        判断多个命题关系
            与and -- > 并且
            或 --> 或者
            非 --> 取反
        语法：
            命题1  and 命题2     都满足
            命题1  or 命题2      一个就行
            not 命题1           取反
    练习：exercise02

"""
# 来自丈母娘的灵魂质问：
# 1. 有钱  并且  有才
# int(input("请输入你的财产：")) > 10000000
# input("请问您是否有才华：") == "有"

# result = int(input("请输入你的财产：")) > 10000000  and input("请问您是否有才华：") == "有"
# print(result)

# 2. 有钱  或者  有才
# result = int(input("请输入你的财产：")) > 10000000  or input("请问您是否有才华：") == "有"
# print(result)

# 3. 非 not
print(not True) # False
