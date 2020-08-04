"""
    练习:参照day02/exercise07案例,
         定义函数,计算治愈比例
"""


# definite_num = int(input("请输入确诊人数："))
# cure_num = int(input("请输入治愈人数："))
# print("治愈比例为：" + str(cure_num / definite_num * 100) + "%")

def calculate_cure_ratio(cure_num,definite_num):
    return cure_num / definite_num

# 测试
result = calculate_cure_ratio(10,50)
print(result)
