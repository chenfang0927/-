"""
    迭代 iter:每一次对过程的重复称为一次“迭代”，
             而每一次迭代得到的结果会作为下一次迭代的初始值。
        可迭代iterable:能够完成迭代过程的对象.
        迭代器iterator:实施迭代过程的对象
    练习:exercise01
"""
message = "我是齐天大圣孙悟空"
# for item in message:
#     print(item)

# for 循环原理
# 1. 获取迭代器对象
iterator = message.__iter__()
while True:
    try:
        # 2. 获取下一个元素
        item = iterator.__next__()
        print(item)
        # 3. 如果没有元素,则停止循环.
    except StopIteration:
        break

# 面试题:可以参与for循环的条件是?
# 能够获取迭代器对象(可迭代对象)
# 具有__iter__函数
