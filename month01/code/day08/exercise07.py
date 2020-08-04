"""
    练习:参照day03/exercise08案例,
    定义函数,计算智商等级。
"""


def calculate_iq(ma, ca):
    """
    根据心理年龄与实际年龄，打印智商等级
    :param ma: 心里年龄
    :param ca: 实际年龄
    :return: 智商等级
    """
    iq = ma / ca * 100
    if iq >= 140:
        return "天才"  # 退出函数
    if iq >= 120:
        return "超常"
    if iq >= 110:
        return "聪慧"
    if iq >= 90:
        return "正常"
    if iq >= 80:
        return "迟钝"
    return "低能"

result = calculate_iq(90,100)
print(result)