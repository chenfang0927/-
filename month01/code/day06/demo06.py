"""
    字典推导式
"""

# 　需求：range(1,11)中的数字作为key,平方作为value
# dict01 = {}
# for number in range(1, 11):
#     dict01[number] = number ** 2

dict01 = {number: number ** 2
          for number in range(1, 11)
          }

# dict01 = {}
# for number in range(1, 11):
#     if number % 2 ==0:
#         dict01[number] = number ** 2

dict01 = {number: number ** 2
          for number in range(1, 11)
          if number % 2 == 0}
print(dict01)

