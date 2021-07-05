def my_func(n_1, n_2, n_3):
    return sum([n_1, n_2, n_3]) - min([n_1, n_2, n_3])


print('Сумма наибольших аргументов = ', my_func(int(input('Введите первое число: ')),
                                                int(input('Введите второе число: ')),
                                                int(input('Введите третье число: '))))
