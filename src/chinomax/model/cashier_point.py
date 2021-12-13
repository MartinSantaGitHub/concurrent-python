import time
import colorama
from threading import RLock
from asyncio import sleep, Lock
from src.chinomax.model.cart import Cart


class CashierPoint:
    def __init__(self, name: str):
        self.__name = name
        self.__incomes = 0
        self.__time = 0
        self.__async_semaphore = Lock()
        self.__multi_semaphore = RLock()

    def get_name(self):
        return self.__name

    def get_incomes(self):
        return self.__incomes

    def get_time(self):
        return self.__time

    async def pay_cart_async(self, cart: Cart):
        delay = cart.get_delayed_seconds()

        async with self.__async_semaphore:
            await sleep(delay)

            self.__incomes += cart.get_total_cart()
            self.__time += delay

        print(colorama.Fore.YELLOW + f'Cart Id: {cart.get_id()} - Cashier Point: {self.__name} - Delayed: {delay}', flush=True)

    def pay_cart_multi(self, cart: Cart):
        delay = cart.get_delayed_seconds()

        with self.__multi_semaphore:
            time.sleep(10)

            self.__incomes += cart.get_total_cart()
            self.__time += delay

        print(colorama.Fore.YELLOW + f'Cart Id: {cart.get_id()} - Cashier Point: {self.__name} - Delayed: {delay}', flush=True)
