# -*- coding: utf-8 -*-
########################################################################
#                                                                      #
# Grid. Табличная вёрстка                                              #
#                                                                      #
# MIT License                                                          #
# Copyright (c) 2021 Michael Nikitenko                                 #
#                                                                      #
########################################################################


from tkinter import Tk, Label, Frame, LabelFrame, Button

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
root.config(bg=COLOR_BASE)


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
    text='Тестим Гриды',
    bg=COLOR_BASE,
    fg=COLOR_TEXT,
    padx=10,
    pady=10
)
main_frame.pack(fill='both', expand=1, padx=10, pady=10)


# column, row           Столбец строка (ну как везде)
# columnspan, rowspan   Объединение ячеек
# ipadx ipady           отступы внутри
# padx pady             отступы снаружи
# sticky                Где содержимое должно находиться n e s w ne nw se sw


def mapper(row, col, colspan):
    return {'row': row, 'col': col, 'colspan': colspan}


rows = [(lambda x: x // 3)(i) for i in range(9, -1, -1)]
cols = [0] + [(lambda x: x)(j) for i in range(0, 3) for j in range(0, 3)]
colspans = [3] + [(lambda x: 1)(i) for i in range(0, 9)]
labels_list = list(map(mapper, rows, cols, colspans))


for index, data in enumerate(labels_list):
    TemplateLabel(master=main_frame, text=str(index)).grid(row=data['row'], column=data['col'],
                                                           columnspan=data['colspan'])


if __name__ == '__main__':
    root.mainloop()
