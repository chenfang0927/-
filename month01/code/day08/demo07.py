"""
    作用域
          局部作用域：函数内部有效
          全局作用域：整个文件有效
          小范围(一个函数)使用局部变量
          大范围(多个函数)使用全局变量
"""
# ------------全局作用域：整个文件有效------------
b = 200
# ------------函数------------
def func01():
    # 局部作用域：函数内部有效
    a = 100
    print(a)

def func02():
    # 局部可以访问全局
    print(b)
# ------------调用(入口)------------
func01()
func02()
print(b)

