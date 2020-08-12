"""
re 模块函数使用示例2
"""
import re

s = "   Alex:1998,Sunny:1997" # 目标字符串
pattern = r"(\w+):(?P<year>\d+)" # 正则

# 将匹配到的内容生成一个迭代对象
l = re.finditer(pattern,s)
for i in l:
    # 每次取出一个匹配内容对应的match对象
    print(i.group('year'))  # 获取match对应内容

# 匹配目标开头
# obj = re.match(pattern,s)
# print(obj.group())

# 匹配目标字符串第一处符合规则的地方
obj = re.search(pattern,s)
print(obj.group())

# 获取匹配到的内容在目标字符串中的位置 s[3:12]
print(obj.span())

# 捕获组组名和对应内容形成的字典
print(obj.groupdict())