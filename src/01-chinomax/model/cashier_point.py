import multiprocessing
import colorama
from asyncio import sleep, Semaphore
from threading import current_thread
from model.cart import Cart
from model.cashier_point_base import CashierPointBase


class CashierPoint(CashierPointBase):
    def __init__(self, name: str):
        super().__init__(name)
        self.__semaphore = Semaphore(value=1)

    async def pay_cart_async(self, cart: Cart):
        current_process = multiprocessing.current_process()
        thread_id = current_thread().ident
        delay = cart.get_delayed_seconds()

        async with self.__semaphore:
            await sleep(delay)

            self.add_incomes(cart.get_total_cart())
            self.add_time(delay)

        # print(colorama.Fore.YELLOW + f'Cart Id: {cart.get_id()} - '
        #                              f'Cashier Point: {self.get_name()} - '
        #                              f'Delayed: {delay}', flush=True)
        print(colorama.Fore.YELLOW + f'Process Id: {current_process.pid} - '
                                     f'Thread Id: {thread_id} - '
                                     f'Cart Id: {cart.get_id()} - '
                                     f'Cashier Point: {self.get_name()} - '
                                     f'Delayed: {delay}', flush=True)
