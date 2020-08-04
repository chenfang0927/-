"""
    在终端中录入一个疫情确诊人数,再录入一个治愈人数,
    打印治愈比例
    格式：治愈比例为xx%
"""
definite_num = int(input("请输入确诊人数："))
cure_num = int(input("请输入治愈人数："))
print("治愈比例为：" + str(cure_num / definite_num * 100) + "%")
