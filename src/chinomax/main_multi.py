import multiprocessing
import time
from multiprocessing import Process

import colorama
import utils.messages as messages
import utils.repository as repository
from datetime import datetime
from model.cashier_point import CashierPoint
from model.supermarket import Supermarket
from src.chinomax.model.cart import Cart

super_market_name = 'ChinoMax'





def main():
    global pay_cart
    def pay_cart(cashier_point: CashierPoint, cart: Cart):
        p = multiprocessing.current_process()
        time.sleep(5)
    pool = multiprocessing.Pool()
    tasks = []
    cashier_points = {'east_cp': CashierPoint(name='EAST'),
                      'north_cp': CashierPoint(name='NORTH'),
                      'west_cp': CashierPoint(name='WEST')}
    super_market = Supermarket(name=super_market_name, cashier_points=list(cashier_points.values()))
    t0 = datetime.now()

    print(colorama.Fore.WHITE + messages.get_header_text(name=super_market_name), flush=True)

    # tasks += [Process(target=pay_cart, args=(cashier_points['east_cp'], cart))
    #           for cart in repository.get_carts_from_east_cashier_point()]
    # tasks += [Process(target=pay_cart, args=(cashier_points['north_cp'], cart))
    #           for cart in repository.get_carts_from_north_cashier_point()]
    b = Process(target=pay_cart, args=(cashier_points['west_cp'], repository.get_cart_from_west_cashier_point(),))

    #pool.close()
    #pool.join()

    if __name__ == "__main__":
        b.start()

    #[a.start() for a in tasks]
    #[a.join() for a in tasks]

    dt = datetime.now() - t0

    show_results(super_market)

    print(colorama.Fore.WHITE + f'Total time: {dt.total_seconds()} seconds', flush=True)


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
