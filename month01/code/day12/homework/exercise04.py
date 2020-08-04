"""
    -- 玩家攻击(攻击力)多个敌人，敌人受伤(减血)后可能si亡(播放si亡动画)
        区别:敌人与敌人列表
"""


class Player:
    def __init__(self, atk=50):
        self.atk = atk

    def group_attack(self, list_target):
        print("玩家发起群体攻击")
        for target in list_target:
            target.damage(self.atk)


class Enemy:
    def __init__(self, hp=100):
        self.hp = hp

    def damage(self, value):
        print("(⊙o⊙)…敌人受伤啦")
        self.hp -= value
        if self.hp <= 0:
            print("播放死亡动画")


p01 = Player()
list_enemys = [Enemy(50), Enemy(80), Enemy(100)]
p01.group_attack(list_enemys)
p01.group_attack(list_enemys)
