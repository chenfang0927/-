"""
    创建员工管理器
        1. 记录多个员工（程序员、测试员....）
        2. 提供计算总薪资的方法.

    程序员：底薪 + 项目分红
    测试员: 底薪 + Bug数 × 5

    满足：
        开闭原则
    测试：
        创建员工管理器，存储多个员工对象。
        通过员工管理器，调用计算总薪资方法.
"""


class EmployeeManager:
    def __init__(self):
        # 建议将使用的数据私有化
        self.__all_employee = []

    def add_employee(self, emp):
        # 如果 emp  是一种 员工类型
        if isinstance(emp, Employee):
            self.__all_employee.append(emp)

    def calculate_total_money(self):
        total_money = 0
        for emp in self.__all_employee:
            total_money += emp.get_money()
        return total_money


class Employee:
    def __init__(self, base_salary):
        self.base_salary = base_salary

    def get_money(self):
        return self.base_salary

    # --------------------------------


class Programmer(Employee):
    def __init__(self, base_salary, bonus):
        super().__init__(base_salary)
        self.bonus = bonus

    def get_money(self):
        # 先通过爸爸的方法获取底薪
        base_salary = super().get_money()
        return base_salary + self.bonus


class Tester(Employee):
    def __init__(self, base_salary, bug_count):
        super().__init__(base_salary)
        self.bug_count = bug_count

    def get_money(self):
        return super().get_money() + self.bug_count * 5


manager = EmployeeManager()
manager.add_employee(Programmer(8000, 100000))
manager.add_employee(Tester(5000, 500))
manager.add_employee("二大爷")
print(manager.calculate_total_money())
