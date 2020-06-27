dict_key = []
dict_val = []
sum_val = 0
try:
    with open('text_6.txt', 'r', encoding='utf-8') as f_obj:
        for _ in f_obj:
            text = _.replace('\n', '')
            text = text.split(' ')
            dict_key.append(text[0])
            for el in text[1:]:
                if el != '-':
                    el = el.replace('(л)', '')
                    el = el.replace('(пр)', '')
                    el = el.replace('(лаб)', '')
                else:
                    el = 0
                sum_val += int(el)
            dict_val.append(sum_val)
            sum_val = 0
except IOError:
    print('Файл не найден!')

dict_all = dict(zip(dict_key, dict_val))
print(dict_all)
