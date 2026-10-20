# Задача 2. Генератор случайных чисел.

from random import randint


def gen_random(num_count, begin, end):
    for _ in range(num_count):
        # randint включает обе границы диапазона.
        yield randint(begin, end)


if __name__ == '__main__':
    print(list(gen_random(5, 1, 3)))
