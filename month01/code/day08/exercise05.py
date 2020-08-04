"""
    练习:参照day02/exercise08案例,
         定义函数,计算重量。
"""

def calculate_weight(amount):
    """
        计算重量
    :param amount: 总两数
    :return: 元组类型,斤两
    """
    jin = amount // 16
    liang = amount % 16
    return jin, liang

result = calculate_weight(100)
print(type(result))
print(result)
