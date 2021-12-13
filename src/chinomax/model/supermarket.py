from typing import List
from src.chinomax.model.cashier_point import CashierPoint


class Supermarket:
    def __init__(self, name: str, cashier_points: List[CashierPoint]):
        self.__name = name
        self.__cashier_points = cashier_points

    def get_name(self):
        return self.__name

    def get_cashier_points(self):
        return self.__cashier_points

    def get_incomes(self):
        return sum([i.get_incomes() for i in self.__cashier_points])
