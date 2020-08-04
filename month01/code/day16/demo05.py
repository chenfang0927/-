"""
    yield --> 生成器
    MyRange3.0
    类 --> 函数
    练习:exercise08/09
"""
"""
class Generator:# 生成器 = 可迭代对象 + 迭代器
    def __iter__(self): # 可迭代对象
        return self
    
    def __next__(self): # 迭代器
        ....
"""
def my_range(end):
    start = 0
    while start < end:
        yield start
        start += 1

for item in my_range(5):
    print(item)

# 延迟操作/惰性操作
# 循环一次 计算一次 返回一次
range = my_range(5)
iterator = range.__iter__()
while True:
    try:
        item = iterator.__next__()
        print(item)
    except StopIteration:
        break