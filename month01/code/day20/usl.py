from bll import Control
from model import CommodityModel
CLASS CommodityView:
    def __init__(self):
        self.__commodity = Control()

    def commodity_view(self):
        print('1)添加商品信息')
        print('2)查看商品信息')
        print('3修改商品信息')
        print('4)删除商品信息')

    def input_number(self):
        number = int(input('请输入'))
        if number == 1:
            self.input_information()
        if number == 2:
            self.look_information()
        if number == 3:
            self.modify_information()
        if number == 4:
            pass

    def mian(self):
        while True:
            self.commodity_view()
            self.input_number()

    def input_information(self):
        inf = CommodityModel()
        inf.cid = input('请输入商品编号')
        inf.name = input('请输入商品名称')
        inf.price = input('请输入商品单价')
        self.__commodity.control_xinxi(inf)

    def look_information(self):
        for stu in self.__commodity.list01:
            print(f'商品编号是{stu.cid}商品名称是{stu.name}商品单价是{stu.price}序号是{stu.sid}')

    def modify_information(self):
        print_number = int(input('请输入序列号'))
        if self.__commodity.remmodify(print_number):
            print('删除成功')
        else:
            print('删除失败')
