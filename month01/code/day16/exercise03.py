"""
    迭代图形管理器
    画出架构设计图
"""

class GraphicIterator:
    def __init__(self, data):
        self.data = data
        self.index = -1

    def __next__(self):
        self.index += 1
        if self.index < len(self.data):
            return self.data[self.index]
        else:
            raise StopIteration()


class GraphicManager:
    def __init__(self):
        self.all_graphic = []

    def add_graphic(self, graphic):
        self.all_graphic.append(graphic)

    def __iter__(self):
        return GraphicIterator(self.all_graphic)

manager = GraphicManager()
manager.add_graphic("圆形")
manager.add_graphic("矩形")
manager.add_graphic("三角形")

for item in manager:
    print(item)
