"""
re 模块函数使用示例
"""
import re

s = "Alex:1998,Sunny:1997" # 目标字符串
pattern = r"(\w+):(\d+)" # 正则

# 正则表达式有子组的时候，只获取子组对应的匹配内容
l = re.findall(pattern,s)
print(l)

# 使用正则表达式匹配到的内容对目标字符串切割
l = re.split(r"\W+",s,2)
print(l)

# 使用\W+匹配目标字符串s，使用## 替换匹配到的内容
s = re.sub(r"\W+",'##',s,2)
print(s) # 得到替换后的字符串