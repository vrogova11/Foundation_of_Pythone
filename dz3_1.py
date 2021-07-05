winter = [12, 1, 2]
spring = [3, 4, 5]
summer = [6, 7, 8]
autumn = [9, 10, 11]

while True:
    month = int(input('Введите месяц: '))
    if 1 <= month <= 12:
        if month in winter:
            result = 'Зима'
        elif month in spring:
            result = 'Весна'
        elif month in summer:
            result = 'Лето'
        elif month in autumn:
            result = 'Осень'
        break
    else:
        print('Номер месяца может быть от 1 до 12!')

print(f'{month}-й месяц относится к времени года - {result}')
