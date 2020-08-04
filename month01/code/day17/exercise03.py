# 练习1:在列表中获取所有整数,并计算它的平方.
# 练习2:在列表中获取所有大于10的小数.
# 要求：使用列表推导式，生成器表达式完成.
# 通过调试，体会差异.

list01 = [54, 65.5, True, "a", False, "b", 3, "c"]

# 练习1:
list02 = [item ** 2 for item in list01 if type(item) == int]
for number in list02:
    print(number)

generator02 = (item ** 2 for item in list01 if type(item) == int)
for number in generator02:
    print(number)

# 练习2:
list03 = [item for item in list01 if type(item) == float and item > 10]
for number in list03:
    print(number)

generator03 = (item for item in list01 if type(item) == float and item > 10)
for number in generator03:
    print(number)
