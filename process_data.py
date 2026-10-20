# Задача 7. Итоговая обработка данных.

import json
import sys

from cm_timer import cm_timer_1
from field import field
from gen_random import gen_random
from print_result import print_result
from unique import Unique


@print_result
def f1(arg):
    # Убираем повторы без учета регистра и сортируем названия профессий.
    return sorted(Unique(field(arg, 'job-name'), ignore_case=True), key=lambda x: x.lower())


@print_result
def f2(arg):
    # Оставляем профессии, название которых начинается со слова «программист».
    return list(filter(lambda x: x.lower().startswith('программист'), arg))


@print_result
def f3(arg):
    # Добавляем каждой профессии отметку о знании Python.
    return list(map(lambda x: x + ' с опытом Python', arg))


@print_result
def f4(arg):
    # Генерируем по одной зарплате и соединяем её с каждой профессией.
    salaries = gen_random(len(arg), 100000, 200000)
    return list(map(lambda x: f'{x[0]}, зарплата {x[1]} руб.', zip(arg, salaries)))


def main():
    if len(sys.argv) < 2:
        raise SystemExit('Укажите путь к JSON-файлу с вакансиями.')

    path = sys.argv[1]
    with open(path, encoding='utf-8') as file:
        data = json.load(file)

    # Функции выполняются по цепочке, а таймер измеряет общее время.
    with cm_timer_1():
        f4(f3(f2(f1(data))))


if __name__ == '__main__':
    main()
