"""
    对时间的处理
    https://www.runoob.com/python3/python3-date-time.html
"""
import time

# 1. 人类时间
# 时间元组: 年/月/日/时/分/秒/星期/一年的第几天/夏令时
print(time.localtime())
# 2. 计算机时间
# 时间戳: 从1970年1月1日 0时0分0秒到现在经过的秒数
print(time.time())  # 1592377581.6000147
# 3. 时间戳 --> 时间元组
tuple_time = time.localtime(1592377581.6000147)
# 4. 时间元组 --> 时间戳
print(time.mktime(tuple_time))
# 5. 时间元组 --> 字符串
# 语法:字符串 = time.strftime(格式,时间元组)
# 20/06/17 15:06:21
print(time.strftime("%y/%m/%d %H:%M:%S",tuple_time))
# 2020/06/17 15:06:21
print(time.strftime("%Y/%m/%d %H:%M:%S",tuple_time))
# 6. 字符串 --> 时间元组
# 语法:时间元组 = time.strptime(时间字符串,格式)
print(time.strptime("2020/06/17 15:06:21","%Y/%m/%d %H:%M:%S"))