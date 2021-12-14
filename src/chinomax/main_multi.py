import multiprocessing
import time
import colorama
import utils.messages as messages
import utils.repository as repository
from typing import List
from datetime import datetime
from model.supermarket import Supermarket
from src.chinomax.model.cart import Cart
from src.chinomax.model.cashier_point_base import CashierPointBase

super_market_name = 'ChinoMax'


def main():
    pool = multiprocessing.Pool()
    t0 = datetime.now()

    print(colorama.Fore.WHITE + messages.get_header_text(name=super_market_name), flush=True)

    cashier_point_east = CashierPointBase(name='EAST')
    cashier_point_north = CashierPointBase(name='NORTH')
    cashier_point_west = CashierPointBase(name='WEST')

    tasks = [pool.apply_async(func=pay_cart,
                              args=(cashier_point_east, repository.get_carts_from_east_cashier_point())),
             pool.apply_async(func=pay_cart,
                              args=(cashier_point_north, repository.get_carts_from_north_cashier_point())),
             pool.apply_async(func=pay_cart,
                              args=(cashier_point_west, [repository.get_cart_from_west_cashier_point()]))]

    pool.close()
    pool.join()

    cashier_points = [t.get() for t in tasks]
    super_market = Supermarket(name=super_market_name, cashier_points=cashier_points)

    dt = datetime.now() - t0

    show_results(super_market)

    print(colorama.Fore.WHITE + f'Total time: {dt.total_seconds():.0f} seconds', flush=True)


def pay_cart(cashier_point: CashierPointBase, carts: List[Cart]):
    current_process = multiprocessing.current_process()

    for cart in carts:
        delay = cart.get_delayed_seconds()

        time.sleep(delay)
        cashier_point.add_incomes(cart.get_total_cart())
        cashier_point.add_time(delay)

        print(colorama.Fore.YELLOW + f'Cart Id: {current_process.pid}-{cart.get_id()} - '
                                     f'Cashier Point: {cashier_point.get_name()} - '
                                     f'Delayed: {delay}', flush=True)

    return cashier_point


def show_results(super_market: Supermarket):
    message = '''
    ----------------------------------------------
    '''

    for cashier_point in super_market.get_cashier_points():
        message += f'''
    Cashier Point: {cashier_point.get_name()} 
    Total: {cashier_point.get_incomes():.2f} 
    Time: {cashier_point.get_time()}
    '''

    message += f'''
    ----------------------------------------------

    Total Incomes: {super_market.get_incomes():.2f}
    '''

    print(colorama.Fore.CYAN + message, flush=True)


if __name__ == '__main__':
    main()
