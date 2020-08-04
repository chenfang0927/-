# 练习1：将两个列表，合并为一个字典
# 		姓名列表["张无忌","赵敏","周芷若"]
# 		房间列表[101,102,103]

# 练习2：颠倒练习1字典键值
list_names = ["张无忌", "赵敏", "周芷若"]
list_rooms = [101, 102, 103]

# dict_infos = {}
# for i in range(len(list_names)):
#     # list_rooms[i] 作为key
#     # list_names[i] 作为value
#     dict_infos[list_rooms[i]] = list_names[i]
# print(dict_infos)

dict_infos = {list_rooms[i]: list_names[i]
              for i in range(len(list_names))
              }

result = {v: k for k, v in dict_infos.items()}

print(dict_infos)
print(result)
