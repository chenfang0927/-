"""
    封装数据练习
"""
class Commodity:
    def __init__(self, cid, name, price):
        self.cid = cid
        self.name = name
        self.price = price


class Order:
    def __init__(self, cid, count):
        self.cid = cid
        self.count = count


list_commodity_infos = [
    Commodity(1001, "屠龙刀", 10000),
    Commodity(1002, "倚天剑", 10000),
    Commodity(1003, "金箍棒", 52100),
    Commodity(1004, "口罩", 20),
    Commodity(1005, "酒精", 30),
]

list_orders = [
    Order(1001, 1),
    Order(1002, 3),
    Order(1005, 2),
]


def print_single_commodity(commodity):
    print(f"编号:{commodity.cid},商品名称:{commodity.name},商品单价:{commodity.price}")


# 1.定义函数,打印所有商品信息,
def print_commodity_infos():
    for commodity in list_commodity_infos:
        print_single_commodity(commodity)


# 2. 定义函数,打印商品单价小于2万的商品信息
def print_price_in_2w():
    for commodity in list_commodity_infos:
        if commodity.price < 20000:
            print_single_commodity(commodity)


# 3. 查找最贵的商品(使用自定义算法,不使用内置函数)
def commodity_max_by_price():
    max_value = list_commodity_infos[0]
    for i in range(1, len(list_commodity_infos)):
        if max_value.price < list_commodity_infos[i].price:
            # 使用更大的那个订单 替换 假设的订单
            max_value = list_commodity_infos[i]
    return max_value


# 4. 根据单价对商品列表降序排列
def descending_order_by_price():
    for r in range(len(list_commodity_infos) - 1):
        for c in range(r + 1, len(list_commodity_infos)):
            if list_commodity_infos[r].price < list_commodity_infos[c].price:
                list_commodity_infos[r], list_commodity_infos[c] = list_commodity_infos[c], list_commodity_infos[r]


# 5.  定义函数,打印所有订单中的商品信息
def print_order_infos():
    for order in list_orders:  # 遍历所有订单
        for commodity in list_commodity_infos:  # 遍历所有商品信息
            if order.cid == commodity.cid:
                print(f"商品名称{commodity.name},商品单价:{commodity.price},数量{order.count}.")
                break  # 跳出内层循环


#  ----------测试---------

descending_order_by_price()
for item in list_commodity_infos:
    # 打印自定义对象的风格
    # <__main__.类名 object at 0x..>
    print(item.__dict__)
