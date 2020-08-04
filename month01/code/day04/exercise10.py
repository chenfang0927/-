# 1. 在终端中录入一个内容,
#   循环打印每个文字的编码值。
content = input('请输入内容:')
for name in content:
    print(ord(name))

# 2. 循环录入编码值,打印文字.
#    直到输入空字符串,停止。
while True:
    content = input("请输入：")
    if content == "":
        break
    content = int(content)
    print(chr(content))