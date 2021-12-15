from typing import List
from model.cart import Cart
from model.item import Item
from model.product import Product

rice = Product(name='Rice', price=15.50)
milk = Product(name='Milk', price=25.0)
oil = Product(name='Oil', price=45.70)

def get_carts_from_east_cashier_point() -> List[Cart]:
    # Total East Cashier Point: $328.40

    # Total cart1: $176.70
    cart1 = Cart([Item(rice, quantity=2), Item(milk, quantity=4), Item(oil, quantity=1)])

    # Total cart2: $65.50
    cart2 = Cart([Item(product=rice, quantity=1), Item(product=milk, quantity=2)])

    # Total cart3: $86.20
    cart3 = Cart([Item(product=rice, quantity=1), Item(product=milk, quantity=1), Item(product=oil, quantity=1)])

    return [cart1, cart2, cart3]


def get_carts_from_north_cashier_point() -> List[Cart]:
    # Total North Cashier Point: $212.90

    # Total cart1: $162.90
    cart1 = Cart([Item(product=rice, quantity=3), Item(product=milk, quantity=1), Item(product=oil, quantity=2)])

    # Total cart2: $50.0
    cart2 = Cart([Item(product=milk, quantity=2)])

    return [cart1, cart2]


def get_cart_from_west_cashier_point() -> Cart:
    # Total North Cashier Point: $214.60
    cart = Cart([Item(product=rice, quantity=5), Item(product=oil, quantity=3)])

    return cart
