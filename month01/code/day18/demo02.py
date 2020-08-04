"""
    函数作用域
        - 外部嵌套作用域 语法
         # 内部函数可以访问外部函数变量
         # 如果修改外部函数变量,必须通过nonlocal声明
"""
# 外部函数
def func01():
    # 局部变量：对文件而言
    # 外部嵌套变量：对func02而言
    a = 10

    # 内部函数
    def func02():
        # 内部函数可以访问外部函数变量
        print(a)

    func02()

# 调用外部函数(内部函数不执行)
func01()


# 外部函数
def func03():
    a = 10

    # 内部函数
    def func04():
        # 如果修改外部函数变量,必须通过nonlocal声明
        nonlocal a
        a = 20

    func04()
    print(a)# ?

func03()

