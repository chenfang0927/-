# from common.list_helper import ListHelper

# 在__init__.py中配置
# __all__ = ["list_helper"]

# 导入模块是否成功的唯一标准：
# 导入路径 + sys.path = 实际路径

import sys

sys.path.append("/home/tarena/month01/code/day15/my_projcet")
print(sys.path)

from common import  *

class SkillDeployer:
    def func02(self):
        print("func02执行了")

# ListHelper.func03()
list_helper.ListHelper.func03()

