"""
    请排列出所有扑克牌(大小王不算,使用列表存储)
    ["红桃","黑桃","方片","梅花"]
    ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
"""
type_card = ["红桃", "黑桃", "方片", "梅花"]
card_num = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
list_card = [(type, num) for type in type_card for num in card_num]
print(list_card)
