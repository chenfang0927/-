"""
    练习1需求:
        在员工列表中,查找姓名是"刘岳浩"的员工
        在员工列表中,查找员工编号是1005的员工

    练习2需求:
        在员工列表中,查找所有员工的姓名
        在员工列表中,查找所有员工的编号和薪资

    步骤
        1. 定义函数,完成需求.
        2. 将变化点定义为函数
           将通用代码定义为函数
        3. 通用函数使用参数隔离变化点
        4. 将通用函数移动到IterableHelper类中
        5. 在当前模块中调用通用函数(lambda)
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


def find01():
    for emp in list_employee:
        if emp.name == "刘岳浩":
            return emp


def find02():
    for emp in list_employee:
        if emp.eid == 1005:
            return emp


def condition01(emp):
    return emp.name == "刘岳浩"


def condition02(emp):
    return emp.eid == 1005


def find(func):
    for emp in list_employee:
        # if emp.eid == 1005:
        # if condition02(emp):
        if func(emp):
            return emp


emp01 = IterableHelper.find_single(list_employee, lambda emp: emp.name == "刘岳浩")
print(emp01.__dict__)


# 2.
def select01():
    for emp in list_employee:
        yield emp.name

def select02():
    for emp in list_employee:
        yield (emp.eid, emp.money)


def handle01(emp):
    return emp.name

def handle02(emp):
    return  (emp.eid, emp.money)

def select(func):
    for emp in list_employee:
        # yield (emp.eid, emp.money)
        # yield handle02(emp)
        yield func(emp)

for item in IterableHelper.select(list_employee,lambda emp:(emp.eid, emp.money)):
    print(item)