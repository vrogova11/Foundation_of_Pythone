def fact(number):
    com = 1
    list_com = []
    if number == 0:
        list_com = [1]
    else:
        for _ in range(1, number + 1):
            com *= _
            list_com.append(com)
    for _ in list_com:
        yield _


while True:
    try:
        n = int(input('Введите число n: '))
    except ValueError:
        print('n должно быть целочисленным!')
        continue
    if n < 0:
        print('n не может быть меньше 0!')
        continue
    else:
        break

for el in fact(n):
    print(el)
