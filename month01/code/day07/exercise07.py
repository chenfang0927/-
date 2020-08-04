dict_travel_info = {
    "北京": {
        "景区": ["长城", "故宫"],
        "美食": ["烤鸭", "豆汁胶圈", "炸酱面"]
    },
    "四川": {
        "景区": ["九寨沟", "峨眉山"],
        "美食": ["火锅", "兔头"]
    }
}

# 1)打印所有城市（一行一个）
for city in dict_travel_info:
    print(city)
# 2)打印北京所有美食（一行一个）
for food in dict_travel_info["北京"]["美食"]:
    print(food)
# 3)打印四川所有景区（一行一个）
for scenic_area in dict_travel_info["四川"]["景区"]:
    print(scenic_area)
# 4)打印所有城市的所有景区（一行一个）
for city in dict_travel_info:
    for scenic_area in dict_travel_info[city]["景区"]:
        print(scenic_area)
# 5)为北京添加景区："天坛"
dict_travel_info["北京"]["景区"].append("天坛")
# 6)删除四川美食：兔头
dict_travel_info["四川"]["美食"].remove("兔头")
