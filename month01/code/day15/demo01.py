"""
    Python程序结构

包(文件夹)
    模块(文件)
        类
            函数
                语句

    导入模块是否成功的唯一标准：
         导入路径 + sys.path = 实际路径

    import sys
    sys.path.append("/home/tarena/month01/code/day15/my_projcet")
    print(sys.path)
"""
# # 方法1
# # import 路径.模块名
# import package01.package02.module01 as m
#
# m.func01()
#
# # 方法2
# from 路径.模块名 import 成员
from package01.package02.module01 import func01

func01()

# # 方法3
# # from 路径.模块名 import *
# from package01.package02.module01 import *
#
# func01()
