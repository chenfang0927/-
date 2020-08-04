"""
    创建敌人类
    创建实例变量并保证数据在有效范围内
        姓名、血量、攻击力、防御力
              0-100  1 – 30、 0 – 20
"""


# 1. 函数名与变量名必须相同
# 2. 函数体操作双下划线__命名的变量
class Enemy:
    def __init__(self, name="", hp=0, atk=0, defense=0):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.defense = defense

    @property
    def hp(self):
        return self.__hp

    @hp.setter
    def hp(self, value):
        if 0 <= value <= 100:
            self.__hp = value
        else:
            raise Exception("血量超过范围")

    @property
    def atk(self):
        return self.__atk

    @atk.setter
    def atk(self, value):
        if 0 <= value <= 100:
            self.__atk = value
        else:
            raise Exception("攻击力超过范围")

    @property
    def defense(self):
        return self.__defense

    @defense.setter
    def defense(self, value):
        if value < 0:
            value = 0
        elif value > 20:
            value = 20
        self.__defense = value


e01 = Enemy("灭霸", 100, 30, 20)
print(e01.name)
print(e01.hp)
print(e01.atk)
print(e01.defense)
