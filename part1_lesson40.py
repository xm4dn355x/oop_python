# -*- coding: utf-8 -*-
########################################################################
#                                                                      #
#                                                                      #
#                                                                      #
# MIT License                                                          #
# Copyright (c) 2021 Michael Nikitenko                                 #
#                                                                      #
########################################################################


class Person:
    anal = True

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age     # "Защищенное" свойство. Не надо трогать.
        self.__tits = 3     # "Приватное" свойство. Питон защищает и не даёт его печатать и редактировать напрямую

    def print_info(self):
        print(f'Hello, my name is {self.name}, Age: {self.age}')

    @property
    def tits(self):
        return self.__tits

    @tits.setter
    def tits(self, size: int):
        if size in range(1, 5):
            self.__tits = size
        else:
            print('Wrong tits size')


class Employee(Person):
    company = 'SC'

    # def __init__(self):
    #     pass

    def more_info(self):
        print(f'{self.name} works in {self.company}')


class Kettle:

    def turn_on(self):
        print('Нажимаем кнопку включения')
        self.__boil()
        self.__check_temp()
        self.__beep()
        self._turn_off()

    def __boil(self):
        print('Разогревание воды')

    def __check_temp(self):
        print('Проверяем температуру воды')

    def __beep(self):
        print('Подаём звуковой сигнал')

    def _turn_off(self):
        print('Отключение')


class Vehicle:

    def __init__(self, name, model, **kwargs):
        self.name = name
        self.model = model
        if 'passengers_max' in kwargs:
            self.passengers_max = kwargs['passengers_max']
        else:
            self.passengers_max = 1


class Car(Vehicle):

    def __init__(self, name, model, **kwargs):
        super().__init__(name, model, **kwargs)
        if 'fwd' in kwargs:
            self.fwd = kwargs['fwd']
        else:
            self.fwd = False


class Plane(Vehicle):

    def __init__(self, name, model, **kwargs):
        super().__init__(name, model, **kwargs)
        if 'max_height' in kwargs:
            self.max_height = kwargs['max_height']
        else:
            self.max_height = False


if __name__ == '__main__':
    employee = Employee('John', 27)
    employee.print_info()
    print(employee.tits)
    audi = Car(name='Audi', model='A3 3.0', passengers_max=5, fwd=True)
    print(audi.__dict__)
    airbus = Plane(name='Airbus', model='A320', passengers_max=300, max_height=10000)
    print(airbus.__dict__)
