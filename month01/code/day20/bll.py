
class Control:
    def __init__(self):
        self.list01 = []
        self.__star_sid = 1000

    def control_xinxi(self, i):
        self.__star_sid += 1
        i.sid = self.__star_sid
        self.list01.append(i)

    def remmodify(self, i):
        for inf in self.list01:
            if inf.sid == i:
                self.list01.remove(inf)
                return True
        return False



