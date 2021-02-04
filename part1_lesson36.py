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

    def print_info(self):
        print(f'Hello, my name is {self.name}')


if __name__ == '__main__':
    a = A()
    print(a)
    print(a.property1)
    print(a.say_hi())
    print(a.say_hi(name='Buddy'))
    person = Person(name='Katy')
    person.print_info()
