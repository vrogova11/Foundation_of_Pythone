my_str = input('Введите строку из нескольких слов: ')
my_list = []
for i in my_str.split():
    my_list.append(i)

for i, val in enumerate(my_list, 1):
    print(f'{i}) {val[:10]}')
