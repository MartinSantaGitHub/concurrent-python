import random
from typing import List
from src.chinomax.model.item import Item


class Cart:
    __id = 0

    def __init__(self, items: List[Item]):
        self.__items = items

    def get_id(self):
        Cart.__id += 1

        return Cart.__id

    def get_delayed_seconds(self):
        return random.randint(3, 9)

    def get_total_cart(self):
        return sum([i.get_total_price() for i in self.__items])
