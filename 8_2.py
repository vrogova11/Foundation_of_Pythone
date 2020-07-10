class My_ZeroDivisionError(Exception):
    def __init__(self, text):
        self.txt = text


num_1 = input('Введите делимое: ')
num_2 = input('Введите делитель: ')

try:
    num_1 = int(num_1)
    num_2 = int(num_2)
    if int(num_2) == 0:
        raise My_ZeroDivisionError('Деление на 0 невозможно!')
except ValueError:
    print('Ошибка ввода')
except My_ZeroDivisionError as err:
    print(err)
else:
    print(round(num_1 / num_2, 2))
