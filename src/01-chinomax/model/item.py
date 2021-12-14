from model.products.product import Product


class Item:
    def __init__(self, product: Product, quantity: int):
        self.__product = product
        self.__quantity = quantity

    def get_total_price(self):
        return self.__product.get_price() * self.__quantity
