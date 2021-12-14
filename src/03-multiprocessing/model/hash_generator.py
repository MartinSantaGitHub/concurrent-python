import datetime
import hashlib
import colorama
import multiprocessing
from threading import current_thread


class HashGenerator:
    def __init__(self, difficulty: int):
        self.__difficulty = difficulty

    def __calculate_hash(self, timestamp: datetime.datetime, seed: int):
        data = str(timestamp) + str(seed)
        data = data.encode()
        hash = hashlib.sha256(data).hexdigest()

        return hash

    def get_hash(self):
        timestamp = datetime.datetime.now()
        seed = 0
        hash = self.__calculate_hash(timestamp, seed)
        difficulty_check = '0' * self.__difficulty

        while hash[:self.__difficulty] != difficulty_check:
            seed += 1
            hash = self.__calculate_hash(timestamp, seed)

        return hash

    def get_hashes(self, quantity: int):
        current_process = multiprocessing.current_process()
        thread_id = current_thread().ident
        hashes = []

        while quantity > 0:
            # print(colorama.Fore.YELLOW + f'Process Id: {current_process.pid} - '
            #                              f'Thread Id: {thread_id} - '
            #                              f'Quantity: {quantity}', flush=True)
            hashes.append(self.get_hash())
            quantity -= 1

        return hashes
