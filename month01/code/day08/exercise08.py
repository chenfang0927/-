"""
    练习:参照day04/homework/exercise03案例,
    定义函数,计算折扣。
"""


# def calculate_discount(account_type, money):
#     if account_type == "vip":
#         if money < 500:
#             return 0.85
#         else:
#             return 0.8
#     else:
#         if money > 800:
#             return 0.9
#         else:
#             return 1

def calculate_discount(account_type, money):
    """

    :param account_type:
    :param money:
    :return:
    """
    if account_type == "vip":
        return 0.85 if money < 500 else 0.8
    return 0.9 if money > 800 else 1

result = calculate_discount("vip",800)
print(result)