"""
    创建狗类
        数据：品种、爱称、年龄、体重
        行为：吃、叫
        实例化两个对象并调用其方法
"""
class Dog:
    def __init__(self, variety, name, age, weight=0.0):
        self.variety = variety
        self.name = name
        self.age = age
        # 生成参数的快捷键：alt + 回车
        self.weight = weight

    def eat(self):
        print(self.name, "吃东西")

    def yell(self):
        print(self.name, "大声喊叫")


d01 = Dog("金毛", "哮天犬", 2, 10)
d01.eat()
d01.yell()
