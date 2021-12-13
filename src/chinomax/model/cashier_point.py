import colorama
from asyncio import sleep, Lock
from src.chinomax.model.cart import Cart
from src.chinomax.model.cashier_point_base import CashierPointBase


class CashierPoint(CashierPointBase):
    def __init__(self, name: str):
        super().__init__(name)
        self.__async_semaphore = Lock()

    async def pay_cart_async(self, cart: Cart):
        delay = cart.get_delayed_seconds()

        async with self.__async_semaphore:
            await sleep(delay)

            self.add_incomes(cart.get_total_cart())
            self.add_time(delay)

        print(colorama.Fore.YELLOW + f'Cart Id: {cart.get_id()} - Cashier Point: {self.get_name()} - Delayed: {delay}', flush=True)
