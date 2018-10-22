import gameMode
import brain

executable = "Snake.exe"
window_title = "Parameters"
picture_path = "pic.png"


def main():
    gameMode.set_up_game("17x17", 500, executable, window_title)
    brain.think_and_move("17x17", 500, picture_path)


if __name__ == '__main__':
    main()
