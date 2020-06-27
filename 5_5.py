f_obj = open('text5_5.txt', 'w+', encoding='utf-8')
text = input('Введите числа через пробел: ')
f_obj.write(text)
f_obj.seek(0)
text = f_obj.read().split(' ')
for t in text:
    if t == '':
        text.remove(t)
print(sum(map(int, text)))

f_obj.close()
