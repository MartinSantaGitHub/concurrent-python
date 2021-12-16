import multiprocessing
import colorama
from multiprocessing.managers import BaseManager
from multiprocessing import Semaphore, Process
from dotenv import load_dotenv
from threading import current_thread
from utils.db_connection import DatabaseConnectionBase
from utils.db_connection_mock import DatabaseConnectionMock

load_dotenv()


def show_id(db_conn: DatabaseConnectionBase):
    current_process = multiprocessing.current_process()
    thread_id = current_thread().ident
    current_id = db_conn.get_id()

    print_results(current_process.pid, thread_id, current_id)
    #print(f'db_conn: {str(db_conn)}')


def show_id_safe(db_conn: DatabaseConnectionBase, semaphore: Semaphore):
    current_process = multiprocessing.current_process()
    thread_id = current_thread().ident

    with semaphore:
        current_id = db_conn.get_id()

    print_results(current_process.pid, thread_id, current_id)
    #print(f'db_conn: {str(db_conn)}')


def print_results(pid: int, thread_id: int, current_id: int):
    print(colorama.Fore.YELLOW + f'Process Id: {pid} - '
                                 f'Thread Id: {thread_id} - '
                                 f'Sequencer Id: {current_id}', flush=True)


def main():
    BaseManager.register('DatabaseConnectionMock', DatabaseConnectionMock)
    manager = BaseManager()

    manager.start()

    db_conn = manager.DatabaseConnectionMock()
    semaphore = Semaphore(value=1)
    processes = []

    print()
    #print(f'db_conn init: {str(db_conn)}')

    for _ in range(6):
        processes.append(Process(target=show_id_safe, args=(db_conn, semaphore)))

    [p.start() for p in processes]
    [p.join() for p in processes]


if __name__ == '__main__':
    main()
