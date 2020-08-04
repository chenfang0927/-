class StudentModel:
    def __init__(self, name='', age=0, score=0, sid=0):
        self.name=name
        self.age=age
        self.score=score
        self.sid=sid
class StudentView:


    def student_view(self):
        print('01)添加学生信息')
        print('02)查看学生信息')
        print('01)修改学生信息')
    def import_number(self):
        import_number=int(input('请输入数字'))
        if import_number == 1:
            self.import_message()

    def import_message(self):
        print('请输入学生信息')
        stu=StudentModel()
        stu.name=input('请输入学生名字')
        stu.age=input('请输入学生年龄')
        stu.score=input('请输入学生名字')
class StudentController:
    def __init__(self):
        self.list=[]
    def add(self):
        self.list.append(stu)








