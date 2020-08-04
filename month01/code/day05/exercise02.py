"""
https://voice.baidu.com/act/newpneumonia/newpneumonia/?from=osari_pc_3
    练习1:
        创建疫情地区列表
        创建新增人数列表
        创建现有人数列表
        要求：存储３个元素
    练习2:
        为以上三个列表追加第四个元素
        为以上三个列表在第二个元素上插入广东信息　
"""
list_city = ["香港", "内蒙古", "四川"]
list_new_people = [6, 0, 0]
list_now_people = [51, 25, 16]

list_city.append("台湾")
list_new_people.append(0)
list_now_people.append(9)

list_city.insert(1, "广东")
list_new_people.insert(1, 0)
list_now_people.insert(1, 6)
