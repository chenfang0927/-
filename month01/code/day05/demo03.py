"""
    切片　
        容器名[开始:结束:间隔]  不包含结束索引的元素
        容器名[开始:结束]  间隔默认为１
        容器名[:结束]  开始默认为0
        容器名[:]  开始默认为0
        容器名[::-1]  从尾到头
"""
# for number in range( 开始 ,结束 ,间隔 ):
# for number in range( 开始 ,结束):
# for number in range(结束):

message = "我是花果山水帘洞美猴王齐天大圣"
print(message[0:3:1])  # 我是花
print(message[0:8:2])  # 我花山帘
print(message[0:3])  # 我是花
print(message[:3])  # 我是花
print(message[:])  # 我是花果山水帘洞美猴王齐天大圣
print(message[3:])  # 果山水帘洞美猴王齐天大圣
print(message[3:-1])  # 果山水帘洞美猴王齐天大
print(message[::-1])  #圣大天齐王猴美洞帘水山果花是我
print(message[2:250])  # 花果山水帘洞美猴王齐天大圣
print(message[2:7:-1])  #空
print(message[7:2])  #空


