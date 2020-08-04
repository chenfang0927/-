"""
    1. 玩家攻击敌人,敌人受伤(播放动画)
    2. 玩家(攻击力)攻击敌人(血量),
        敌人受伤(播放动画,血量减少)
    3. 敌人(攻击力)还能攻击玩家(血量),
        玩家受伤(碎屏,血量减少)
"""

# 1. 类与类调用
# class Player:
#     def attack(self, emeny):
#         emeny.damage()
#
# class Enemy:
#     def damage(self):
#         print("播放受伤动画")
#
# p01 = Player()
# e01 = Enemy()
# p01.attack(e01)

# 2. 调用时增加数据   玩家(攻击力)  -攻击力->  敌人(血量)
"""
class Player:
    def __init__(self, atk=0):
        self.atk = atk
    def attack(self, emeny):
        print("玩家攻击敌人")
        emeny.damage(self.atk)

class Enemy:
    def __init__(self, hp):
        self.hp = hp
    def damage(self, value):
        print("播放受伤动画")
        self.hp -= value
        print("敌人血量是", self.hp)


p01 = Player(50)
e01 = Enemy(100)
p01.attack(e01)
p01.attack(e01)
"""


# 3.
class Player:
    def __init__(self, hp, atk):
        self.hp = hp
        self.atk = atk

    def attack(self, emeny):
        print("玩家攻击敌人")
        emeny.damage(self.atk)

    def damage(self, value):
        print("碎屏")
        self.hp -= value
        print("敌人血量是", self.hp)


class Enemy:
    def __init__(self, hp, atk):
        self.hp = hp
        self.atk = atk

    def damage(self, value):
        print("播放受伤动画")
        self.hp -= value
        print("敌人血量是", self.hp)

    def attack(self, player):
        print("敌人攻击玩家")
        player.damage(self.atk)


p01 = Player(500, 50)
e01 = Enemy(100, 10)
p01.attack(e01)
e01.attack(p01)
