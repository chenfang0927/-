"""
    一家公司有如下岗位：
     "经理"："曹操","刘备","孙权"
     "技术" ："曹操","刘备","张飞","关羽“
    2. 是经理也是技术的都有谁?
    3. 是经理不是技术的都有谁?
    4. 不是经理是技术的都有谁?
    5. 身兼一职的都有谁?
    6. 公司总共有多少人数?
"""
manager = {"曹操", "刘备", "孙权"}
technicist = {"曹操", "刘备", "张飞", "关羽"}
print(manager & technicist)  # 交集 {'刘备', '曹操'}
print(manager - technicist)  # 补集 {'孙权'}
print(technicist - manager)  # 补集 {'张飞', '关羽'}
print(technicist ^ manager)  # 补集 {'孙权', '张飞', '关羽'}
print(len(manager | technicist))  # 并集 5
