from abc import abstractmethod


class DatabaseConnectionBase:
    @abstractmethod
    def __update_id(self, updated_id: int):
        pass

    @abstractmethod
    def get_id(self):
        pass
