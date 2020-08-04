"""
    定义函数,根据年月日计算星期数
    结果：星期一
         星期二
         ....
         星期日
    步骤:定义函数(函数名称/参数/返回值)
         拼接年月日 --> 字符串   2020-6-17   %Y-%m-%d
         字符串 --> 时间元组
         时间元组  --> 星期
         星期 --> 星期一
"""
import time


def get_week(year, month, day):
    # str(year) + "-" + str(month) +"-" +str(day)
    # "%d-%d-%d"%(year, month, day)
    # f"{year}-{month}-{day}"
    str_time = f"{year}-{month}-{day}"
    tuple_time = time.strptime(str_time, "%Y-%m-%d")
    week_index = tuple_time[6]
    weeks = ("星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日")
    return weeks[week_index]


print(get_week(2020, 6, 17))
