# Задача 4. Сортировка по модулю в порядке убывания.

data = [4, -30, 100, -100, 123, 1, 0, -1, -4]


if __name__ == '__main__':
    result = sorted(data, key=abs, reverse=True)
    print(result)

    result_with_lambda = sorted(data, key=lambda x: abs(x), reverse=True)
    print(result_with_lambda)
