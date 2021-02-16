# -*- coding: utf-8 -*-
########################################################################
#                                                                      #
#                                                                      #
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


from tkinter import Tk, Button, ttk, font
import time


COLOR_OVERLAY_LIGHT = '#383B40'     # active clicked button
COLOR_OVERLAY_DARK = '#2D2F34'      # foreground element
COLOR_SURFACE = '#27292D'           # button, label or some other element
COLOR_BASE = '#1F2023'              # Base element background
COLOR_OVERFLOW = '#010101'          # all app background
COLOR_TEXT = '#FFFFFF'              # Text color

ROOT_WINDOW_WIDTH = 500
ROOT_WINDOW_HEIGHT = 300
ROOT_WONDOW_POS_X = 500
ROOT_WINDOW_POS_Y = 500


root = Tk()
root.title('Hello GUI World!')
root.iconbitmap('Python.ico')
root.geometry(f'{ROOT_WINDOW_WIDTH}x{ROOT_WINDOW_HEIGHT}+{ROOT_WONDOW_POS_X}+{ROOT_WINDOW_POS_Y}')
root.resizable(width=False, height=True)
root.config(bg=COLOR_BASE)


def showtime():
    current_time = time.strftime('%H:%M:%S')
    time_button['text'] = current_time


def clicker():
    prev = button_clicker['text']
    try:
        prev = int(prev)
    except ValueError:
        prev = 0
    res = str(prev + 1)
    button_clicker['text'] = res


def turn_back():
    counter = button_clicker['text']
    try:
        counter = int(counter)
    except ValueError:
        counter = 0
    counter = str(counter - 1)
    button_clicker['text'] = counter


time_button = Button(
    master=root,
    text='Который час?',
    height=1,   # В знакоместах
    width=12,   # В знакоместах
    bg=COLOR_SURFACE,
    fg=COLOR_TEXT,
    activebackground=COLOR_OVERLAY_LIGHT,
    activeforeground=COLOR_TEXT,
    font=('Helvetica', 20, 'normal'),
    justify='center',     # left center right Выравнивание текста кнопки внутри контейнера текста кнопки
    command=showtime
)
time_button.pack()

button_clicker = Button(
master=root,
    text='Кликер',
    height=1,   # В знакоместах
    width=12,   # В знакоместах
    bg=COLOR_SURFACE,
    fg=COLOR_TEXT,
    activebackground=COLOR_OVERLAY_LIGHT,
    activeforeground=COLOR_TEXT,
    font=('Helvetica', 20, 'normal'),
    justify='center',     # left center right Выравнивание текста кнопки внутри контейнера текста кнопки
    command=clicker
)
button_clicker.pack()

button_turn_back = Button(
    text='-1',
    height=1,   # В знакоместах
    width=12,   # В знакоместах
    bg=COLOR_SURFACE,
    fg=COLOR_TEXT,
    activebackground=COLOR_OVERLAY_LIGHT,
    activeforeground=COLOR_TEXT,
    font=('Helvetica', 20, 'normal'),
    justify='center',     # left center right Выравнивание текста кнопки внутри контейнера текста кнопки
    command=turn_back
)
button_turn_back.pack()


if __name__ == '__main__':
    root.mainloop()
