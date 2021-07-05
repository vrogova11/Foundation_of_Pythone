text = 'some_text'
f_obj = open('text.txt', 'a+', encoding='utf-8')
while text != '':
    text = input('Введите строку:')
    f_obj.write(text)
    f_obj.write('\n')

print('Файл записан!\n')
f_obj.seek(0)

text_list = f_obj.readlines()
for kol_str, kol_word in enumerate(text_list, 1):
    kol_word = kol_word.split(' ')
    if '\n' in kol_word:
        kol_word.remove('\n')
    print(f'{kol_str}-я строка содержит {len(kol_word)} слов(а).')

f_obj.close()









