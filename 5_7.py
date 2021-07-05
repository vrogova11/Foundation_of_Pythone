import json
firm_dict = {}
prof_dict = {}
profit = 0
sum_profit = 0
kol_prof = 0
try:
    with open('text_7.txt', 'r', encoding='utf-8') as f_obj:
        for line in f_obj:
            text = line.replace('\n', '').split(' ')
            profit = int(text[2]) - int(text[3])
            firm_dict[text[0]] = profit
        for _ in firm_dict.values():
            if _ > 0:
                kol_prof += 1
                sum_profit += _
        prof_dict['average_profit'] = round(sum_profit / kol_prof)
        print([firm_dict, prof_dict])
except IOError:
    print('Ошибка ввода-вывода!')
try:
    with open('my_file.json', 'w', encoding='utf-8') as write_f:
        json_str = json.dumps([firm_dict, prof_dict], ensure_ascii=False)
        print(json_str, file=write_f)
except IOError:
    print('Ошибка ввода-вывода')
else:
    print('Json-объект создан!')

