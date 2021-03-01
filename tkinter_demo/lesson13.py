# -*- coding: utf-8 -*-
########################################################################
#                                                                      #
# Menu                                                                 #
#                                                                      #
# MIT License                                                          #
# Copyright (c) 2021 Michael Nikitenko                                 #
#                                                                      #
########################################################################


from tkinter import Tk, Label, Frame, LabelFrame, Button, Text, Scrollbar, Menu
from dark_theme_colors import COLOR_TEXT, COLOR_BASE, COLOR_OVERFLOW, COLOR_OVERLAY_LIGHT, COLOR_OVERLAY_DARK, \
    COLOR_SURFACE


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


# Menu
main_menu = Menu(master=root, bg=COLOR_BASE, fg=COLOR_TEXT)
root.config(menu=main_menu)
# File
menu_file = Menu(master=main_menu, tearoff=0, bg=COLOR_BASE, fg=COLOR_TEXT)
menu_file.add_command(label='Открыть')
menu_file.add_command(label='Сохранить')
menu_file.add_command(label='Закрыть')
menu_file.add_separator()
menu_file.add_command(label='Выйти', command=root.quit)
# Edit
menu_edit = Menu(master=main_menu, tearoff=0, bg=COLOR_BASE, fg=COLOR_TEXT)
menu_edit.add_command(label='Отменить')
menu_edit.add_command(label='Повторить')
menu_edit.add_separator()
# Edit -> навести суету
menu_sueta = Menu(master=menu_edit, tearoff=0, bg=COLOR_BASE, fg=COLOR_TEXT)
menu_sueta.add_command(label='Сделать лево-право')
menu_edit.add_cascade(label='Навести суету', menu=menu_sueta)
main_menu.add_cascade(label='Файл', menu=menu_file)
main_menu.add_cascade(label='Правка', menu=menu_edit)
main_menu.add_command(label='О программе')


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
    text='Суетология',
    bg=COLOR_BASE,
    fg=COLOR_TEXT,
    padx=10,
    pady=10
)
main_frame.pack(fill='both', expand=1, padx=10, pady=10)



if __name__ == '__main__':
    root.mainloop()
