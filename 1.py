def my_div(n_1, n_2):
    try:
        result = n_1 / n_2
        print(f'{n_1} / {n_2} = {result}')
    except ZeroDivisionError:
        print('Деление на ноль невозможно!')


my_div(int(input('Введите делимое: ')), int(input('Введите делитель: ')))
