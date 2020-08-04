"""
    基本的操作：增删改查
    分配职责：
        界面视图类View：负责处理界面逻辑，比如显示菜单，获取输入，显示结果等。
        逻辑控制类Controller：负责存储学生信息，处理业务逻辑。比如添加、删除等
        数据模型类Model：定义需要处理的数据类型。比如学生信息。 
"""
list01 = []
# 增加
list01.append(10)
list01.append(20)
# 修改
list01[0] = 100
# 查询
print(list01[0])
# 删除
list01.remove(10)
del list01[0]

