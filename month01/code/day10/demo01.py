"""
    实例成员:对象.成员名
        实例变量
            对象.变量名
        实例方法
            对象.方法()
    练习:exercise01
"""

class Wife:
    def __init__(self, name):
        # 局部变量：存储在栈帧中
        a = 10
        # 实例变量：存储在对象中
        self.name = name

    def work(self):
        # print(a) 不能访问其他方法的局部变量
        # 可以访问自身对象的实例变量
        print(self.name + "在工作")


w01 = Wife("双儿")
w02 = Wife("建宁")
print(w01.name)
print(w02.name)
# 存储了对象所有的实例变量
print(w01.__dict__)  # {'name': '双儿'}
w01.work()  # 自动传递对象地址 work(w01)
w02.work()  # 自动传递对象地址 work(w01)
Wife.work(w01)  # 手动传递对象地址 类名.方法名(对象地址)

"""
class Wife:
    pass

w01 = Wife()
w01.name = "建宁"  # 创建实例变量
w01.name = "双儿"  # 修改实例变量
print(w01.name)

dict01 = {}
dict01["a"] = "A"
dict01["a"] = "B"
print(dict01["a"])  # B
"""

# class Wife:
#     def set_name(self,name):
#         # 建议创建实例变量在__init__中
#         self.name = name
#
# w01 = Wife()
# w01.set_name("双儿")
# print(w01.name) #
