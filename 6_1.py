def int_fun(text):
    return text.title()


while True:
    ex = 0
    new_words = []
    words = input('Введите строку из слов, состоящих из маленьких латинских букв: ').split()
    for word in words:
        for t in word:
            if 97 <= ord(t) <= 122:
                continue
            else:
                print('Строка не соответствует заданным требованиям!')
                ex = 1
                break
        if ex == 0:
            new_words.append(int_fun(''.join(word)))
            continue
        else:
            break
    if ex != 0:
        continue
    else:
        print(' '.join(new_words))
        break





