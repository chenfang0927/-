"""
    自定义对象的列表,如果需要使用内置函数就需要重写比较运算符.
    重写比较运算符
        __eq__  定义相同依据
        __lt__  定义大小依据
"""
class Employee:
    def __init__(self, eid=0, did=0, name="", money=0):
        self.eid = eid
        self.did = did
        self.name = name
        self.money = money

    # 员工对象的相同依据
    def __eq__(self, other):
        return self.eid == other.eid

    # 员工对象的大小依据
    def __lt__(self, other):
        return self.money < other.money


e01 = Employee(1001, 9002, "师父", 60000)
e02 = Employee(1001, 9002, "师父", 60000)

# 内部调用__eq__
# 比较内容是否相同
print(e01 == e02) # true  编号相同
# 比较地址是否相同
print(e01 is e02) # false 两个员工对象

# 员工列表
list_employees = [
    Employee(1001, 9002, "师父", 60000),
    Employee(1001, 9002, "师父", 60000),
    Employee(1001, 9002, "师父", 60000),
    Employee(1002, 9001, "孙悟空", 50000),
    Employee(1003, 9002, "猪八戒", 20000),
    Employee(1004, 9001, "沙僧", 30000),
    Employee(1005, 9001, "小白龙", 15000),
]
print(list_employees.count(Employee(1001)))
print(list_employees.index(Employee(1005)))
# 内部在循环调用员工的__lt__方法
list_employees.sort()
print(list_employees) # 重写__repr__

