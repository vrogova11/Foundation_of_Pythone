class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки {self.title}!')


class Pen(Stationery):
    def draw(self):
        print(f'Запуск отрисовки ручкой {self.title}!')


class Pencil(Stationery):
    def draw(self):
        print(f'Запуск отрисовки карандашом {self.title}!')


class Handle(Stationery):
    def draw(self):
        print(f'Запуск отрисовки маркером {self.title}!')


stat = Stationery('Parker Jotter')
stat.draw()

pen = Pen('Parker Jotter')
pen.draw()

pencil = Pencil('Cretacolor')
pencil.draw()

handle = Handle('Finecolor')
handle.draw()