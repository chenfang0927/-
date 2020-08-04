"""
    复习面向对象
        面向对象：考虑问题从对象的角度出发
            识别对象   分配职责   建立交互
        三个特征：
            封装：分而治之,变则疏之      [分]
            继承：抽象、统一、隔离变化   [隔]
            多态：体现子类个性(变化)    [做]
        六个原则：
            开闭原则：能够增加新功能,不修改客户端代码.
            单一职责：小而精,有且只有一个改变的原因
            依赖倒置：使用抽象(爸爸),不适用具体(儿子)
            组合复用：优先使用组合关系,不是继承关系.
                继承：统一变化(交通工具约束火车汽车在运输的行为上是一致的)
                组合：连接变化(人通过变量调用交通工具)
            里氏替换：形参是父,实参可以是各种子类。
                     建议扩展重写
            迪米特：通过抽象隔离调用(低耦合)
"""