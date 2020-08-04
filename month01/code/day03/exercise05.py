"""
    在收银台练习基础上，增加新功能。
	如果钱不够提示"金额不足"
	否则提示"应找回：xx元"
"""
price = float(input("请输入单价："))
num = int(input("请输入数量："))
money = float(input("请输入金额："))
return_back = money - price * num
if return_back > 0:
    print("应找回" + str(return_back) + "元")
else:
    print("金额不足")

