import mouse_control
import time
import os
import win32gui
import sys

#  Vrijednosti koordinata
x = 0
y = 0

#  Koordinata za izbor velicine polja
x_chose_field = x + 180
y_chose_field = y + 60

#  Sredina izbora velicine polja
x_field_first_choice = x_chose_field
y_field_first_choice = y_chose_field + 16

#  Koordinata za izbor brzine zmije
x_chose_interval = x + 180
y_chose_interval = y + 103

#  Sredina izbora brzine zmije
x_interval_first_choice = x_chose_interval
y_interval_first_choice = y_chose_interval + 16

#  Visina polja za izbor
_dim = 13

#  Koordinata starta
x_start = x + 106
y_start = y + 152

#  Koordinata X igre
x_exit = 175
y_exit = 65

#  Pomjeraj X po jedinici polja
_dim_exit = 40


def set_field_size(n):
    mouse_control.set_mouse_position(x_chose_field, y_chose_field)
    mouse_control.left_click()
    time.sleep(.500)
    if n == "7x7":
        mouse_control.set_mouse_position(x_field_first_choice, y_field_first_choice)
    if n == "9x9":
        mouse_control.set_mouse_position(x_field_first_choice, y_field_first_choice + _dim)
    if n == "11x11":
        mouse_control.set_mouse_position(x_field_first_choice, y_field_first_choice + _dim * 2)
    if n == "13x13":
        mouse_control.set_mouse_position(x_field_first_choice, y_field_first_choice + _dim * 3)
    if n == "15x15":
        mouse_control.set_mouse_position(x_field_first_choice, y_field_first_choice + _dim * 4)
    if n == "17x17":
        mouse_control.set_mouse_position(x_field_first_choice, y_field_first_choice + _dim * 5)
    if n == "19x19":
        mouse_control.set_mouse_position(x_field_first_choice, y_field_first_choice + _dim * 6)
    mouse_control.left_click()


def set_move_interval(i):
    mouse_control.set_mouse_position(x_chose_interval, y_chose_interval)
    mouse_control.left_click()
    time.sleep(.500)
    if i == 100:
        mouse_control.set_mouse_position(x_interval_first_choice, y_interval_first_choice)
    if i == 200:
        mouse_control.set_mouse_position(x_interval_first_choice, y_interval_first_choice + _dim * 1)
    if i == 300:
        mouse_control.set_mouse_position(x_interval_first_choice, y_interval_first_choice + _dim * 2)
    if i == 400:
        mouse_control.set_mouse_position(x_interval_first_choice, y_interval_first_choice + _dim * 3)
    if i == 500:
        mouse_control.set_mouse_position(x_interval_first_choice, y_interval_first_choice + _dim * 4)
    if i == 600:
        mouse_control.set_mouse_position(x_interval_first_choice, y_interval_first_choice + _dim * 5)
    if i == 700:
        mouse_control.set_mouse_position(x_interval_first_choice, y_interval_first_choice + _dim * 6)
    if i == 800:
        mouse_control.set_mouse_position(x_interval_first_choice, y_interval_first_choice + _dim * 7)
    if i == 900:
        mouse_control.set_mouse_position(x_interval_first_choice, y_interval_first_choice + _dim * 8)
    if i == 1000:
        mouse_control.set_mouse_position(x_interval_first_choice, y_interval_first_choice + _dim * 9)
    mouse_control.left_click()


def start_game():
    time.sleep(.500)
    mouse_control.set_mouse_position(x_start, y_start)
    mouse_control.left_click()
    mouse_control.set_mouse_position(0, 0)


def start_exe(path):
    try:
        os.startfile(path)
    except FileNotFoundError:
        print("EXCEPTION: Executable not found!")


def maximize(window_title):
    window = win32gui.FindWindow(None, window_title)
    win32gui.SetForegroundWindow(window)
    win32gui.ShowWindow(window, 3)


def set_up_game(field_size, move_interval, executable, window_title):
    start_exe(executable)
    time.sleep(1)
    maximize(window_title)
    time.sleep(1)
    set_field_size(field_size)
    set_move_interval(move_interval)
    start_game()


def close_all(field_size):
    close_game(field_size)
    sys.exit(0)


def close_game(field_size):
    mouse_control.set_mouse_position(x_exit + _dim_exit * field_size, y_exit)
