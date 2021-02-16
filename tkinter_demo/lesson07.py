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


def change_color(color: str):
    test_label['bg'] = color
    test_entry.delete(0, 'end')
    test_entry.insert(0, color)


python_png = PhotoImage(file='python-powered-w-200x80.png')

test_image_png = Label(
    master=root,
    image=python_png,
    bg=COLOR_SURFACE,
)
test_image_png.pack()

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
test_label.pack()

test_entry = Entry(
    master=root,
    bg=COLOR_SURFACE,
    fg=COLOR_TEXT,
    width=22,
    justify='left',
    font=('Helvetica', 20, 'normal')
)
test_entry.insert(0, 'Hello')           # Вставляем текст по индексу
test_entry.insert('end', ' World!!')    # Вставляем текст в конец
print(test_entry.get())                 # Достаём текст из поля ввода
test_entry.delete(first=0, last='end')  # Удаляем текст по индексам
test_entry.pack()

# Buttons generator proc style
colors = {
    '#FF0000': 'Красный',
    '#FFFF00': 'Желтый',
    '#00FF00': 'Зелёный',
    '#0000FF': 'Синий',
}

for color_hash, color_name in colors.items():
    Button(
        master=root,
        text=color_name,
        height=1,
        width=20,
        bg=color_hash,
        fg=COLOR_TEXT,
        activebackground=COLOR_OVERLAY_LIGHT,
        activeforeground=COLOR_TEXT,
        font=('Helvetica', 20, 'normal'),
        justify='center',
        command=lambda lambda_hash=color_hash: change_color(lambda_hash)
    ).pack()


if __name__ == '__main__':
    root.mainloop()
