"""
    定义函数, 在一行中打印一维列表各元素
    例如：
      list01 = [2,3,4,56]
    	list02 = ["a","b","c","d"]

    	2 3 4 56
    	a b c d
"""


# list01 = [2,3,4,56]
# for item in list01:
#     print(item,end = " ")
#
# list02 = ["a","b","c","d"]
# for item in list02:
#     print(item,end = " ")

# 将共性行为提取到函数中,将数据的变化作为参数。
def print_single_list(list_target):
    """
        在终端中打印列表的元素
    :param list_target: 目标列表
    """
    for item in list_target:
        print(item, end=" ")


list01 = [2, 3, 4, 56]
print_single_list(list01)


list02 = ["a", "b", "c", "d"]
print_single_list(list01)
