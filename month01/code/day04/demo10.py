"""
    字符串字面值
"""
# 1. 写法
name01 = "悟空"  # (推荐)
name02 = '悟空'
# 可见即所得
name03 = """
悟
  空"""
name04 = '''悟空'''

# 2.
#  单引号内的双引号不算结束符
#  双引号内的单引号不算结束符
message = '我是"孙悟空"。'
message = "我是'孙悟空'。"


# 3. 转义字符:改变原始含义的特殊字符
# \"  \'    换行\n   \\
message = "我是\"孙悟空\"。"
print(message)# 我是"孙悟空"。

message = "我是\n孙悟空。"
print(message)#

url = "\\a\\b\c\d\e.txt"
# 原始字符：后面的字符串木有转义字符
url = r"\a\b\c\d\e.txt"
print(url)
