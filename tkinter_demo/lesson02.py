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


COLOR_OVERLAY_LIGHT = '#383B40'
COLOR_OVERLAY_DARK = '#2D2F34'
COLOR_SURFACE = '#27292D'
COLOR_BASE = '#1F2023'
COLOR_OVERFLOW = '#010101'
COLOR_TEXT = '#FFFFFF'

ROOT_WINDOW_WIDTH = 500
ROOT_WINDOW_HEIGHT = 300
ROOT_WONDOW_POS_X = 500
ROOT_WINDOW_POS_Y = 500


root = Tk()
root.title('Hello GUI World!')
root.iconbitmap('Python.ico')
root.geometry(f'{ROOT_WINDOW_WIDTH}x{ROOT_WINDOW_HEIGHT}+{ROOT_WONDOW_POS_X}+{ROOT_WINDOW_POS_Y}')
root.resizable(width=False, height=True)
root.config(bg=COLOR_OVERFLOW)

def some_command():
    print('button clicked')

test_button = Button(
    master=root,
    text='Кнопка\n#1',
    height=1,   # В знакоместах
    width=60,    # В знакоместах
    bg=COLOR_SURFACE,
    fg=COLOR_TEXT,
    activebackground=COLOR_OVERLAY_LIGHT,
    activeforeground=COLOR_TEXT,
    font=('Comic Sans MS', 20, 'italic'),
    justify='center',     # left center right Выравнивание текста кнопки внутри контейнера текста кнопки
    command=some_command
)
test_button['font'] = ('Times', 20, 'normal')
# test_button = ttk.Button(master=root, text='Виндовая кнопка', command=some_command) # Кнопка в стиле ОС
test_button.pack()

if __name__ == '__main__':
    root.mainloop()
