class StudentModel:
    def __init__(self, name='', age=0, money=0, sid=0):
        self.name=name
        self.age=age
        self.money=money
        self.sid=sid
class StudentView:
    def __init__(self):
        self.data= StudentModel()
    def select_number(self):
        print('01)添加学生信息')
        print('02)查看学生信息')
    def import_number(self):
        import01=input('请输入')
        if import01 == 1:
            self.type_in_data()
    def main(self):
        """
            入口函数
        """
        while True:
            self.select_number()
            self.import_number()
    def type_in_data(self):
        stu=()
        stu.name= input('学生名字')
        stu.age=input('学生年纪')
        stu.money=input('请输入零花钱')
w01=StudentView()
w01.main()



# class Logic :
#     def __init__(self):
#         self.list01=[]
#     def append01(self):
#         self.list01.append()



