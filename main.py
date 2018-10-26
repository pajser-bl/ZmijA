import game_mode
import brain

executable = "Snake.exe"
window_title = "Parameters"


def main():
    setup_and_start("11x11", 1100)


def setup_and_start(field_size, move_interval):
    game_mode.set_up_game(field_size, move_interval, executable, window_title)
    brain.think_and_move(field_size, move_interval)


if __name__ == '__main__':
    main()
