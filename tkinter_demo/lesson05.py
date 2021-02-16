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


def add_str():
    test_entry.insert('end', 'Hello!')


def del_str():
    test_entry.delete(0, 'end')


def get_str():
    test_label['text'] = test_entry.get()


def show_str():
    if test_entry['show'] == '*':
        test_entry['show'] = ''
    else:
        test_entry['show'] = '*'


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
    show='*',                           # Можно сделать секретный ввод
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

add_button = Button(
    master=root,
    text='Добавить текст',
    height=1,
    width=20,
    bg=COLOR_SURFACE,
    fg=COLOR_TEXT,
    activebackground=COLOR_OVERLAY_LIGHT,
    activeforeground=COLOR_TEXT,
    font=('Helvetica', 20, 'normal'),
    justify='center',
    command=add_str
)
add_button.pack()

del_button = Button(
    master=root,
    text='Удалить текст',
    height=1,
    width=20,
    bg=COLOR_SURFACE,
    fg=COLOR_TEXT,
    activebackground=COLOR_OVERLAY_LIGHT,
    activeforeground=COLOR_TEXT,
    font=('Helvetica', 20, 'normal'),
    justify='center',
    command=del_str
)
del_button.pack()

get_button = Button(
    master=root,
    text='Прочитать текст',
    height=1,
    width=20,
    bg=COLOR_SURFACE,
    fg=COLOR_TEXT,
    activebackground=COLOR_OVERLAY_LIGHT,
    activeforeground=COLOR_TEXT,
    font=('Helvetica', 20, 'normal'),
    justify='center',
    command=get_str
)
get_button.pack()

show_button = Button(
    master=root,
    text='Показать текст',
    height=1,
    width=20,
    bg=COLOR_SURFACE,
    fg=COLOR_TEXT,
    activebackground=COLOR_OVERLAY_LIGHT,
    activeforeground=COLOR_TEXT,
    font=('Helvetica', 20, 'normal'),
    justify='center',
    command=show_str
)
show_button.pack()

if __name__ == '__main__':
    root.mainloop()
