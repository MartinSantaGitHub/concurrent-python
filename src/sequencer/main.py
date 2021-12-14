import os
import colorama
import multiprocessing
from dotenv import load_dotenv
from threading import Thread, current_thread
from src.sequencer.model.sequencer import Sequencer
from src.sequencer.utils.db_connection import DatabaseConnection

load_dotenv()


def show_id(seq: Sequencer):
    current_process = multiprocessing.current_process()
    thread_id = current_thread().ident
    current_id = seq.get_id()

    print(colorama.Fore.YELLOW + f'Process Id: {current_process.pid} - Thread Id: {thread_id} - Current Id: {current_id}', flush=True)


def main():
    db_driver = os.environ["DB_DRIVER"]
    db_name = os.environ["DB_NAME"]
    db_user = os.environ["DB_USER"]
    db_password = os.environ["DB_PASSWORD"]
    db_host = os.environ["DB_HOST"]
    db_port = os.environ["DB_PORT"]
    db_conn = DatabaseConnection(db_driver, db_user, db_password, db_host, db_port, db_name)
    sequencer = Sequencer(db_conn)

    jobs = [
        Thread(target=show_id, args=(sequencer,)),
        Thread(target=show_id, args=(sequencer,)),
        Thread(target=show_id, args=(sequencer,)),
        Thread(target=show_id, args=(sequencer,)),
        Thread(target=show_id, args=(sequencer,)),
        Thread(target=show_id, args=(sequencer,))
    ]

    [j.start() for j in jobs]
    [j.join() for j in jobs]


if __name__ == '__main__':
    main()
