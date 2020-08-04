"""
    练习:自学其他算数运算符与增强运算符重载
          -             -=
          *             *=
        创建新对象     返回原对象
"""


class Vector2:
    """
        二维向量
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __multiplication(self, other):
        if type(other) == Vector2:
            x = self.x * other.x
            y = self.y * other.y
        else:  # 默认为int类型
            x = self.x * other
            y = self.y * other
        return x, y

    def __mul__(self, other):
        x, y = self.__multiplication(other)
        # 返回新对象
        return Vector2(x, y)

    def __imul__(self, other):
        x, y = self.__multiplication(other)
        # 返回原对象
        self.x = x
        self.y = y
        return self


pos01 = Vector2(1, 2)
pos02 = Vector2(3, 4)
pos03 = pos01 * pos02  # pos01.__mul__(pos02)
print(pos03.__dict__)  #

pos04 = pos01 * 2
print(pos04.__dict__)  #

pos01 *= pos02
print(pos01.__dict__)  #

pos01 *= 2
print(pos01.__dict__)  #
