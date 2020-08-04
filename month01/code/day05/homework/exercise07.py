# 9, 根据下列信息提取变量
#    使用占位符拼接字符串·
#     湖北确诊67802人,治愈63326人,治愈率0.93
# 	70秒是1分钟零10秒


# 在固定的格式中,插入灵活的数据.
message = "湖北确诊%d人,治愈%d人,治愈率%.1f" % (67802, 63326, 0.93)
print(message)

rate_cure = 0.93
message = f"湖北确诊{67802}人,治愈{63326}人,治愈率{rate_cure:.1}"
print(message)

second = 70
message = "%d秒是%.2d分钟零%d秒" % (second, second // 60, second % 60)
print(message)

# f-string 整数不足两位使用0填充
# https://blog.csdn.net/sunxb10/article/details/81036693
message = f"{second}秒是{second // 60:02}分钟零{second % 60}秒"
print(message)
