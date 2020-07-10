class Complex_number:
    def __init__(self, num):
        self.num = num
        self.a = int(self.num.real)
        self.b = int(self.num.imag)

    def __add__(self, other):
        if self.b + other.b > 0:
            return f'{self.a + other.a}+{self.b + other.b}i'
        elif self.b + other.b < 0:
            return f'{self.a + other.a}{self.b + other.b}i'
        elif self.a + other.a == 0 and self.b + other.b == 0:
            return '0'
        elif self.a + other.a == 0:
            return f'{self.b + other.b}i'
        elif self.b + other.b == 0:
            return f'{self.a + other.a}'

    def __mul__(self, other):
        if self.a * other.b + other.a * self.b > 0:
            return f'{self.a * other.a - self.b * other.b}+{self.a * other.b + other.a * self.b}i'
        elif self.a * other.b + other.a * self.b < 0:
            return f'{self.a * other.a - self.b * other.b}{self.a * other.b + other.a * self.b}i'


n_1 = Complex_number(2 + 3j)
n_2 = Complex_number(4 - 10j)
print(n_1 + n_2)
print(n_1 * n_2)