class Road:

    def __init__(self, _lenght, _width):
        self._lenght = _lenght
        self._width = _width

    def my_weight(self):
        weight = round(self._lenght * self._width * 25 * 5 / 1000)
        print(f'Масса асфальта равна: {weight} т')


road_1 = Road(int(input('Введите длину полотна: ')), int(input('Введите ширину полотна: ')))
road_1.my_weight()
