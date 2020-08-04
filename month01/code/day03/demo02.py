"""
    bool运算
        bool类型  真的True   假的False
            表达命题(一个带有判断性质的陈述句)
        运算符
            比较运算符
                相同==   不同!=
                (数值)大小 >  >=   <  <=
    练习：exercise01
"""

# 命题：我是个总统(输入的职业等于总统)
# result = input("请输入您的职业：") ==  "总统"
# print(result)# True  False

# 命题：您成年了(输入的年龄是大于18岁)
result = int(input("请输入您的年龄：")) >= 18
print(result)