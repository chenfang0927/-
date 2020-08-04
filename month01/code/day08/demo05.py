"""
    函数 -- 返回值 应用
        设计理念：崇尚小而精,拒绝大而全
    练习：exercise03~09
"""


# # 1. 获取数据
# usd = input("请输入美元：")
# # 2. 逻辑处理
# rmb = float(usd) * 7.1465
# # 3. 显示结果
# print(usd + "美元 =" + str(rmb) + "人民币")

# 将一个功能从头到尾实现,分割为做法 + 用法
#  获取数据 -->  参数
#  逻辑处理 -->  函数体
#  显示结果 -->  返回值
def usd_to_rmb(usd):
    # 2. 逻辑处理
    rmb = float(usd) * 7.1465
    return rmb


rmb = usd_to_rmb("20")
print(rmb)
