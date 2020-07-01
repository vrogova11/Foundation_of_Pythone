from random import choice


class Car:

    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Машина {self.name} цвет {self.color} поехала!')

    def stop(self):
        print(f'Машина {self.name} цвет {self.color} остановилась!')

    def turn(self):
        turn = choice(['направо', 'налево'])
        print(f'Машина {self.name} цвет {self.color} повернула {turn}!')

    def show_speed(self):
        print(f'Машина {self.name} цвет {self.color} движется со скоростью {self.speed} км/ч!')


class TownCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)
        print(f'Это машина {self.name} цвет {self.color} класc Town!')

    def show_speed(self):
        print(f'Машина {self.name} цвет {self.color} движется со скоростью {self.speed} км/ч!')
        if int(self.speed) > 60:
            print('Превышение скоростного режима!')


class SportCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)
        print(f'Это машина {self.name} цвет {self.color} класc Sport!')


class WorkCar(Car):

    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)
        print(f'Это машина {self.name} цвет {self.color} класc Work!')

    def show_speed(self):
        print(f'Машина {self.name} цвет {self.color} движется со скоростью {self.speed} км/ч!')
        if int(self.speed) > 40:
            print('Превышение скоростного режима!')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)
        print(f'Это полицейская машина {self.name} цвет {self.color}!')


car = Car('50', 'blue', 'Wolksvagen')
car.go()
car.show_speed()
car.turn()
car.stop()
print()
town_car = TownCar('40', 'white', 'Mazda')
town_car.go()
town_car.show_speed()
town_car.turn()
town_car.stop()
print()
sport_car = SportCar('150', 'yellow', 'Ferrari')
sport_car.go()
sport_car.show_speed()
sport_car.turn()
sport_car.stop()
print()
work_car = WorkCar('60', 'white', 'Mercedes')
work_car.go()
work_car.show_speed()
work_car.turn()
work_car.stop()
print()
work_car = PoliceCar('70', 'grey', 'Ford')
work_car.go()
work_car.show_speed()
work_car.turn()
work_car.stop()
print()
