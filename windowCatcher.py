import win32gui

def maximize(window_title):
    window = win32gui.FindWindow(None, window_title)
    win32gui.SetForegroundWindow(window)
    win32gui.ShowWindow(window,3)

