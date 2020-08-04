"""
    模块
    练习：
        将student_info_manager.py分解为4个模块
            -- bll.py --> 业务business 逻辑logic 层layer
                          存储Controller类
            -- usl.py --> 用户user 显示show 层layer
                          存储View类
            -- model.py --> 存储数据模型Model
            -- main.py  --> 存储入口代码
"""
# 建议设置项目根目录
#  -- 在day14文件夹上,右键选择"Mark Directory as"
#  -- 在选择"Sources Root"

# 导入方式1： 创建变量module01关联该模块
# 语法：
# import 模块
# 模块.成员
# 适合：面向过程的技术(全局变量、函数)

import module01

module01.func01()

# m01 = module01.MyClass()
# m01.func02()


# 导入方式2： 将该模块成员导入到当前作用域中
# 语法：from 文件名 import 内容
# 适合：面向对象的技术(类)
# from module01 import func01
from module01 import MyClass

# func01()

# m01 = MyClass()
# m01.func02()

# 导入方式3： 将该模块所有成员导入到当前作用域中
# 语法：from 文件名 import *
# 适合：面向对象的技术(类)
from module01 import *

func01()

m01 = MyClass()
m01.func02()
