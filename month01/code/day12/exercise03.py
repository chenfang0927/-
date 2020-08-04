"""

"""
class Commodity:
    def __init__(self, cid=0, name="", price=0):
        self.cid = cid
        self.name = name
        self.price = price

    def __eq__(self, other):
        return self.cid == other.cid

    def __lt__(self, other):
        return self.price < other.price

list_commodity_infos = [
    Commodity(1001, "屠龙刀", 10000),
    Commodity(1002, "倚天剑", 10000),
    Commodity(1003, "金箍棒", 52100),
    Commodity(1004, "口罩", 20),
    Commodity(1005, "酒精", 30),
]
# 1. 在商品列表中,查找Commodity(1003)的索引  列表.index
print(list_commodity_infos.index(Commodity(1003)))
# 2. 在商品列表中,判断是否存在Commodity(1005)的商品 Commodity(1005) in 列表
print(Commodity(1005) in list_commodity_infos)
# 3. 在商品列表中,移除Commodity(1002)对象   列表.remove
list_commodity_infos.remove(Commodity(1002))
# 4. 在商品列表中,根据单价升序排列    列表.sort
list_commodity_infos.sort()
print(list_commodity_infos)
# 5. 在商品列表中,获取单价最高的商品   max(列表)
print(max(list_commodity_infos).__dict__)
