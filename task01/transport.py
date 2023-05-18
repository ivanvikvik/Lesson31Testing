class Transport:
    def __init__(self, tank=1000):
        self.__tank = tank

    @property
    def tank(self):
        return self.__tank

    @tank.setter
    def tank(self, tank):
        return self.__tank

    def go(self):
        pass
