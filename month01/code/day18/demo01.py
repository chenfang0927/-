"""
    内置高阶函数
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

# 1. map : 映射
# map(func,iterable) -> 生成器
for item in map(lambda item: item.name, list_employee):
    print(item)

# for item in IterableHelper.select(list_employee,lambda item:item.name):
#     print(item)

# 2.filter:过滤
# filter(func,iterable) -> 生成器
for item in filter(lambda emp: emp.money > 15000, list_employee):
    print(item.__dict__)

# for item in IterableHelper.find_all(list_employee,lambda emp:emp.money > 15000):
#     print(item.__dict__)

# 3.max  4.min : 最大最小
#  极值 = max(容器, key=函数)
max_emp = max(list_employee, key=lambda item: item.money)
print(max_emp.__dict__)

# max_emp =IterableHelper.get_max(list_employee,lambda item:item.money)
# print(max_emp.__dict__)

# 5. 排序
# -- 升序
# 　排序结果 = sorted(容器, key=函数)
result = sorted(list_employee, key=lambda e: e.money)
print(result)

# IterableHelper.ascending_order(list_employee,lambda e:e.money)
# print(list_employee)

# -- 降序
# 　排序结果 = sorted(容器, key=函数, reverse=True)
result = sorted(list_employee, key=lambda e: e.money, reverse=True)
print(result)
