"""
    练习:使用装饰器，为旧功能增加新功能(验证权限).
"""

# 验证权限
def verif_permissions(func):
    def wrapper(*args, **kwargs):
        print("验证权限")
        return func(*args, **kwargs)
    return wrapper

@verif_permissions
def insert():
    print("插入成功")

@verif_permissions
def delete():
    print("删除成功")

insert()
delete()
