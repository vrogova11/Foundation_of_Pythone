day = 1

while True:
    result = int(input('Введите результат пробежки в первый день: '))
    if result > 0:
        purpose = int(input('Введите желаемый результат: '))
        if result >= purpose:
            print('Желаемый результат не может быть меньше или равен достигнутому!')
            continue
        else:
            break
    else:
        print('Результат пробежки не может быть меньше или равен 0!')

print('Результат: ')

while True:
    print('{}-й день: {:.2f}'.format(day, result))
    if result <= purpose:
        result *= 1.1
        day += 1
    else:
        break

print(f'Ответ: на {day}-й день спортсмен достигнет результата — не менее {purpose} км.')
