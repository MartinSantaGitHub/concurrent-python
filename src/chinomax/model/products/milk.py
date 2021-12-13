from src.chinomax.model.products.product import Product

PRICE = 25.0


class Milk(Product):
    def __init__(self):
        super().__init__(PRICE)
