time = int(input('Введите время в секундах: '))
hours = int(time / 3600)
minutes = int(time % 3600 / 60)
seconds = time % 3600 % 60
print('Точное время: {:>02d}:{:>02d}:{:>02d}'.format(hours, minutes, seconds))





