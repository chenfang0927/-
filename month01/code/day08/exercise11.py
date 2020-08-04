"""
    参照day07/exercise03
    将之前6个练习作为函数
"""
# 商品字典
dict_commodity_infos = {
    1001: {"name": "屠龙刀", "price": 10000},
    1002: {"name": "倚天剑", "price": 10000},
    1003: {"name": "金箍棒", "price": 52100},
    1004: {"name": "口罩", "price": 20},
    1005: {"name": "酒精", "price": 30},
}

# 订单列表
list_orders = [
    {"cid": 1001, "count": 1},
    {"cid": 1002, "count": 3},
    {"cid": 1005, "count": 2},
]


# 1.打印所有商品信息,
def print_commodity_infos():
    for cid, info in dict_commodity_infos.items():
        print(f'编号{cid},名称{info["name"]},单价{info["price"]}')


# 2. 打印所有订单中的信息,
def print_order_infos():
    for order in list_orders:
        print("商品编号%d,购买数量%d." % (order["cid"], order["count"]))


# 3. 打印商品单价小于2万的商品信息
def print_commodity_infos_lt_2w():
    for cid, info in dict_commodity_infos.items():
        if info["price"] < 20000:
            print("商品编号%d,商品名称%s,商品单价%d." % (cid, info["name"], info["price"]))


# 4. 打印所有订单中的商品信息,
def print_commodity_in_order():
    for order in list_orders:
        cid = order["cid"]
        comodity = dict_commodity_infos[cid]
        print("商品名称%s,商品单价:%d,数量%d." % (comodity["name"], comodity["price"], order["count"]))


# 5. 查找数量最多的订单(使用自定义算法,不使用内置函数)
def get_max_order_by_count():
    max_value = list_orders[0]
    for i in range(1, len(list_orders)):
        if max_value["count"] < list_orders[i]["count"]:
            max_value = list_orders[i]
    return max_value


# 6. 根据购买数量对订单列表降序(大->小)排列
# 取数据(不要最后一个)
def descending_order_by_count():
    for r in range(len(list_orders) - 1):
        # 作比较(下一个)
        for c in range(r + 1, len(list_orders)):
            if list_orders[r]["count"] > list_orders[c]["count"]:
                list_orders[r], list_orders[c] = list_orders[c], list_orders[r]


# 调用
print_commodity_infos()
print_order_infos()
print_commodity_infos_lt_2w()
print_commodity_in_order()
result = get_max_order_by_count()
print(result)
descending_order_by_count()
print(list_orders)