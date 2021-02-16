# -*- coding: utf-8 -*-
########################################################################
#                                                                      #
# TKinter first demo lesson                                            #
#                                                                      #
# MIT License                                                          #
# Copyright (c) 2021 Michael Nikitenko                                 #
#                                                                      #
########################################################################
# Overlay Light #383B40
# Overlay Dark  #2D2F34
# Surface       #27292D
# Base          #1F2023     base element backgroung
# Overflow      #010101     all app background

# Text
# color         #FFFFFF
# opacity       65%
# contrast      7.02:1

from tkinter import Tk


root = Tk()
root.title('Hello GUI World!')
root.iconbitmap('Python.ico')
root.geometry('500x300+500+500')
root.resizable(width=False, height=True)
root.config(bg='#010101')


if __name__ == '__main__':
    root.mainloop()
