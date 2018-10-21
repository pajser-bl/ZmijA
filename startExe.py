import os

def startExe(path):
    try:
        os.startfile(path)

    except FileNotFoundError:
        print("EXCEPTION: Executable not found!")
