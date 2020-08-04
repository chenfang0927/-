"""
    5.  使用面向对象思想,描述下列情景.
        张无忌使用乾坤大挪移(眩晕+伤害)攻击
        张无忌使用九阳神功(伤害+击飞)攻击
        还可能使用其他技能攻击

        封装：分而治之
            人    乾坤大挪移    九阳神功
        继承：抽象  统一   隔离
        多态(重写):
            彰显子类的个性
"""

class Person:
    def __init__(self, name=""):
        self.name = name

    def attack(self, skill):
        print(self.name,"在攻击")
        # 1. 运行前 调用父(技能类)
        skill.deploy()

class Skill:
    def deploy(self):
        pass

class QianKunDaNuoYi(Skill):
    # 2. 子重写
    def deploy(self):
        print("眩晕")
        print("伤害")

class JiuYangShenGong(Skill):
    def deploy(self):
        print("眩晕")
        print("击飞")

zwj = Person("张无忌")
# 3. 创建子
qkdny = QianKunDaNuoYi()
zwj.attack(qkdny)


# class ...(Skill):
#     def deploy(self):
#         ....
