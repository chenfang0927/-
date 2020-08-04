"""
    学生信息管理系统MVC
"""


# 2.数据模型
class StudentModel:
    """
        学生数据模型
        对具体学生信息进行抽象
    """

    def __init__(self, name="", age=0, score=0, sid=0):
        self.name = name
        self.age = age
        self.score = score
        # 学生编号：对数据进行唯一标识(全球唯一标识符)
        self.sid = sid  # 自增长1001   1002   1003

    # 对某个数据进行有效性验证
    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        if value < 0:
            value = 0
        elif value > 100:
            value = 100
        self.__score = value


# 3.界面逻辑
class StudentView:
    """
        学生视图：负责处理界面逻辑
    """

    def __init__(self):
        self.__controller = StudentController()

    def __display_menu(self):
        print("1) 添加学生信息")
        print("2) 显示学生信息")
        print("3) 删除学生信息")
        # ...

    def __select_menu(self):
        item = input("请输入选项：")
        if item == "1":
            # 先写调用,再快捷键生成定义函数代码
            # atl + 回车
            self.__input_student()
        elif item == "2":
            self.__show_students()
        elif item == "3":
            self.__delete_student()

    def main(self):
        """
            入口函数
        """
        while True:
            self.__display_menu()
            self.__select_menu()

    def __input_student(self):
        stu = StudentModel()
        stu.name = input("请输入学生姓名：")
        stu.age = int(input("请输入学生年龄："))
        stu.score = int(input("请输入学生成绩："))
        self.__controller.add_student(stu)

    def __show_students(self):
        for stu in self.__controller.list_students:
            print(f"{stu.name}的编号是{stu.sid}年龄是{stu.age}成绩是{stu.score}")

    def __delete_student(self):
        sid = int(input("请输入需要删除的学生编号："))
        if self.__controller.remove_student(sid):
            print("删除成功")
        else:
            print("删除失败")


# 4.业务逻辑
class StudentController:
    """
        学生控制器
            负责处理业务逻辑
    """

    def __init__(self):
        self.__list_students = []
        self.__start_sid = 1001

    # 只读属性
    @property
    def list_students(self):
        return self.__list_students

    def add_student(self, stu):
        """
            添加学生
        :param stu: 需要添加的学生对象
        """
        stu.sid = self.__start_sid
        self.__start_sid += 1
        self.__list_students.append(stu)

    def remove_student(self, sid):
        """
            删除学生
        :param sid: int类型的学生编号
        :return: bool类型,是否删除成功
        """
        for student in self.__list_students:
            if student.sid == sid:
                self.__list_students.remove(student)
                return True  # 删除成功
        return False  # 删除失败


# 1.入口
view = StudentView()
view.main()
