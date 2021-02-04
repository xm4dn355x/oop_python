# -*- coding: utf-8 -*-
########################################################################
#                                                                      #
# Часть 1. Урок 36 Основы ООП. Класс и объект                          #
#                                                                      #
# MIT License                                                          #
# Copyright (c) 2021 Michael Nikitenko                                 #
#                                                                      #
########################################################################


class A:
    property1 = 'Property 1'
    name = 'Stranger'

    def say_hi(self, name=''):
        if name:
            return f'Hi {name}'
        else:
            return f'Hi {self.name}'


class Person:
    anal = True

    def __init__(self, name: str):
        self.name = name
        self._age = 20      # "Защищенное" свойство. Не надо трогать.
        self.__tits = 3     # "Приватное" свойство. Питон защищает и не даёт его печатать и редактировать напрямую

    def print_info(self):
        print(f'Hello, my name is {self.name}, Age: {self._age}')

    @property
    def tits(self):
        return self.__tits

    @tits.setter
    def tits(self, size: int):
        if size in range(1, 5):
            self.__tits = size
        else:
            print('Wrong tits size')

if __name__ == '__main__':
    a = A()
    print(a)
    print(a.property1)
    print(a.say_hi())
    print(a.say_hi(name='Buddy'))
    person = Person(name='Katy')
    person.print_info()
    print(person._Person__tits)     # Достучались до приватного свойства
    print(person.tits)
    person.tits = -1
    person.tits = 0
    person.tits = 2
    person.tits = 6
    print(person.tits)
