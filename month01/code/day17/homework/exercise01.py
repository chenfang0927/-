class Skill:
    def __init__(self, name="", atk_rate=0.0, cost_sp=0, duration=0):
        self.name = name
        self.atk_rate = atk_rate
        self.cost_sp = cost_sp
        self.duration = duration


list_skills = [
    Skill("横扫千军", 1, 50, 5),
    Skill("九阳神功", 3, 150, 6),
    Skill("降龙十八掌", 3, 150, 5),
    Skill("一阳指", 1.2, 0, 2),
    Skill("乾坤大挪移", 3.2, 30, 2),
    Skill("打狗棍", 1.3, 0, 6),
]
"""
    -- 定义函数,查找攻击比例atk_rate大于1的所有技能
    -- 定义函数,查找消耗法力cost_sp为零并且持续时间duration大于5的所有技能
    -- 定义函数,查找名称为"九阳神功"的单个技能对象
    -- 定义函数,查找消耗法力最大的单个技能对象
    -- 定义函数,根据持续时间,对技能列表升序排列
    -- 定义函数,判断技能列表中是否存在名称相同的技能对象
              有true没有false(要求:自定义算法实现) 
"""

# -- yield 返回多个数据
def find_skills_by_atk_rate():
    for skill in list_skills:
        if skill.atk_rate > 1:
            yield skill


def find_skills_by_cost_sp_and_duration():
    for skill in list_skills:
        if skill.cost_sp == 0 and skill.duration > 5:
            yield skill

# -- return 返回单个数据
def find_skills_by_name():
    for skill in list_skills:
        if skill.name == "九阳神功":
            return skill


def get_max_skill_by_cost_sp():
    max_emp = list_skills[0]
    for i in range(1, len(list_skills)):
        if max_emp.cost_sp < list_skills[i].cost_sp:
            max_emp = list_skills[i]
    return max_emp


def is_repeating():
    for r in range(len(list_skills) - 1):
        for c in range(r + 1, len(list_skills)):
            if list_skills[r].name == list_skills[c].name:
                return True
    return False

# -- 没有返回
def ascending_order_by_duration():
    for r in range(len(list_skills) - 1):
        for c in range(r + 1, len(list_skills)):
            if list_skills[r].duration > list_skills[c].duration:
                list_skills[r], list_skills[c] = list_skills[c], list_skills[r]


if __name__ == '__main__':
    # 调用yield
    # -- 通过for执行生成器
    result = find_skills_by_atk_rate()
    for item in result:
        print(item.__dict__)

    # 生成器缺点1:只能用一次
    # for item in result:
    #     print(item.__dict__)

    # 生成器缺点2:不能使用索引/切片
    # result[-1]

    # -- 生成器 --> 容器
    # 缺点:将所有数据加载到内存中,占用可能过多.
    result = tuple(find_skills_by_cost_sp_and_duration())
    for item in result:
        print(item.__dict__)

    # 调用return
    skill = find_skills_by_name()
    print(skill.__dict__)

    emp = get_max_skill_by_cost_sp()
    print(emp.__dict__)

    print(is_repeating())

    # 调用无返回值
    ascending_order_by_duration()
    for item in list_skills:
        print(item.__dict__)
