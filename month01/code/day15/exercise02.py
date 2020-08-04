"""
    定义函数,获取成绩
    如果成绩输入有误,循环录入,直到正确为止.
"""
"""
    练习:对员工管理器进行异常处理
"""
def get_score():
    while True:
        try:
            score = float(input("请输入成绩:"))
            return score # 退出函数
        except:
            print("成绩输入有误!")

print(get_score()) # 有效的成绩