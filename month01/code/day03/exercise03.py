"""
   练习1:
        满足年龄大于25 并且 身高小于170 条件 "入职",否则"拒绝"
   练习2:
        满足 高、富、帅 条件,"闺女嫁给你",否则"去学习吧"
"""
if int(input("请输入年龄：")) > 25 and float(input("请输入身高：")) < 170:
    print("入职")
else:
    print("拒绝")

if int(input("请输入身高")) > 180 and int(input("请输入财产:")) > 10000000 and int(input("请输入颜值:")) > 95:
    print("闺女嫁给你")
else:
    print("去学习吧")
