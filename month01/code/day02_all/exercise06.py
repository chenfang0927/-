"""
    在终端中获取商品单价、购买的数量和支付金额。
    计算应该找回多少钱。
"""
# 1. 获取数据
unit_price = float(input("请输入商品单价："))
amount = int(input("请输入购买的数量："))
money = float(input("请输入支付金额："))
# 2. 逻辑处理
result = money - unit_price * amount
# 3. 显示结果
print("应该找回" + str(result))
