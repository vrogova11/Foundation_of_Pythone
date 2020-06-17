keys_goods = ['Название', 'Цена', 'Количество', 'Ед.']
all_goods = []
count = 0
while True:
    n = int(input('Хотите добавить товар? 1 - Да 0 - Нет: '))
    if n == 1:
        good = []
        dict_one_good = dict()
        count += 1
        for key in keys_goods:
            dict_one_good[key] = (input(f'{key} товара: '))
        good.append(count)
        good.append(dict_one_good)
        good = tuple(good)
        all_goods.append(good)
    elif n == 0:
        print('Товары:')
        for el in all_goods:
            print(el)

        print('Аналитика о товарах: ')
        new_all_goods = []
        new_goods = []
        for key in keys_goods:
            for i, values in enumerate(all_goods):
                new_goods.append(all_goods[i][1].get(key))
            new_goods = list(set(new_goods))
            new_all_goods.append(new_goods)
            new_goods = []

        new_dict = dict(zip(keys_goods, new_all_goods))

        print(new_dict)
        break
    else:
        print('Выберите 1 или 0!')
        continue

