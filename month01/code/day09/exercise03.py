"""
    调用下列函数
"""


def func01(*args, **kwargs):  # 实参数量无限
    print(args)
    print(kwargs)


func01()
func01(1, 2, a=1, b=2)


# p1:位置形参:必填
# p2:位置形参+默认形参:可选
# args:星号元组形参：位置实参数量无限
# p3:命名关键字形参+默认形参:关键字实参(可选)
# kwargs:双星号字典形参：关键字实参数量无限
def func02(p1, p2="", *args, p3=0, **kwargs):
    print(p1)
    print(p2)
    print(args)
    print(p3)
    print(kwargs)

func02(1,2,3,4,5,p3 = 3,a=1,b=2)
func02(1)