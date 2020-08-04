"""
    View
"""
from bll import EmployeeController
from model import EmployeeModel


class EmployeeView:
    def __init__(self):
        self.__controller = EmployeeController()

    def __display_menu(self):
        print("1) 添加员工信息")
        print("2) 显示员工信息")
        print("3) 删除员工信息")
        print("4) 修改员工信息")

    def __select_menu(self):
        item = input("请输入选项：")
        if item == "1":
            self.__input_employee()
        elif item == "2":
            self.__show_employee()
        elif item == "3":
            self.__delete_employee()
        elif item == "4":
            self.__modify_employee()

    def main(self):
        """
            入口函数
        """
        while True:
            self.__display_menu()
            self.__select_menu()

    def get_number(self,message):
        while True:
            try:
                number = int(input(message))
                return number  # 退出函数
            except:
                print("输入有误!")

    def __input_employee(self):
        employee = EmployeeModel()
        employee.name = input("请输入员工姓名：")
        # employee.did = int(input("请输入部门编号："))
        employee.did = self.get_number("请输入部门编号：")
        employee.money = self.get_number("请输入员工薪资：")
        self.__controller.add_employee(employee)

    def __show_employee(self):
        for employee in self.__controller.list_employees:
            print("%s的员工编号是%d,部门编号是%d,工资是%.2f" % (employee.name, employee.eid, employee.did, employee.money))

    def __delete_employee(self):
        cid = self.get_number("请输入商品编号：")
        if self.__controller.remove_employee(cid):
            print("删除成功")
        else:
            print("删除失败")

    def __modify_employee(self):
        employee = EmployeeModel()
        employee.eid = self.get_number("请输入需要修改的员工编号：")
        employee.name = input("请输入需要修改的员工姓名：")
        employee.did = self.get_number("请输入需要修改的部门编号：")
        employee.money = self.get_number("请输入需要修改的员工薪资：")

        if self.__controller.update_employee(employee):
            print("修改成功")
        else:
            print("修改失败")