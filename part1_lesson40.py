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


if __name__ == '__main__':
    employee = Employee('John', 27)
    employee.print_info()
    print(employee.tits)
