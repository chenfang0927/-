"""
    列表适合：存储单一维度的信息
        疫情地区列表（地区）
    字典适合：存储多个维度的信息
        疫情信息(地区、新增人数、现有人数..)

    练习1: 创建三个字典, 存储前三个地区疫情信息
           (地区, 新增, 现有, 累计, 治愈)
    练习2: 为以上三个字典, 添加si亡信息
    练习3: 删除第一个字典的新增人数,
    练习4: 将第二个字典的新增人数设置为0,
    练习5: 打印第三个字典信息:
    格式: xx新增xx, 现有xx, 累计xx, 治愈xx, si亡xx
"""
# 1.
dict_epidemic_of_Hong_Kong = {
    "region": "香港", "now": 6,
    "current": 53, "total": 1099, "cure": 1042}

dict_epidemic_of_guangzhou = {
    "region": "广州", "now": 25,
    "current": 1, "total": 996, "cure": 990}

dict_epidemic_of_neimeng = {
    "region": "内蒙古", "now": 0,
    "current": 21, "total": 235, "cure": 213}

# 2.
dict_epidemic_of_Hong_Kong["death"] = 4
dict_epidemic_of_guangzhou["death"] = 1
dict_epidemic_of_neimeng["death"] = 3

# 3.
del dict_epidemic_of_Hong_Kong["now"]

# 4.
dict_epidemic_of_guangzhou["now"] = 0

# 5.
print("%s新增%d, 现有%d, 累计%d, 治愈%d, si亡%d" % (
    dict_epidemic_of_neimeng["region"],
    dict_epidemic_of_neimeng["now"],
    dict_epidemic_of_neimeng["current"],
    dict_epidemic_of_neimeng["total"],
    dict_epidemic_of_neimeng["cure"],
    dict_epidemic_of_neimeng["death"],)
)
