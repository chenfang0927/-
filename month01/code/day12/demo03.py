"""
    运算符重载
        增强运算符 +=  -=  *=  /=   ...
        + 无论可变还是不可变对象,都创建新对象

        += 对于可变对象,在原有基础上进行修改
           对于不可变对象,创建新对象
    练习:exercise02

"""


class Vector2:
    """
        二维向量
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # +=
    def __iadd__(self, other):
        # 因为自定义类是可变对象
        # 所以返回原有对象self,不是创建新对象
        self.x += other.x
        self.y += other.y
        return self

pos01 = Vector2(1, 2)
print(id(pos01))
pos01 += Vector2(3, 4)
print(id(pos01))

"""
# += 对于可变对象,在原有基础上进行修改
list01 = [1]
print(id(list01))# 139887136870152
list01 += [2]
print(id(list01))# 139887136870152

# += 对于不可变对象,创建新对象
tuple01 = (1,)
print(id(tuple01))# 139887167310872
tuple01 += (2,)
print(id(tuple01))# 139887136858376
"""
