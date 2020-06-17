my_list = [7, 7, 5, 4, 3, 2, 1]
print(f'Стартовый рейтинг: {my_list}')
result_list = [7, 7, 5, 4, 3, 2, 1]
while True:
    result = int(input('Введите результат: '))
    if result <= 0:
        print('Результат может быть >= 1')
        continue
    else:
        break
for i, val in enumerate(my_list):
    if result > val:
        result_list.insert(i, result)
        break
    elif result == 1:
        result_list.append(result)
        break
print(f'Итоговый рейтинг: {result_list}')
