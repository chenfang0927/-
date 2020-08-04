"""
    特殊导入方式
       设置包的__init__.py文件
"""
# 方式1：import 包
# 设置：import package01.package02.module01
# import package01.package02 as p
#
# p.module01.func01()

# 方式2：from 包 import 包
# 设置：from package01.package02 import module01
# from package01 import package02
#
# package02.module01.func01()

# 方式3：from 包 import *
# 设置：__all__ = ["module01"]
from package01.package02 import *

module01.func01()
