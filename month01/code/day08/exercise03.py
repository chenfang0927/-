# 练习:参照day02/exercise06案例,创建收银台找零函数
# # 1. 获取数据
# unit_price = float(input("请输入商品单价："))
# amount = int(input("请输入购买的数量："))
# money = float(input("请输入支付金额："))
# # 2. 逻辑处理
# result = money - unit_price * amount
# # 3. 显示结果
# print("应该找回" + str(result))

def change_money(money, unit_price, amount):
    """
        收银台找零功能
    :param money: 支付的金额
    :param unit_price: 单价
    :param amount: 购买数量
    :return: 应找回的金额
    """
    final_money = money - unit_price * amount
    return final_money


result = change_money(100, 13, 4)
print(result)
