class CashierPointBase:
    def __init__(self, name: str):
        self.__name = name
        self.__incomes = 0
        self.__time = 0

    def get_name(self):
        return self.__name

    def get_incomes(self):
        return self.__incomes

    def get_time(self):
        return self.__time

    def set_name(self, name: str):
        self.__name = name

    def add_incomes(self, incomes: float):
        self.__incomes += incomes

    def add_time(self, time: float):
        self.__time += time
