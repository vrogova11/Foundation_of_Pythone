class Worker:

    def __init__(self):
        self.name = input('Имя сотрудника: ')
        self.surname = input('Фамилия сотрудника: ')
        self.position = input('Должность сотрудника: ')
        self._income = {"wage": int(input('Оклад: ')), "bonus": int(input('Бонус: '))}


class Position(Worker):

    def get_full_name(self):
        print(f'Полное имя сотрудника: {self.name} {self.surname}')

    def get_total_income(self):
        print(f'Доход с учетом премии: {sum(self._income.values())}')


while True:
    chose = input('Добавить данные сотрудника? Да - 1 Нет - 0 ')
    if chose == '1':
        pos_worker = Position()
        pos_worker.get_full_name()
        pos_worker.get_total_income()
    elif chose == '0':
        break
    else:
        print('Повторите выбор!')
