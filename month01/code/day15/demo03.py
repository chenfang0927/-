"""
    总结 -- 包和模块
    1. 为什么要有模块和包?
          为了结构更加清晰
    2. 导入方法
        (1) import 路径.模块 as 别名
            别名.成员
        (2) from 路径.模块 import 成员
            直接使用成员
    3. 是否成功的唯一标准
            导入路径  + sys.path = 真实路径
            主模块:第一次执行的模块
            根目录:主模块所在文件夹
    4. 模块变量
"""


# 模块变量
import demo01
# -- 获取文档字符串
print(demo01.__doc__)

# -- 获取文件完整路径
# /home/tarena/2005/day15/demo03.py
print(demo01.__file__)

# -- 获取模块名称
print(demo01.__name__) # 被导入的模块是模块名demo01
print(__name__) # 只有当前模块是主模块时,才是"__main__"

if __name__ == '__main__':
    print("我是主模块")