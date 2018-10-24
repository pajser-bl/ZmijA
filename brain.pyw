import a_star
import time
import press_key
import picture_matrix
import screen_grab
import game_mode


def think_and_move(field_size, move_interval):
    time_to_wait = move_interval / 1000
    time_to_hurry = move_interval / 10000
    while 1:
        move_order = get_move_order(get_field_int(field_size), time_to_wait)
        print(move_order)
        for direction in move_order:
            print(direction)
            move(direction)
            wait(time_to_wait - time_to_hurry)


def wait(time_to_wait):
    time.sleep(time_to_wait)


def move(direction):
    if direction == "right":
        press_key.press_right()
    if direction == "left":
        press_key.press_left()
    if direction == "down":
        press_key.press_down()
    if direction == "up":
        press_key.press_up()


def get_direction(first_node, second_node):
    (old_x, old_y) = first_node.coordinates
    (new_x, new_y) = second_node.coordinates
    if old_x < new_x:
        return "right"
    if old_x > new_x:
        return "left"
    if old_y < new_y:
        return "down"
    if old_y > new_y:
        return "up"


def get_field_int(field_size):
    if field_size == "7x7":
        return 7
    if field_size == "9x9":
        return 9
    if field_size == "11x11":
        return 11
    if field_size == "13x13":
        return 13
    if field_size == "15x15":
        return 15
    if field_size == "17x17":
        return 17
    if field_size == "19x19":
        return 19


def get_path(field_size, time_to_wait):
    matrix = picture_matrix.map_matrix(field_size, time_to_wait)
    if matrix is None:
        return None
    return a_star.a_star(matrix)


def get_move_order(field_size, time_to_wait):
    path = get_path(field_size, time_to_wait)
    if not path:
        print("Matrix is bad, trying to remap...")
        time.sleep(.100)
        path = get_path(field_size, time_to_wait)
        if not path:
            print("Remapping failed. Stopping simulation.")
            print("Taking screen shot.")
            screen_grab.save_screen_grab(field_size, game_mode.get_foreground_window_title())
            print("Closing all windows.")
            game_mode.close_all(field_size)
    move_order = []
    for i in range(0, len(path)-1):
        direction = get_direction(path[i], path[i+1])
        move_order.append(direction)
    return move_order
