"""
    迭代器 --> yield
    练习:exercise05,06
"""
class SkillManager:
    def __init__(self):
        self.__skills = []

    def add_skill(self, skill):
        self.__skills.append(skill)

    # def __iter__(self):
    #     print("准备")
    #     yield self.__skills[0]
    #
    #     print("准备")
    #     yield self.__skills[1]
    #
    #     print("准备")
    #     yield self.__skills[2]
    def __iter__(self):
        for skill in self.__skills:
            print("准备")
            yield skill

        # yield 生成迭代器代码的大致规则:
        # 1. 将yield之前的代码定义到__next__方法中
        # 2. 将yield之后的数据作为__next__方法返回值

manager = SkillManager()
manager.add_skill("降龙十八掌")
manager.add_skill("六脉神剑")
manager.add_skill("乾坤大挪移")

# 迭代自定义对象
for skill in manager:
    print(skill)

# iterator = manager.__iter__()
# while True:
#     try:
#         item = iterator.__next__()
#         print(item)  # 降龙十八掌
#     except StopIteration:
#         break

# 现象:调用__iter__方法,但是不执行
#     调用__next__方法,执行__iter__方法
#     执行到yield返回,当再次调用__next__方法继续执行__iter__方法
