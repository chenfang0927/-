"""
    Controller
"""
class EmployeeController:
    def __init__(self):
        self.__list_employees = []
        self.__start_eid = 1001

    @property
    def list_employees(self):
        return self.__list_employees

    def add_employee(self, employee):
        employee.eid = self.__start_eid
        self.__start_eid += 1
        self.__list_employees.append(employee)

    def remove_employee(self, cid):
        for commodity in self.__list_employees:
            if commodity.cid == cid:
                self.__list_employees.remove(commodity)
                return True
        return False

    def update_employee(self, employee):
        for item in self.__list_employees:
            if item.eid == employee.eid:
                item.did = employee.did
                item.name = employee.name
                item.money = employee.money
                return True
        return False
