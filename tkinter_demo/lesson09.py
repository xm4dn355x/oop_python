# -*- coding: utf-8 -*-
########################################################################
#                                                                      #
# Pack and Frame                                                       #
#                                                                      #
# MIT License                                                          #
# Copyright (c) 2021 Michael Nikitenko                                 #
#                                                                      #
########################################################################


from tkinter import Tk, Label, Frame, LabelFrame

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

# Без фреймов
# label_one = Label(
#     master=root,
#     text='Метка 1',
#     bg='red',
#     fg=COLOR_TEXT,
#     height=1,
#     width=8,
#     justify='left',
#     anchor='center',
#     font=('Helvetica', 20, 'normal'),
# )
# label_two = Label(
#     master=root,
#     text='Метка 2',
#     bg='green',
#     fg=COLOR_TEXT,
#     height=1,
#     width=8,
#     justify='left',
#     anchor='center',
#     font=('Helvetica', 20, 'normal')
# )
# label_three = Label(
#     master=root,
#     text='Метка 3',
#     bg='blue',
#     fg=COLOR_TEXT,
#     height=1,
#     width=8,
#     justify='left',
#     anchor='center',
#     font=('Helvetica', 20, 'normal')
# )
# label_four = Label(
#     master=root,
#     text='Метка 4',
#     bg='yellow',
#     fg=COLOR_TEXT,
#     height=1,
#     width=8,
#     justify='left',
#     anchor='center',
#     font=('Helvetica', 20, 'normal')
# )
# label_five = Label(
#     master=root,
#     text='Метка 4',
#     bg=COLOR_OVERLAY_LIGHT,
#     fg=COLOR_TEXT,
#     height=1,
#     width=8,
#     justify='left',
#     anchor='center',
#     font=('Helvetica', 20, 'normal')
# )

# label_one.pack(side='top', fill='both')
# label_two.pack(side='bottom', fill='both')
# label_three.pack(side='right', fill='both')
# label_four.pack(side='left', fill='both')
# label_five.pack(side='left', fill='both')

# С фреймами
frame_top = LabelFrame(
    master=root,
    text='Top Frame',
    bg='pink',
    padx=10,
    pady=10
)
frame_bottom = Frame(
    master=root,
    bg='aqua',
    padx=10,
    pady=10
)
label_one = Label(
    master=frame_top,
    text='Метка 1',
    bg='red',
    fg=COLOR_TEXT,
    height=1,
    width=8,
    justify='left',
    anchor='center',
    font=('Helvetica', 20, 'normal'),
)
label_two = Label(
    master=frame_top,
    text='Метка 2',
    bg='green',
    fg=COLOR_TEXT,
    height=1,
    width=8,
    justify='left',
    anchor='center',
    font=('Helvetica', 20, 'normal')
)
label_three = Label(
    master=frame_bottom,
    text='Метка 3',
    bg='blue',
    fg=COLOR_TEXT,
    height=1,
    width=8,
    justify='left',
    anchor='center',
    font=('Helvetica', 20, 'normal')
)
label_four = Label(
    master=frame_bottom,
    text='Метка 4',
    bg='yellow',
    fg=COLOR_TEXT,
    height=1,
    width=8,
    justify='left',
    anchor='center',
    font=('Helvetica', 20, 'normal')
)
label_five = Label(
    master=root,
    text='Метка 4',
    bg=COLOR_OVERLAY_LIGHT,
    fg=COLOR_TEXT,
    height=1,
    width=8,
    justify='left',
    anchor='center',
    font=('Helvetica', 20, 'normal')
)

frame_top.pack(side='top', fill='both', padx=10, pady=10, expand=1)

label_five.pack(side='bottom', anchor='se', fill='y', padx=10, pady=10)

frame_bottom.pack(side='bottom', fill='both', padx=10, pady=10)

label_one.pack(side='left', fill='both', expand=1)
label_two.pack(side='left', fill='both')
label_three.pack(side='left', fill='both')
label_four.pack(side='left', fill='both', expand=1)


if __name__ == '__main__':
    root.mainloop()
