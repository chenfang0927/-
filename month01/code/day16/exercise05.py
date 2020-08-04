"""
    使用yield代替迭代器EmployeeIterator
    迭代员工管理器
"""


class EmployeeManager:
    def __init__(self):
        self.all_employee = []

    def add_employee(self, emp):
        self.all_employee.append(emp)

    def __iter__(self):
        for item in self.all_employee:
            yield item

manager = EmployeeManager()
manager.add_employee("老王")
manager.add_employee("老李")
manager.add_employee("老孙")

for item in manager:
    print(item)
