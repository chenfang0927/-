"""
    MyRange2.0
    使用 yield 代替迭代器
"""
class MyRange:
    def __init__(self, end):
        self.end = end

    # 使用yield 返回0~4
    def __iter__(self):
        start = 0
        while start <  self.end:
            yield start
            start += 1

for item in MyRange(5):
    print(item)