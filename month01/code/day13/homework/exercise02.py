"""
    根据下列使用方式,重写员工类相关函数.
"""

class Skill:
    def __init__(self, name="", atk_rate=0.0, cost_sp=0, duration=0):
        self.name = name
        self.atk_rate = atk_rate
        self.cost_sp = cost_sp
        self.duration = duration

    # 判断相同的依据
    def __eq__(self, other):
        return self.name == other.name

    # 判断大小的依据
    def __lt__(self, other):
        return self.atk_rate < other.atk_rate

# 员工列表
list_skills = [
    Skill("乾坤大挪移",3,100,60),
    Skill("九阳神功",2.5,80,50),
    Skill("乾坤大挪移", 3, 100, 60),
    Skill("六脉神剑",2,50,3)
]

# 在技能列表中查找的Skill("九阳神功")索引
print(list_skills.index(Skill("九阳神功")))
# 在技能列表中查找的Skill("乾坤大挪移")的数量
print(list_skills.count(Skill("乾坤大挪移")))
# 查攻击力比例atk_rate最小的技能
print(min(list_skills).__dict__)
# 根据攻击力比例atk_rate排序
list_skills.sort()
for item in list_skills:
    print(item.__dict__)
