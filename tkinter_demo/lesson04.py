# -*- coding: utf-8 -*-
########################################################################
#                                                                      #
#                                                                      #
#                                                                      #
# MIT License                                                          #
# Copyright (c) 2021 Michael Nikitenko                                 #
#                                                                      #
########################################################################


from tkinter import Tk, Label, PhotoImage


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


test_label = Label(
    master=root,
    text='Test\nText2dfgdfgdfg\nText3dfgdfgdfgdgdfdfg',
    bg=COLOR_SURFACE,
    fg=COLOR_TEXT,
    height=4,
    width=20,
    justify='left',
    anchor='w',  # Позиционирование текста в контейнере n, ne, e, se, s, sw, w, nw, center
    font=('Helvetica', 20, 'normal')
)
test_label.pack()

python_png = PhotoImage(file='python-powered-w-200x80.png')

test_image_png = Label(
    master=root,
    image=python_png,
    bg=COLOR_SURFACE,
)
test_image_png.pack()


if __name__ == '__main__':
    root.mainloop()
