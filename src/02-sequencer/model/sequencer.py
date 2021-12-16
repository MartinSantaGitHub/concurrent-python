from threading import Semaphore
from utils.db_connection_base import DatabaseConnectionBase


class Sequencer:
    def __init__(self, db_connection: DatabaseConnectionBase):
        self.__db_conn = db_connection
        self.__semaphore = Semaphore(value=1)

    def get_id(self):
        return self.__db_conn.get_id()

    def get_id_safe(self):
        with self.__semaphore:
            return self.__db_conn.get_id()
