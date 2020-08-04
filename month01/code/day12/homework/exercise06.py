"""
    删除列表中所有重复的元素(重复元素只保留一个)。
    输入：[6,2,3,4,5,6,7,3,2,4,8]
"""

def remove_duplicate(list_target):
    # 取出数据:从最后一个开始,到到第二个结束.
    for r in range(len(list_target) - 1, 0, -1):
        # 判断重复:从第一个开始,到取出的数据前一项
        for c in range(r):
            if list_target[r] == list_target[c]:
                del list_target[r]
                break


list01 = [6, 2, 3, 4, 5, 6, 7, 3, 2, 4, 8]
remove_duplicate(list01)
print(list01)
