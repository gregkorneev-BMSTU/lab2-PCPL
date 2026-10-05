# Лабораторная работа №2

## Функциональные возможности языка Python

Простая реализация всех 7 задач лабораторной работы:
https://github.com/ugapanyuk/BKIT_2022/wiki/lab_python_fp

Проект специально написан без сложных конструкций, чтобы код было удобно переписать вручную и объяснить на защите.

## Структура

```text
lab_python_fp_project/
├── .gitignore
├── README.md
├── requirements.txt
└── lab_python_fp/
    ├── __init__.py
    ├── field.py
    ├── gen_random.py
    ├── unique.py
    ├── sort.py
    ├── print_result.py
    ├── cm_timer.py
    ├── process_data.py
    └── data_light.json
```

## Запуск отдельных задач

Из корня проекта:

```bash
python lab_python_fp/field.py
python lab_python_fp/gen_random.py
python lab_python_fp/unique.py
python lab_python_fp/sort.py
python lab_python_fp/print_result.py
python lab_python_fp/cm_timer.py
```

## Запуск итоговой задачи

```bash
python lab_python_fp/process_data.py lab_python_fp/data_light.json
```

`process_data.py` получает путь к JSON-файлу первым аргументом командной строки.

## Что делает каждый файл

- `field.py` — генератор значений выбранных полей словаря.
- `gen_random.py` — генератор случайных целых чисел.
- `unique.py` — итератор, пропускающий повторяющиеся элементы.
- `sort.py` — сортировка чисел по модулю с `lambda` и без неё.
- `print_result.py` — декоратор для печати имени функции и результата.
- `cm_timer.py` — два контекстных менеджера для измерения времени.
- `process_data.py` — цепочка `f1 -> f2 -> f3 -> f4` для обработки вакансий.

## О данных

В проект включён небольшой `data_light.json` с той же нужной для задания структурой (`job-name`), чтобы проект запускался сразу. При работе с полным набором данных из методички достаточно передать путь к официальному `data_light.json` вместо этого файла.
