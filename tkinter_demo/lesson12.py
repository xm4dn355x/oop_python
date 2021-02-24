# -*- coding: utf-8 -*-
########################################################################
#                                                                      #
# Text, Scrollbar                                                      #
#                                                                      #
# MIT License                                                          #
# Copyright (c) 2021 Michael Nikitenko                                 #
#                                                                      #
########################################################################


from tkinter import Tk, Label, Frame, LabelFrame, Button, Text, Scrollbar

COLOR_OVERLAY_LIGHT = '#383B40'  # active clicked button
COLOR_OVERLAY_DARK = '#2D2F34'  # foreground element
COLOR_SURFACE = '#27292D'  # button, label or some other element
COLOR_BASE = '#1F2023'  # Base element background
COLOR_OVERFLOW = '#010101'  # all app background

COLOR_TEXT = '#FFFFFF'  # Text color

ROOT_WINDOW_WIDTH = 500
ROOT_WINDOW_HEIGHT = 400
ROOT_WONDOW_POS_X = 500
ROOT_WINDOW_POS_Y = 500

root = Tk()
root.title('Hello GUI World!')
root.iconbitmap('Python.ico')
root.geometry(f'{ROOT_WINDOW_WIDTH}x{ROOT_WINDOW_HEIGHT}+{ROOT_WONDOW_POS_X}+{ROOT_WINDOW_POS_Y}')
root.resizable(width=False, height=True)
root.config(bg=COLOR_OVERFLOW)


class TemplateLabel(Label):
    def __init__(self, master, text):
        super(TemplateLabel, self).__init__(
            master=master,
            text=text,
            bg=COLOR_SURFACE,
            fg=COLOR_TEXT,
            height=1,
            width=8,
            justify='left',
            anchor='center',
            font=('Helvetica', 20, 'normal'),
            padx=5,
            pady=5
        )


main_frame = LabelFrame(
    master=root,
    text='Тестим Place',
    bg=COLOR_BASE,
    fg=COLOR_TEXT,
    padx=10,
    pady=10
)
main_frame.pack(fill='both', expand=1, padx=10, pady=10)

menu_frame = LabelFrame(
    master=main_frame,
    text='Меню',
    height=90,
    bg=COLOR_BASE,
    fg=COLOR_TEXT,
    padx=10,
    pady=10
)
menu_frame.pack(fill='x')

text_frame = LabelFrame(
    master=main_frame,
    text='Текст',
    bg=COLOR_BASE,
    fg=COLOR_TEXT,
    padx=10,
    pady=10
)
text_frame.pack(fill='both', expand=1)

l1 = TemplateLabel(master=menu_frame, text='Menu')
l1.place(x=0, y=0)

# Работают те же методы как и в Label, но это двумерный массив

text_field = Text(
    master=text_frame,
    bg=COLOR_OVERLAY_LIGHT,
    fg=COLOR_TEXT,
    padx=10,
    pady=10,
    wrap='word',                # Перенос по словам word, перенос по символам char (default)
    insertbackground='red',     # Цвет курсора
    selectbackground='red',     # Цвет выделения текста
    spacing1=0,                 # Отступ в самом начале
    spacing2=0,                 # Отступ между строк
    spacing3=10,                # Отступ между абзацами
    width=49                    # Стандартная ширина строки 80 символов
)
text_field.pack(fill='both', expand=1, side='left')

scroll = Scrollbar(
    master=text_frame,
    command=text_field.yview,
)
scroll.pack(fill='y', side='left')
text_field.config(yscrollcommand=scroll.set)

if __name__ == '__main__':
    root.mainloop()
