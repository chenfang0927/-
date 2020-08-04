"""
    情景：手雷爆炸，可能伤害敌人或者玩家的生命。
    变化：还可能伤害房子、树、鸭子....
    要求：增加新事物，不影响手雷.
    体会：开闭原则
        增加新攻击目标,手雷不改变.
    画出架构设计图
"""


# ----------架构师-----------
class Grenade:
    def explode(self, target):
        print("手雷爆炸")
        target.damage()


class AttackTarget:
    def damage(self):
        pass


# ----------程序员-----------
class Enemy(AttackTarget):

    def damage(self):
        print("敌人受伤")

class Player(AttackTarget):

    def damage(self):
        print("玩家受伤")

g01 = Grenade()
e01 = Enemy()
p01 = Player()
g01.explode(p01)
