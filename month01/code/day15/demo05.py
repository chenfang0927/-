"""
    异常处理
        目的:错误状态(向上翻)  -->   正常状态(向下走)
        核心价值：保障程序按照既定流程执行
"""


def div_apple(apple_count):
    person_count = int(input("请输入人数:"))
    result = apple_count / person_count
    print("每人%d个苹果" % (result))


# 写法1:对症下药(官方建议)
"""
# 检测可能出错的代码
try:
    div_apple(10)
# 定位错误代码
except ValueError:
    print("不能输入非整数类型")
except ZeroDivisionError:
    print("不能输入零")

print("后续逻辑")
"""

# 写法2:包治百病(常用)
"""
# 检测可能出错的代码
try:
    div_apple(10)
# 定位全部错误代码
# except Exception:
except:
    print("出错喽")

print("后续逻辑")
"""

# 写法3:一定执行的逻辑
"""
# 检测可能出错的代码
try:
    div_apple(10)
    # 打开文件
    # 处理文件(错误) 
# 最终 无论是否发生错误,一定执行的代码.
finally:
    # 关闭文件
    print("分苹果结束")

print("后续逻辑")
"""

# 写法4:没有出错才执行的逻辑
# 检测可能出错的代码
try:
    div_apple(10)
except:
    print("出错啦")
# 没有出错才执行的逻辑
else:
    print("分苹果成功啦")

print("后续逻辑")
