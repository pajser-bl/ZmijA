import game_mode
import brain

executable = "Snake.exe"
window_title = "Parameters"
picture_path = "pic.png"


def main():

    game_mode.set_up_game("7x7", 1000, executable, window_title)
    brain.think_and_move("7x7", 1000, picture_path)


if __name__ == '__main__':
    main()
