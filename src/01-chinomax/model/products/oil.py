from model.products.product import Product

PRICE = 45.70


class Oil(Product):
    def __init__(self):
        super().__init__(PRICE)
