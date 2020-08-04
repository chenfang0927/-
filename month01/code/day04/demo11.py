"""
    字符串格式化
        "格式" % (变量)
        在格式中可以写占位符(%s %d %f)
"""
# 灵活的数据
name = "唐僧"
age = 2
score = 100.51
# 按照固定的格式显示
# 字符串拼接（格式复杂代码可读性差）
# print("我是" + name + "今年" + str(age)
#       + "考试" + str(score) + "分")

# 占位符%s
print("我是%s今年%.2d考试%.1f分" % (name, age, score))


usd = "15"
rmb = float(usd) * 7.1465
# print(usd + "美元 =" + str(rmb) + "人民币")
print("%s美元 = %.2f人民币"%(usd,rmb))