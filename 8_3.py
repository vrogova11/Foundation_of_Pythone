class Not_number_err(Exception):
    def __init__(self, text):
        self.text = text

list_num = []

while True:
    a = input('Введите число!'
              '\nДля завершения программы нажмите "Q", для продолжения "Enter": ')
    if a == 'Q':
        print(f'Сформированный список чисел: {list_num}')
        break
    else:
        try:
            if not a.lstrip('-').isdigit():
                raise Not_number_err('Вы ввели не число!')
        except Not_number_err as err:
            print(err)
        else:
            list_num.append(int(a))

