"""
    1. 定义函数,将列表中奇数设置为1
    (选做)2. 定义函数,将列表中奇数删除
    测试数据:[3,7,5,6,7,8,9,13]

    结论:在列表中删除多个元素,倒序删除
"""


def change_odd_to_one(list_target):
    for i in range(len(list_target)): 
        if list_target[i] % 2:
            list_target[i] = 1

list01 = [3,7,5,6,7,8,9,13]
# change_odd_to_one(list01)
# print(list01)

# 问题1：漏删 -- 后面的元素向前挤,所以提前.
# 问题2：越界 -- 删除元素列表长度减少
# for i in range(len(list01)):
#     if list01[i] % 2:
#         del list01[i]

# 根据条件在容器中删除多个元素
# 倒序删除
def delete_all_by_odd(list_target):
    for i in range(len(list_target) - 1, -1, -1):
        if list_target[i] % 2:
            del list_target[i]

list01 = [3, 4, 5, 6, 7, 8, 9]
delete_all_by_odd(list01)
print(list01)
