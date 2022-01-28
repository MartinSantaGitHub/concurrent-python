import random
from typing import List
from model.item import Item


class Cart:
    __current_id = 0

    def __init__(self, items: List[Item]):
        Cart.__current_id += 1
        self.__items = items
        self.__id = Cart.__current_id

    def get_id(self):
        return self.__id

    def get_delayed_seconds(self):
        return random.randint(3, 9)

    def get_total_cart(self):
        return sum([i.get_total_price() for i in self.__items])
