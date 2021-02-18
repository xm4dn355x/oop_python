# -*- coding: utf-8 -*-
########################################################################
#                                                                      #
# Place.                                                               #
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

# anchor                n e s w ne nw se sw     Относительно какой точки блока считается позиционирование
# x, y                  int pixels              В какую конкретную координату контейнера устанавливается элемент
# relx, rely            float 0.0-1.0           Куда устанавливается элемент относительно родительского контейнера в %
# bordermode            inside outside          Границы контейнера (хз вообще)
# height, width         int pixels              Высота и ширина в пикселях
# relheight relwidth    float 0.0-1.0           Высота элемента относительно родительского контейнера в процентах

l1 = TemplateLabel(master=main_frame, text='Test1')
l1.place(x=0, y=0, anchor='nw')

l2 = TemplateLabel(master=main_frame, text='Test2')
l2.place(relx=0.5, rely=0.5, anchor='c')


if __name__ == '__main__':
    root.mainloop()
