"""
    函数返回结果:
        return 数据  -- 单个
        yield 数据   -- 多个
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

# 1. 定义函数,在list_employee中查找薪资大于等于15000的所有员工
def find_employees_gt_15k():
    for emp in list_employee:
        if emp.money >= 15000:
            yield emp
for item in find_employees_gt_15k():
    print(item.__dict__)

# 2. 定义函数,在list_employee中查找员工编号为1005的员工
def find_employee_at_eid():
    for emp in list_employee:
        if emp.eid == 1005:
            return emp
employee = find_employee_at_eid()
print(employee.__dict__)

# 3. 定义函数,在list_employee中查找所有员工的姓名
def select_names_by_employee():
    for emp in list_employee:
        yield emp.name

for name in select_names_by_employee():
    print(name)

# 4. 定义函数,在list_employee中查找薪资最高的员工
def get_max_employee_by_money():
    max_emp = list_employee[0]
    for i in range(1,len(list_employee)):
        if max_emp.money  < list_employee[i].money:
            max_emp = list_employee[i]
    return max_emp

emp = get_max_employee_by_money()
print(emp.__dict__)
