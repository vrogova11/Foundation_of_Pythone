my_list = [1, 34.23, 'text', False, ['n1', 'n2'], (3, 4, 5), {1,2,3}, {1: 'One', 2: 'Two'}]
for i, value in enumerate(my_list, 1):
    print(f'{i}-й элемент = {value}. Тип элемента - {type(value)}')