"""sum_number - текущая сумма чисел"""
sum_number = 0


def my_sum(a):
    """Возвращает сумму чисел, введенных ранее, и чисел, введенных в текущей строке.

    Именованные параметры:
    a -- срока, введенная пользователем

    """
    global sum_number
    new_sum = 0
    for n in a:
        try:
            new_sum += int(n)
        except ValueError:
            print(f'"{n}" не является числом!')
    sum_number += new_sum
    print(f'Текущая сумма чисел: {sum_number}')


while True:
    a = input('Введите строку из чисел, разделенных пробелами!'
              '\nДля завершения программы нажмите "Q", для продолжения "Enter": ').split()
    if a == 'Q':
        break
    elif 'Q' in a:
        a = a[:a.index('Q')]
        my_sum(a)
        break
    else:
        my_sum(a)
        continue
