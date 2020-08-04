"""
    exercise06.py
    练习:使用lambda代替condtion0x函数
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


# def condition01(emp):
#     return emp.money >= 15000
#
# def condition02(emp):
#     return emp.did == 9005

# 通用
def find(func):
    for emp in list_employee:
        if func(emp):
            yield emp


# 变化 + 通用
for item in find(lambda emp: emp.did == 9005):
    print(item.__dict__)

for item in find(lambda emp: emp.money >= 15000):
    print(item.__dict__)

for item in IterableHelper.find_all(list_employee, lambda emp: emp.money >= 15000):
    print(item.__dict__)
