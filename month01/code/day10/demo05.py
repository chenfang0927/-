"""
    私有成员:以双下划线开头的成员
        类外无法访问,类内可以访问
        本质：障眼法
            看着是双下划线命名  __data
            实际是单下划线类名+双下划线命名 _MyClass__data
"""

class MyClass:
    def __init__(self, data=0):
        self.__data = data

    def __func01(self):
        print("func01执行喽")


c01 = MyClass(10)
print(c01.__dict__)
# print(c01.__data)
# c01.__func01()

# 不要试图访问私有成员
# print(c01._MyClass__data)
# c01._MyClass__func01()
