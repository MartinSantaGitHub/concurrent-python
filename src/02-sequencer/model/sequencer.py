import random
import time
from threading import RLock
from utils.db_connection import DatabaseConnection


class Sequencer:
    def __init__(self, db_connection: DatabaseConnection):
        self.__db_conn = db_connection
        self.__semaphore = RLock()

    def get_id(self):
        delay = random.randint(3, 9)

        time.sleep(delay)

        with self.__semaphore:
            next_id = self.__db_conn.get_id()

        return next_id
