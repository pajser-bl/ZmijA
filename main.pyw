import game_mode
import brain

executable = "Snake.exe"
window_title = "Parameters"


def main():

    game_mode.set_up_game("19x19", 3000, executable, window_title)
    brain.think_and_move("19x19", 3000)


if __name__ == '__main__':
    main()
