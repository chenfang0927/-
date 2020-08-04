"""
class Commodity:
        def __init__(self, cid, name, price):
            self.cid = cid
            self.name = name
            self.price = price

    list_commodity_infos = [
        Commodity(1001, "屠龙刀", 10000),
        Commodity(1002, "倚天剑", 10000),
        Commodity(1003, "金箍棒", 52100),
        Commodity(1004, "口罩", 20),
        Commodity(1005, "酒精", 30)
        Commodity(1006, "屠龙刀", 10000),
        Commodity(1007, "口罩", 50),
    ]
    -- 定义函数,删除列表中价格大于1w的商品
    -- (选做) 定义函数,删除列表中商品名称相同的商品(不使用其他容器,自定义算法)
"""
class Commodity:
    def __init__(self, cid, name, price):
        self.cid = cid
        self.name = name
        self.price = price


list_commodity_infos = [
    Commodity(1001, "屠龙刀", 10000),
    Commodity(1002, "倚天剑", 10000),
    Commodity(1003, "金箍棒", 52100),
    Commodity(1004, "口罩", 20),
    Commodity(1005, "酒精", 30),
    Commodity(1006, "屠龙刀", 10000),
    Commodity(1007, "口罩", 50),
]

def delete_all_gt_1w():
    for i in range(len(list_commodity_infos) - 1, -1, -1):
        if list_commodity_infos[i].price > 10000:
            del list_commodity_infos[i]


# delete_all_gt_1w()
# for item in list_commodity_infos:
#     print(item.__dict__)

def remove_duplicate():
    for r in range(len(list_commodity_infos) - 1, 0, -1):
        for c in range(r):
            if list_commodity_infos[r].name == list_commodity_infos[c].name:
                del list_commodity_infos[r]
                break

remove_duplicate()
for item in list_commodity_infos:
    print(item.__dict__)
