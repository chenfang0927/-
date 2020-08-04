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

    三大特征
        封装：创建EmployeeManager、Programmer、Tester
        继承：创建Employee
        多态:EmployeeManager调用Employee
            Programmer、Tester重写Employee
            向EmployeeManager添加的是Programmer、Tester对象

    六大原则：
        开闭：增加新岗位的员工，EmployeeManager不改变
        单一职责：
            EmployeeManager操作所有员工
            Programmer负责实现程序员的薪资算法
            Tester负责实现测试员的薪资算法
        依赖倒置：
            EmployeeManager使用Employee
            不使用Programmer、Tester
        组合复用：
            EmployeeManager和员工薪资算法
        里氏替换：
            Programmer、Tester重写时先调用父类方法
        迪米特法则：
            Employee隔离EmployeeManager与Programmer、Tester的变化
"""

class EmployeeManager:
    def __init__(self):
        self.all_employee = []

    def add_employee(self, emp):
        self.all_employee.append(emp)

    def calculate_total_money(self):
        total_money = 0
        for emp in self.all_employee:
            total_money += emp.get_money()
        return total_money


class Employee:
    def get_money(self):
        pass


# --------------------------------

class Programmer(Employee):
    def __init__(self, base_salary, bonus):
        self.base_salary = base_salary
        self.bonus = bonus

    def get_money(self):
        super().get_money()
        return self.base_salary + self.bonus


class Tester(Employee):
    def __init__(self, base_salary, bug_count):
        self.base_salary = base_salary
        self.bug_count = bug_count

    def get_money(self):
        super().get_money()
        return self.base_salary + self.bug_count * 5


manager = EmployeeManager()
manager.add_employee(Programmer(8000, 100000))
manager.add_employee(Tester(5000, 500))
print(manager.calculate_total_money())
