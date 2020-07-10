from abc import ABC, abstractmethod


class Storehouse:
    bd_eqip = []
    bd_dep = []

    @classmethod
    def get_eqip(cls, *eqip):
        for eq in eqip:
            dict_eqip = {}
            dict_eqip['Устройство'] = eq.eqipm
            dict_eqip['Производитель'] = eq.manufacturer
            dict_eqip['Наименование'] = eq.title
            dict_eqip['Оптовая цена'] = eq.sale_price
            dict_eqip['Розничная цена'] = eq.retail_price
            dict_eqip['Количество'] = eq.kol
            Storehouse.bd_eqip.append(dict_eqip)
            print(f'На склад поступил {eq.eqipm} {eq.title} в количестве {eq.kol} шт.')

    def get_department(department, eqip, kol):
        dep = list(eqip.send_department(department))
        Storehouse.bd_dep.append({dep[0]: dep[1]})
        print(f'Устройство {dep[0]} в количестве {kol} шт. передано в отдел {dep[1]}')


class My_ABC(ABC):

    @abstractmethod
    def profit_eqipm(self):
        pass


class Office_eqip(My_ABC):
    def __init__(self, eqipm=None, manufacturer=None, title=None, sale_price=None, retail_price=None, kol=None):
        self.eqipm = eqipm
        self.manufacturer = manufacturer
        self.title = title
        self.sale_price = sale_price
        self.kol = kol
        self.retail_price = retail_price

    @staticmethod
    def profit_eqipm(*eqip):
        profit = 0
        for eq in eqip:
            profit += eq.profit_eqipm
        print(f'Прибыль на оборудование составит: {int(profit)} руб.')


class Printer(Office_eqip):
    department = None

    def __init__(self, manufacturer, title, sale_price, retail_price, kol, print_technology, eqipm='принтер'):
        super().__init__(eqipm, manufacturer, title, sale_price, retail_price, kol)
        self.print_technology = print_technology

    @property
    def profit_eqipm(self):
        profit = (self.retail_price - self.sale_price) * 1.06
        return int(profit)

    def send_department(self, department):
        self.department = department
        return self.title, self.department


class Scaner(Office_eqip):
    department = None

    def __init__(self, manufacturer, title, sale_price, retail_price, kol, scan_technology, auto_doc=False,
                 eqipm='сканер'):
        super().__init__(eqipm, manufacturer, title, sale_price, retail_price, kol)
        self.scan_technology = scan_technology
        self.auto_doc = auto_doc

    @property
    def profit_eqipm(self):
        profit = (self.retail_price - self.sale_price) * 1.03
        return int(profit)

    def send_department(self, department):
        self.department = department
        return self.title, self.department


class Copy_machine(Office_eqip):
    def __init__(self, manufacturer, title, sale_price, retail_price, kol, copy_speed, eqipm='ксерокс'):
        super().__init__(eqipm, manufacturer, title, sale_price, retail_price, kol)
        self.copy_speed = copy_speed

    @property
    def profit_eqipm(self):
        profit = (self.retail_price - self.sale_price) * 1.05
        return int(profit)

pr = 0
sc = 0
cp = 0

manuf = input('Введите производителя принтера: ')
title = input('Введите название принтера: ')
s_price = None
while not s_price:
    try:
        s_price = int(input('Ведите оптовую цену: '))
    except ValueError:
        print('Ошибка ввода!')
r_price = None
while not r_price:
    try:
        r_price = int(input('Ведите розничную цену: '))
    except ValueError:
        print('Ошибка ввода!')
kol = None
while not kol:
    try:
        kol = int(input('Ведите количество: '))
    except ValueError:
        print('Ошибка ввода!')
type = input('Введите тип печати: ')
pr = Printer(manuf, title, s_price, r_price, kol, type)

pr_1 = Printer('Canon', 'Canon Pixma TC304', 2500, 3500, 24, 'струйный')
pr_2 = Printer('Samsung', 'Samsung 4200', 9500, 10800, 18, 'лазерный')
sc_1 = Scaner('EPSON', 'EPSON Perfection V19', 4500, 5600, 12, 'CIS')
cop_1 = Copy_machine('Xerox', 'Xerox B215', 17000, 18000, 10, '30/min')
Storehouse.get_eqip(pr, pr_1, pr_2, sc_1, cop_1)
for eqip in Storehouse.bd_eqip:
    print(eqip)
Storehouse.get_department('Продажи', pr_1, 3)
Storehouse.get_department('Сбыта', sc_1, 5)
for dep in Storehouse.bd_dep:
    print(dep)
Office_eqip.profit_eqipm(pr, pr_1, pr_2, sc_1, cop_1)
