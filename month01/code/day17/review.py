"""
    复习
"""
def func01():
    print("第1部分")
    yield "结果1"

    print("第2部分")
    yield "结果2"

    print("第3部分")

"""
class Generate:
    def __next__(self):
        print("第n部分")
        return "结果n"
"""

# 调用函数返回生成器(推算数据),惰性操作/延迟操作
result = func01()
data = result.__next__()
print(data)

data = result.__next__()
print(data)

