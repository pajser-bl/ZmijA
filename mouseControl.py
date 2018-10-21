import win32api,win32con
import time

def leftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def setMousePosition(x,y):
    win32api.SetCursorPos((x,y))
