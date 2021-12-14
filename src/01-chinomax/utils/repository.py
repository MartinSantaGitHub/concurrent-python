from typing import List
from model.cart import Cart
from model.item import Item
from model.products.milk import Milk
from model.products.oil import Oil
from model.products.rice import Rice


def get_carts_from_east_cashier_point() -> List[Cart]:
    # Total East Cashier Point: $328.40

    # Total cart1: $176.70
    cart1 = Cart([Item(product=Rice(), quantity=2), Item(product=Milk(), quantity=4), Item(product=Oil(), quantity=1)])

    # Total cart2: $65.50
    cart2 = Cart([Item(product=Rice(), quantity=1), Item(product=Milk(), quantity=2)])

    # Total cart3: $86.20
    cart3 = Cart([Item(product=Rice(), quantity=1), Item(product=Milk(), quantity=1), Item(product=Oil(), quantity=1)])

    return [cart1, cart2, cart3]


def get_carts_from_north_cashier_point() -> List[Cart]:
    # Total North Cashier Point: $212.90

    # Total cart1: $162.90
    cart1 = Cart([Item(product=Rice(), quantity=3), Item(product=Milk(), quantity=1), Item(product=Oil(), quantity=2)])

    # Total cart2: $50.0
    cart2 = Cart([Item(product=Milk(), quantity=2)])

    return [cart1, cart2]


def get_cart_from_west_cashier_point() -> Cart:
    # Total North Cashier Point: $214.60
    cart = Cart([Item(product=Rice(), quantity=5), Item(product=Oil(), quantity=3)])

    return cart
