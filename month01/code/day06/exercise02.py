"""
将下列英文语句按照单词进行翻转.
To have a government that is of people by people for people

people for people by people of is that government a have To
"""

message = 'To have a government that is of people by people for people'
list_temp = message.split(' ')
result = ' '.join(list_temp[::-1])
print(result)
