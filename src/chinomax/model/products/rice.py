from src.chinomax.model.products.product import Product

PRICE = 15.50


class Rice(Product):
    def __init__(self):
        super().__init__(PRICE)
