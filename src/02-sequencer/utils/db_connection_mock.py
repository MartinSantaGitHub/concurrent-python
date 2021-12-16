import time
from utils.db_connection import DatabaseConnectionBase


class DatabaseConnectionMock(DatabaseConnectionBase):
    def __init__(self):
        self.__current_id = 0

    def __update_id(self, updated_id: int):
        self.__current_id = updated_id

    def get_id(self):
        current_id = self.__current_id

        time.sleep(0.5)

        next_id = current_id + 1

        self.__update_id(next_id)

        time.sleep(0.25)

        return next_id
