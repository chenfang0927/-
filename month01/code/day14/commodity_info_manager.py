"""
    参照student_info_manager.py完成商品管理系统
    1. 实现添加商品信息功能
        View -- 录入商品信息
        Controller -- 添加商品信息
    画出内存图
    2. 实现显示所有商品信息功能
    3. 实现删除商品信息功能
"""


class CommodityModel:
    def __init__(self, cid=0, name="", price=0.0):
        self.cid = cid
        self.name = name
        self.price = price


class CommodityView:
    def __init__(self):
        self.__controller = CommodityController()

    def __display_menu(self):
        print("1) 添加商品信息")
        print("2) 显示商品信息")
        print("3) 删除商品信息")

    def __select_menu(self):
        item = input("请输入选项：")
        if item == "1":
            self.__input_commodity()
        elif item == "2":
            self.__show_commodity()
        elif item == "3":
            self.__delete_commodity()

    def main(self):
        """
            入口函数
        """
        while True:
            self.__display_menu()
            self.__select_menu()

    def __input_commodity(self):
        commodity = CommodityModel()
        commodity.name = input("请输入商品名称：")
        commodity.price = float(input("请输入商品单价："))
        self.__controller.add_commodity(commodity)

    def __show_commodity(self):
        for commodity in self.__controller.list_commoditys:
            print("%s商品编号是%d,单价是%.2f" % (commodity.name, commodity.cid, commodity.price))

    def __delete_commodity(self):
        cid = int(input("请输入商品编号："))
        if self.__controller.remove_commodity(cid):
            print("删除成功")
        else:
            print("删除失败")


class CommodityController:
    def __init__(self):
        self.__list_commoditys = []
        self.__start_cid = 1001

    @property
    def list_commoditys(self):
        return self.__list_commoditys

    def add_commodity(self, commodity):
        commodity.cid = self.__start_cid
        self.__start_cid += 1
        self.__list_commoditys.append(commodity)

    def remove_commodity(self, cid):
        for commodity in self.__list_commoditys:
            if commodity.cid == cid:
                self.__list_commoditys.remove(commodity)
                return True
        return False


view = CommodityView()
view.main()
