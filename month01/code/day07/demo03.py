"""
    列表推导式 嵌套
    练习:exercise04
"""
list01 = ["香蕉", "苹果", "哈密瓜"]
list02 = ["雪碧", "可乐", "牛奶", "绿茶"]
# list_result = []
# for r in list01:
#     for c in list02:
#         list_result.append(r + c)
# print(list_result)
list_result = [r + c for r in list01 for c in list02]
