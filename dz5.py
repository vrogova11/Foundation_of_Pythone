while True:
    revenue = int(input('Введите размер выручки: '))
    cost = int(input('Введите размер издержек: '))
    if revenue < 0 or cost < 0:
        print('Размер выручки или издержек не может быть меньше 0!')
    else:
        break

if revenue > cost:
    result = 'Прибыль'
elif revenue < cost:
    result = 'Убыток'
else:
    result = 'В ноль'
print(f'Финансовый результат фирмы: {result}')

if result == 'Прибыль':
    rent = (revenue - cost) / revenue
    print(f'Рентабельность выручки {rent}')
    count = int(input('Введите число сотрудников фирмы: '))
    profit = (revenue - cost) / count
    print('Прибыль фирмы в расчете на одного сотрудника: {:.2f}'.format(profit))


