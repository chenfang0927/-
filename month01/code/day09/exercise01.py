"""
    定义函数,根据小时、分钟、秒,计算总秒数
    调用：提供小时、分钟、秒
    调用：提供分钟、秒
    调用：提供小时、秒
    调用：提供分钟
"""


def get_total_second(hour=0, minute=0, second=0):
    result = hour * 3600 + minute * 60 + second
    return result


# 传递全部参数 -- 位置
print(get_total_second(1, 2, 3))
# 传递部分参数 -- 关键字
print(get_total_second(minute=2, second=3))
# 按顺序 + 按名字(跳过minute)
print(get_total_second(1, second=3))
print(get_total_second(minute=2))
