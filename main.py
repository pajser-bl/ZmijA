import startExe
import gameMode
import windowCatcher
import time
import pressKey

executable="Snake.exe"
window_title="Parameters"

def main():
    startExe.startExe(executable)
    time.sleep(1)
    windowCatcher.maximize(window_title)
    time.sleep(1)
    gameMode.setFieldSize("19x19")
    gameMode.setMoveInterval(200)
    gameMode.startGame()
    time.sleep(.10)
    pressKey.pressLeft()
    time.sleep(.200)
    pressKey.pressDown()

if __name__ == '__main__':
    main()