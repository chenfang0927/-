"""
os模块处理文件
"""
import os

# 获取文件大小
print(os.path.getsize("./my.log"))

# 获取一个目录中所有文件名
print(os.listdir("."))

# 判断文件是否存在
print(os.path.exists("./my.log"))

# 是否为普通文件
print(os.path.isfile("./my.log"))

# 删除文件
os.remove("my.log")