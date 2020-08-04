# 练习:
# 打印疫情地区列表所有元素(一行一个)
# 倒序打印新增人数列表(一行一个)
# 将现存人数列表所有元素设置为0

# 删除疫情地区列表中间元素
# 删除新增人数列表前两个元素
# 删除现存人数列表后两个元素
list_city = ["香港", "内蒙古", "四川"]
list_new_people = [6, 0, 0]
list_now_people = [51, 25, 16]

for city in list_city:
    print(city)

for i in range(len(list_new_people) - 1, -1, -1):
    print(list_new_people[i])

for i in range(len(list_now_people)):
    list_now_people[i] = 0

del list_city[len(list_city) // 2]
del list_new_people[:2]
del list_now_people[-2:]
