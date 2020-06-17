text = input('Введите значения списка через пробел: ')
my_list = []
for i in text.split():
    my_list.append(i)

print(my_list)
print(type(my_list))

new_list = []
result_list = []

for i, el in enumerate(my_list, 1):
    if i == len(my_list) and i % 2 !=0:
        result_list.append(el)
    else:
        new_list.append(el)
        if i % 2 == 0:
            new_list.reverse()
            result_list += new_list
            new_list = []
print(result_list)
