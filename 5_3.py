try:
    f_obj = open('text_3.txt', 'r', encoding='utf-8')
    count = 0
    sal = 0
    for i in f_obj:
        count += 1
        text = i.replace('\n', '')
        text = text.split(' ')
        sal += float(text[1])
        if float(text[1]) < 20000:
            print(text[0])
    f_obj.close()
    print(f'Средний доход сотрудников: {sal / count}')
except IOError:
    print('Файл не найден!')




