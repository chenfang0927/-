"""
    将生成器函数,改写为生成器表达式
"""


class EmployeeModel:
    def __init__(self, eid=0, did=0, name="", money=0.0):
        self.eid = eid
        self.did = did
        self.name = name
        self.money = money


list_employee = [
    EmployeeModel(1001, 9003, "林玉玲", 13000),
    EmployeeModel(1002, 9003, "王荆轲", 16000),
    EmployeeModel(1003, 9003, "刘岳浩", 11000),
    EmployeeModel(1004, 9003, "冯舜禹", 17000),
    EmployeeModel(1005, 9003, "曹海欧", 15000),
    EmployeeModel(1006, 9003, "魏鑫珑", 12000),
]

# 1. 在list_employee中查找薪资大于等于15000的所有员工
employees_gt_15k = (emp for emp in list_employee if emp.money >= 15000)
for item in employees_gt_15k:
    print(item.__dict__)

# 3. 在list_employee中查找所有员工的姓名
names_by_employee = (emp.name for emp in list_employee)
for name in names_by_employee:
    print(name)
