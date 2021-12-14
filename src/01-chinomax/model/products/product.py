class Product:
    def __init__(self, price: float):
        self.__price = price

    def get_price(self):
        return self.__price
