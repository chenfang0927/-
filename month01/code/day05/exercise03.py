# 练习:
# 读取疫情地区列表中间元素
# 读取新增人数列表前两个元素
# 读取现存人数列表后两个元素

# 修改疫情地区列表最后一个元素 "sc"
# 修改新增人数列表前两个元素　0
# 修改现存人数列表后两个元素  26 17
list_city = ["香港", "内蒙古", "四川"]
list_new_people = [6, 0, 0]
list_now_people = [51, 25, 16]

print(list_city[len(list_city) // 2])
print(list_new_people[:2])
print(list_now_people[1:])

list_city[-1] = "sc"
list_new_people[:2] = [0, 0]
list_now_people[1:] = [26, 17]