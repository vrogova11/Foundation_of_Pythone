from sys import argv

script_name, hours, rate, bonus = argv


def my_salary():
    global hours, rate, bonus
    try:
        hours = int(hours)
        rate = round(float(rate), 1)
        bonus = round(float(bonus), 1)
    except ValueError:
        return 'Ошибка ввода! Не числовое значение аргументов!'
    if hours < 0 or rate < 0 or bonus < 0:
        return 'Аргументы не могут быть меньше 0'
    return round(hours * rate + bonus, 1)


print(f'Заработная плата сотрудника составила: {my_salary()}')





