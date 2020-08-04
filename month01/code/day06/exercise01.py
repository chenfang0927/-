"""
    在终端中循环录入内容,如果录入空字符串则停止.
    打印所有录入的内容(字符串)
"""

list_city = []
while True:
    city = input("请输入疫情地区:")
    if city == "":
        break
    list_city.append(city)
str_city = "-".join(list_city)
print(str_city)
