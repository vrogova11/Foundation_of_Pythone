max_n = 0

while True:
    n = int(input('Введите число: '))
    if n > 0:
        while n // 10 != 0:
            if n % 10 == 9:
                max_n = 9
                break
            elif n % 10 > max_n:
                max_n = n % 10
            n = n // 10
            # print(n)
            continue
        print(f'Самая большая цифра: {max_n}')
        break
    elif n < 0:
        print('Число должно быть больше 0!')
        continue
    else:
        print('Число не должно быть равно 0!')
