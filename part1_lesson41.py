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

    def __str__(self):
        return f'<{self.__class__.__name__}> Name: {self.name}, Age: {self.age}'

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

    def __init__(self, name: str, age: int, company: str):
        super().__init__(name=name, age=age)
        self.company = company

    def __str__(self):
        return super().__str__() + f', Company: {self.company}'


if __name__ == '__main__':
    mike = Employee(name='Mike', age=27, company='SC')
    print(mike)
    some_person = Person(name='Sergo', age=28)
    print(some_person)
