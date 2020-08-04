"""
    MVC 控制与显示分离
        控制Controller：负责业务逻辑
        显示View：负责界面逻辑
        模型Model：封装数据
        入口main：项目启动
"""


class EmployeeModel:
    def __init__(self, eid=0, did=0, name="", money=0.0):
        self.eid = eid
        self.did = did
        self.name = name
        self.money = money


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

    def __input_employee(self):
        employee = EmployeeModel()
        employee.name = input("请输入员工姓名：")
        employee.did = int(input("请输入部门编号："))
        employee.money = int(input("请输入员工薪资："))
        # self.__controller.add_employee(employee)

    def __show_employee(self):
        for employee in self.__controller.list_employees:
            print("%s的员工编号是%d,部门编号是%d,工资是%.2f" % (employee.name, employee.eid, employee.did, employee.money))

    def __delete_employee(self):
        cid = int(input("请输入商品编号："))
        if self.__controller.remove_employee(cid):
            print("删除成功")
        else:
            print("删除失败")

    def __modify_employee(self):
        employee = EmployeeModel()
        employee.eid = int(input("请输入需要修改的员工编号："))
        employee.name = input("请输入需要修改的员工姓名：")
        employee.did = int(input("请输入需要修改的部门编号："))
        employee.money = int(input("请输入需要修改的员工薪资："))

        if self.__controller.update_employee(employee):
            print("修改成功")
        else:
            print("修改失败")


class EmployeeController:
    def __init__(self):
        self.__list_employees = []
        self.__start_eid = 1001

    @property
    def list_employees(self):
        return self.__list_employees

    # typing 类型标注
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


view = EmployeeView()
view.main()
