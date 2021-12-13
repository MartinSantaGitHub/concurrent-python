import asyncio
import colorama
import utils.messages as messages
import utils.repository as repository
from datetime import datetime
from model.cashier_point import CashierPoint
from model.supermarket import Supermarket

super_market_name = 'ChinoMax'


def main():
    loop = asyncio.get_event_loop()

    tasks = []
    cashier_points = {'east_cp': CashierPoint(name='EAST'),
                      'north_cp': CashierPoint(name='NORTH'),
                      'west_cp': CashierPoint(name='WEST')}
    super_market = Supermarket(name=super_market_name, cashier_points=list(cashier_points.values()))
    t0 = datetime.now()

    print(colorama.Fore.WHITE + messages.get_header_text(name=super_market_name), flush=True)

    tasks += [loop.create_task(cashier_points['east_cp'].pay_cart_async(cart))
              for cart in repository.get_carts_from_east_cashier_point()]
    tasks += [loop.create_task(cashier_points['north_cp'].pay_cart_async(cart))
              for cart in repository.get_carts_from_north_cashier_point()]
    tasks += [loop.create_task(cashier_points['west_cp'].pay_cart_async(repository.get_cart_from_west_cashier_point()))]

    final_task = asyncio.gather(*tasks)

    loop.run_until_complete(final_task)

    dt = datetime.now() - t0

    show_results(super_market)

    print(colorama.Fore.WHITE + f'Total time: {dt.total_seconds():.0f} seconds', flush=True)


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
