"""
    练习:参照day03/exercise06案例,
     定义函数,根据课程编号计算课程名称。
"""

def get_course_name(number):
    """

    :param number:
    :return:
    """
    list_course_name = [
        "Python语言核心编程",
        "Python高级软件技术",
        "Web全栈",
        "网络爬虫",
        "数据分析、人工智能"
    ]
    # if 1<= number <= len(list_course_name):
    #     return list_course_name[number - 1]
    # else:
    #     return "课程不存在"

    # 如果满足条件,不会执行return "课程不存在"
    if 1 <= number <= len(list_course_name):
        return list_course_name[number - 1]
    return "课程不存在"


name = get_course_name(2)
print(name)  # Python语言核心编程
