"""
    自定MyRange类
    实现range(5)效果
"""


class MyRangeIterator:# 迭代器
    def __init__(self,stop):
        self.number = -1
        self.stop = stop

    def __next__(self):
        self.number += 1
        if self.number  < self.stop:
            return self.number
        else:
            raise StopIteration()

class MyRange:
    def __init__(self, end):
        self.end = end

    def __iter__(self):# 可迭代对象
        return MyRangeIterator(self.end)

# for item in MyRange(5):  # 0~4
#     print(item)

# 可以生成撑爆内存的数字
# 循环一次  计算一次  返回一次
for item in MyRange(9999999999999999999999999999999):
    print(item)

for item in range(9999999999999999999999999999999):
    print(item)
