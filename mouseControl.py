import win32api
import win32con
import time


def left_click():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


def set_mouse_position(x, y):
    win32api.SetCursorPos((x, y))
