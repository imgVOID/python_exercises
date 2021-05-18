"""
Создайте три программы: многопоточную, многопроцессорную, асинхронную.
Все они должны ожидать 2 секунды (time.sleep(2), asyncio.sleep(2)).
Выведите на экран время, затраченное на выполнение каждой из функций.

"""

import time
import threading
import asyncio
from concurrent.futures import ProcessPoolExecutor


def func(msg):
    start = time.time()
    print(msg)
    time.sleep(2)
    print('Time:', time.time() - start)


async def func_async():
    start = time.time()
    print('Asynchronous program start...')
    await asyncio.sleep(2)
    print('Time:', time.time() - start)

# Обязательно используйте запрет на выполнение в режиме модуля
if __name__ == '__main__':
    func('Synchronous program start...')
    # Напишите запуск корутины в цикле событий. Используйте asyncio.get_event_loop(),
    # event_loop.run_until_complete(func_async())

    # Напишите мультипотоковую программу. Используйте:
    # threading.Thread(target=func('Multithread program start...')),
    # threading.Thread.start() и threading.Thread.join()

    # Напишите мультипроцессорную программу. Используйте:
    # ProcessPoolExecutor(2), Executor.submit(func('Multiprocess program start...'))
