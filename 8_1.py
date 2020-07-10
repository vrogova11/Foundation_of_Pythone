from datetime import date


class Data:

    def __init__(self, data):
        self.data = data

    '''Преобразует дату из строки в число'''

    @classmethod
    def data_num(cls, data):
        try:
            data_num = list(map(int, cls(data).data.split('-')))
        except ValueError:
            print('Неверный формат ввода!')
            exit()
        day, month, year = data_num[0], data_num[1], data_num[2]
        print(f'День - {day}\nМесяц - {month}\nГод - {year}')

    '''Проводит валидацию даты'''

    @staticmethod
    def data_valid():
        data_new = list(map(int, Data(data).data.split('-')))
        day, month, year = data_new[0], data_new[1], data_new[2]
        try:
            date(year, month, day)
        except IndentationError:
            print('Такой даты не существует!')
        except ValueError:
            print('Такой даты не существует!')
        else:
            print('Дата валидна!')


data = input('Введите дату в формате dd-mm-yyyy: ')
# Вызов метода класса через объект
obj = Data(data)
obj.data_num(data)

# Вызов метода класса через класс
print()
Data.data_num(data)

# Вызов статического метода через класс
print()
Data.data_valid()

print(Data.__dict__)
