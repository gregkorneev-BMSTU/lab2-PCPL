# Задача 1. Генератор field по шаблону из ТЗ.


def field(items, *args):
    # Для каждого словаря нужно указать хотя бы одно поле.
    assert len(args) > 0

    for item in items:
        if len(args) == 1:
            value = item.get(args[0])
            # Значения None по условию задания пропускаются.
            if value is not None:
                yield value
        else:
            result = {}
            for key in args:
                value = item.get(key)
                if value is not None:
                    result[key] = value

            if result:
                yield result


if __name__ == '__main__':
    goods = [
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'color': 'black'}
    ]

    # list() показывает все значения генератора.
    print(list(field(goods, 'title')))
    print(list(field(goods, 'title', 'price')))
