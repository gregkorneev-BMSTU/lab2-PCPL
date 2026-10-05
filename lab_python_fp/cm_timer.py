# Задача 6. Контекстные менеджеры для измерения времени.

import time
from contextlib import contextmanager


class cm_timer_1:
    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        end_time = time.time()
        print(f'time: {end_time - self.start_time}')


@contextmanager
def cm_timer_2():
    start_time = time.time()
    try:
        yield
    finally:
        end_time = time.time()
        print(f'time: {end_time - start_time}')


if __name__ == '__main__':
    print('cm_timer_1:')
    with cm_timer_1():
        time.sleep(0.1)

    print('cm_timer_2:')
    with cm_timer_2():
        time.sleep(0.1)
