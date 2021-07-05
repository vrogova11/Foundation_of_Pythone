def my_func(x, y):
    # return x ** y
    result = x
    for n in range(1, abs(y)):
        result *= x
    return 1 / result


while True:
    try:
        print(my_func(int(input('Введите действительное положительное число x: ')),
                      int(input('Введите целое отрицательное число у: '))))
        break
    except ValueError:
        print('Значения x и y не соответствуют заданному формату!')
        continue
