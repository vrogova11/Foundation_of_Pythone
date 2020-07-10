class Ceil:
    def __init__(self, kol):
        self.kol = kol

    def __str__(self):
        pass

    def __add__(self, other):
        return self.kol + other.kol

    def __sub__(self, other):
        return self.kol - other.kol if self.kol - other.kol >= 0 else other.kol - self.kol

    def __mul__(self, other):
        return self.kol * other.kol

    def __truediv__(self, other):
        try:
            d = self.kol // other.kol
            return d
        except ZeroDivisionError:
            return 'Деление на ноль невозможно!'

    def make_order(self, dig):
        return ''.join('*' * dig + '\n' for i in range(list(divmod(self.kol, dig))[0])) + '*' * list(divmod(self.kol, dig))[1]


ceil_1 = Ceil(56)
ceil_2 = Ceil(11)
print(ceil_1 + ceil_2)
print(ceil_1 - ceil_2)
print(ceil_1 * ceil_2)
print(ceil_1 / ceil_2)
print(ceil_1.make_order(10))