from abc import ABC, abstractmethod


class Clothes(ABC):

    @abstractmethod
    def cloth(self):
        pass


class Coat(Clothes):
    def __init__(self, v):
        self.v = v

    @property
    def v(self):
        return self.__v

    @v.setter
    def v(self, v):
        if v < 40:
            self.__v = 40
        elif v > 58:
            self.__v = 58
        else:
            self.__v = v

    @property
    def cloth(self):
        return round(self.__v / 6.5 + 0.5, 1)


class Suit(Clothes):
    def __init__(self, h):
        self.h = h

    @property
    def h(self):
        return self.__h

    @h.setter
    def h(self, h):
        if h < 130:
            self.__h = 130
        elif h > 180:
            self.__h = 180
        else:
            self.__h = h

    @property
    def cloth(self):
        return round(2 * self.h + 0.3, 1)


coat = Coat(60)
print(f'Расход ткани на пальто: {coat.cloth}')
suit = Suit(185)
print(f'Расход ткани на костюм: {suit.cloth}')
print(f'Общий расход ткани: {coat.cloth + suit.cloth}')

