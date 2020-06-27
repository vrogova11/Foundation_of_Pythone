dict_num = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
try:
    f_obj = open('text_4.txt', 'r', encoding='utf-8')
    for _ in f_obj:
        text = _.split(' ')
        if text[0] in dict_num.keys():
            text[0] = dict_num.get(text[0])
        with open('text_4_1.txt', 'a', encoding='utf-8') as f:
            f.write(' '.join(text))
except IOError:
    print('Файл не найден!')
else:
    print('OK')
finally:
    f_obj.close()



