"""
    练习1需求:
        在员工列表中,查找删除薪资15000以内的所有员工
        在员工列表中,查找删除部门编号是9005的所有员工

    练习2需求:
        在员工列表中,查找薪资最高的员工
        在员工列表中,查找员工编号最大的员工

    练习3需求:
        在员工列表中,根据薪资升序排列
        在员工列表中,根据员工编号升序排列

    步骤
        $1. 定义函数,完成需求.
        x2. 将变化点定义为函数
           将通用代码定义为函数
        x3. 通用函数使用参数隔离变化点
        $4. 在IterableHelper类中创建通用函数
        $5. 在当前模块中调用通用函数(lambda)
"""
from common.iterable_tools import IterableHelper


class EmployeeModel:
    def __init__(self, eid=0, did=0, name="", money=0.0):
        self.eid = eid
        self.did = did
        self.name = name
        self.money = money


list_employee = [
    EmployeeModel(1001, 9003, "林玉玲", 13000),
    EmployeeModel(1002, 9005, "王荆轲", 16000),
    EmployeeModel(1003, 9003, "刘岳浩", 11000),
    EmployeeModel(1004, 9007, "冯舜禹", 17000),
    EmployeeModel(1005, 9005, "曹海欧", 15000),
    EmployeeModel(1006, 9005, "魏鑫珑", 12000),
]

"""
def delete01():
    count = 0
    for i in range(len(list_employee)-1,-1,-1):
        if list_employee[i].money < 15000:
            del list_employee[i]
            count += 1
    return count

def delete02():
    count = 0
    for i in range(len(list_employee)-1,-1,-1):
        if list_employee[i].did == 9005:
            del list_employee[i]
            count += 1
    return count
"""

#                                                  参数是列表中的每个元素
# count = IterableHelper.delete_all(list_employee,lambda emp:emp.money < 15000)
# print(count)

count = IterableHelper.delete_all(list_employee, lambda item: item.did == 9005)
print(count)

# def get_max01():
#     max_value = list_employee[0]
#     for i in range(1, len(list_employee)):
#         if max_value.money < list_employee[i].money:
#             max_value = list_employee[i]
#     return max_value
#
# def get_max02():
#     max_value = list_employee[0]
#     for i in range(1, len(list_employee)):
#         if max_value.eid < list_employee[i].eid:
#             max_value = list_employee[i]
#     return max_value

max = IterableHelper.get_max(list_employee, lambda item: item.money)
print(max.__dict__)

max  IterableHelper.get_max(list_employee, lambda item: item.eid)
print(max.__dict__)

# 在列表中根据薪资升序排列
IterableHelper.ascending_order(list_employee, lambda emp: emp.money)
IterableHelper.ascending_order(list_employee, lambda emp: emp.eid)
print(list_employee)