"""
    索引Index
        容器名[整数]　
    练习:exercise01
"""
message = "我是花果山水帘洞美猴王齐天大圣"
print(message[0])  # 打印第一个元素
print(message[2])  # 打印第三个元素
print(message[-2])  # 打印倒数第二个元素
# print(message[100])# IndexError: string index out of range
# print(message[-100])# IndexError: string index out of range
print(message[-len(message)])  # 第一个
print(message[len(message) - 1])  # 最后一个
