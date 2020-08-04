# 导入方式1: 通过变量关联对方模块
# import usl
#
# view = usl.EmployeeView()
# view.main()

# 导入方式2:将对方模块成员导入到我方作用域中
from usl import EmployeeView

# 如果当前模块是主模块,则执行入口代码
# (当前模块被导入,不执行入口代码)
if __name__ == '__main__':
    view = EmployeeView()
    view.main()


# 导入方式3:
# from usl import *
#
# view = EmployeeView()
# view.main()