from sqlalchemy import create_engine
from sqlalchemy.engine import CursorResult
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.sql import text
from typing import Union


class DatabaseConnection:

    def __init__(self, driver: str, username: str, password: str, host: str, port: Union[int, str], name: str):
        self.driver = driver
        self.username = username
        self.password = password
        self.host = host
        self.port = port
        self.name = name
        self.db_path = self.__set_database()
        self.engine = self.__set_engine()
        self.session = self.__set_session()

    def __set_database(self):
        return '{}://{}:{}@{}:{}/{}'.format(self.driver, self.username, self.password, self.host, self.port, self.name)

    def __set_engine(self):
        return create_engine(self.db_path, pool_size=20, max_overflow=0)

    def __set_session(self):
        return sessionmaker(bind=self.driver)

    def __execute(self, sql_query: str, params: dict = None) -> CursorResult:
        sql_query = text(sql_query)

        with self.engine.connect() as conn:
            with Session(bind=conn) as session:
                result = session.execute(statement=sql_query, params=params)

                session.commit()

        return result

    def get_id(self):
        sql_get = 'SELECT current_id FROM sequencer_id LIMIT 1;'

        current_id = self.__execute(sql_get).fetchone()[0]
        next_id = current_id + 1

        return next_id

    def update_id(self, updated_id: int):
        sql_update = f'UPDATE sequencer_id SET current_id = {updated_id};'

        self.__execute(sql_update)
