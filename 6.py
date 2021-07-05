def int_fun(text):
    return text.title()


while True:
    ex = 0
    text = list(input('Введите слово из маленьких латинских букв: '))
    for t in text:
        if 97 <= ord(t) <= 122:
            continue
        else:
            print('Слово не соответствует заданным требованиям!')
            ex = 1
            break
    if ex == 0:
        print(int_fun(''.join(text)))
        break
    else:
        continue



