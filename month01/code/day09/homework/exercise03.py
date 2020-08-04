# ---------------全局变量-------------
# 员工列表(员工编号 部门编号 姓名 工资)
dict_employees = {
    1001: {"did": 9002, "name": "师父", "money": 60000},
    1002: {"did": 9001, "name": "孙悟空", "money": 50000},
    1003: {"did": 9002, "name": "猪八戒", "money": 20000},
    1004: {"did": 9001, "name": "沙僧", "money": 30000},
    1005: {"did": 9001, "name": "小白龙", "money": 15000},
}

# 部门列表
list_departments = [
    {"did": 9001, "title": "教学部"},
    {"did": 9002, "title": "销售部"},
    {"did": 9003, "title": "品保部"},
]

# ---------------函数-------------

# 1. 打印所有员工信息,
def print_employees():
    for eid, emp in dict_employees.items():
        print(f"{emp['name']}的员工编号是{eid},部门编号是{emp['did']},月薪{emp['money']}元.")

print_employees()

# 2. 打印所有月薪大于2w的员工信息,
# 格式：xx的员工编号是xx,部门编号是xx,月薪xx元.
def print_employees_gt_2w():
    for eid, emp in dict_employees.items():
        if emp['money'] > 20000:
            print(f"{emp['name']}的员工编号是{eid},部门编号是{emp['did']},月薪{emp['money']}元.")


# 3. 在部门列表中查找编号最小的部门
def get_min_by_department():
    max_value = list_departments[0]
    for i in range(1, len(list_departments)):
        if max_value["did"] < list_departments[i]["did"]:
            max_value = list_departments[i]
    return max_value


# 4. 根据部门编号对部门列表降序排列
def descending_order_by_did():
    for r in range(len(list_departments) - 1):
        for c in range(r + 1, len(list_departments)):
            if list_departments[r]["did"] < list_departments[c]["did"]:
                list_departments[r], list_departments[c] = list_departments[c], list_departments[r]

# ---------------入口-------------
print_employees()