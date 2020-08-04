"""
    在终端中录入4个同学身高,打印最高的值.
    算法：
        170    160    180    165
        假设第一个就是最大值
        使用假设的和第二个进行比较, 发现更大的就替换假设的
        使用假设的和第三个进行比较, 发现更大的就替换假设的
        使用假设的和第四个进行比较, 发现更大的就替换假设的
        最后，假设的就是最大的.
"""
height1 = int(input("请输入身高："))
height2 = int(input("请输入身高："))
height3 = int(input("请输入身高："))
height4 = int(input("请输入身高："))
max_value = height1
if max_value < height2:
    max_value = height2
# 使用假设的(可能是第一个也可能是第二个)和第三个身高比较
if max_value < height3:
    max_value = height3
if max_value < height4:
    max_value = height4
print("最高的同学是" + str(max_value))
