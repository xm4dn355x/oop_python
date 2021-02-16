# -*- coding: utf-8 -*-
########################################################################
#                                                                      #
#                                                                      #
#                                                                      #
# MIT License                                                          #
# Copyright (c) 2021 Michael Nikitenko                                 #
#                                                                      #
########################################################################


from tkinter import Tk, Button, Label, PhotoImage, Entry

COLOR_OVERLAY_LIGHT = '#383B40'     # active clicked button
COLOR_OVERLAY_DARK = '#2D2F34'      # foreground element
COLOR_SURFACE = '#27292D'           # button, label or some other element
COLOR_BASE = '#1F2023'              # Base element background
COLOR_OVERFLOW = '#010101'          # all app background
COLOR_TEXT = '#FFFFFF'              # Text color

ROOT_WINDOW_WIDTH = 500
ROOT_WINDOW_HEIGHT = 400
ROOT_WONDOW_POS_X = 500
ROOT_WINDOW_POS_Y = 500


root = Tk()
root.title('Hello GUI World!')
root.iconbitmap('Python.ico')
root.geometry(f'{ROOT_WINDOW_WIDTH}x{ROOT_WINDOW_HEIGHT}+{ROOT_WONDOW_POS_X}+{ROOT_WINDOW_POS_Y}')
root.resizable(width=False, height=True)
root.config(bg=COLOR_BASE)


python_png = PhotoImage(file='python-powered-w-200x80.png')

test_image_png = Label(
    master=root,
    image=python_png,
    bg=COLOR_SURFACE,
)

test_label = Label(
    master=root,
    text='Введите сообщение: ',
    bg=COLOR_SURFACE,
    fg=COLOR_TEXT,
    height=1,
    width=20,
    justify='left',
    anchor='center',
    font=('Helvetica', 20, 'normal')
)

test_entry = Entry(
    master=root,
    bg=COLOR_SURFACE,
    fg=COLOR_TEXT,
    width=22,
    justify='left',
    font=('Helvetica', 20, 'normal')
)
test_entry.insert(0, 'Цвет')


# Buttons generator OOP style
class ColorsButtons():
    """Класс для генерации кнопки меняющей цвета"""
    __height = 1
    __width = 20
    __fg = COLOR_TEXT
    __activebackground = COLOR_OVERLAY_LIGHT
    __activeforeground = COLOR_TEXT
    __font = ('Helvetica', 20, 'normal')
    __justify = 'center'

    def __init__(self, master: object, color_name: str, color_hex: str):
        self.master = master
        self.text = color_name
        self.bg = color_hex
        self.button = Button(
            master=self.master,
            text=self.text,
            height=self.__height,
            width=self.__width,
            bg=self.bg,
            fg=self.__fg,
            activebackground=self.__activebackground,
            activeforeground=self.__activeforeground,
            font=self.__font,
            justify=self.__justify,
            command=self.change_color
        )
        self.button.pack()

    def change_color(self):
        test_label['text'] = self.text
        test_label['bg'] = self.bg
        test_entry.delete(0, 'end')
        test_entry.insert(0, self.bg)


colors = {
    '#FF0000': 'Красный',
    '#FFFF00': 'Желтый',
    '#00FF00': 'Зелёный',
    '#0000FF': 'Синий',
}

# Packing of objects
test_image_png.pack()
test_label.pack()
test_entry.pack()

for color_hex, color_name in colors.items():
    ColorsButtons(master=root, color_name=color_name, color_hex=color_hex)

if __name__ == '__main__':
    root.mainloop()
