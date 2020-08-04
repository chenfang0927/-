"""
    练习:使用装饰器，为旧功能增加新*功能(验证权限).
"""


# 验证权限
def verif_permissions(func):
    def wrapper(*args, **kwargs):
        print("验证权限")
        return func(*args, **kwargs)

    return wrapper

@verif_permissions
def insert(data):
    print("插入成功", data)
    return "ok"

@verif_permissions
def delete(id):
    print("删除成功", id)
    return "yes"


result = insert("10条数据")
print(result)
result = delete(id=1001)
print(result)
class nihao:
    def __init__(self, name):
        self.name=name
