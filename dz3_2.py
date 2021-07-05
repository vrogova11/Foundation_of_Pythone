dict_months = {'Зима': [12, 1, 2], 'Весна': [3, 4, 5], 'Лето': [6, 7, 8], 'Осень': [9, 10, 11]}

while True:
    month = int(input('Введите месяц: '))
    if 1 <= month <= 12:
        for i in dict_months:
            if month in dict_months[i]:
                result = i
        break
    else:
        print('Номер месяца может быть от 1 до 12!')

print(f'{month}-й месяц относится к времени года - {result}')