"""
使用列表推导式生成1--50之间能被3或者5整除的数字
使用列表推导式生成5 -- 100之间的数字平方
"""
list_number = [number for number in range(1,51)
               if number % 3 == 0 or
               number % 5 == 0]

list_number = [number ** 2 for number
               in range(5,101)]