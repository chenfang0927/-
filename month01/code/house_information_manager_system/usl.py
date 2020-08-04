from bll import HouseManagerController


class HouseManagerView:
    """
       责处理界面逻辑(输入/输出/界面跳转)
    """

    def __init__(self):
        self.__controller = HouseManagerController()

    def main(self):
        while True:
            self.__display_menu()
            self.__select_menu()

    def __display_menu(self):
        print("1) 显示所有房源")
        print("2) zuida  ")
        print("3)  ")

    def __select_menu(self):
        item = input("请输入选项:")
        if item == "1":
            self.__display_houses()
        elif item == "2":
            self.__most_expensive_house()
        elif item == "3":
            pass

    def __display_houses(self):
        for house in self.__controller.list_houses:
            # 定义打印房源的格式....
            print(house.__dict__)

    def __most_expensive_house(self):

        for house01 in self.__controller.list_houses:
            print(max(house01.id))
