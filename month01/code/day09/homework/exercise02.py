"""
    参照下列代码,定义函数,计算孩子身高.
    father_height = float(input("请输入父亲的身高（厘米）:"))
    mother_height = float(input("请输入母亲的身高（厘米）:"))
    son_height = (father_height + mother_height) * 0.54
    print("预测儿子的身高是:" + str(son_height) + "厘米")
"""
def calculate_son_height(father_height, mother_height):
    """
        计算孩子身高
    :param father_height: 父亲身高
    :param mother_height: 母亲身高
    :return: 孩子身高
    """
    return (father_height + mother_height) * 0.54

son_height = calculate_son_height(165, 180)
print(son_height)
