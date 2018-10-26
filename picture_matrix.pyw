import screen_grab

# koordinata gornjeg lijevog ugla
x_start = 57
y_start = 80

# sirina i duzina polja u pikselima
_dim = 20

# BOJE POLJA RBG:
WHITE = (255, 255, 255)  # prazno polje 0
GREEN = (0, 128, 0)  # glava zmije 1
BLACK = (0, 0, 0)  # rep zmije 2
RED = (255, 0, 0)  # jabuka 3


#  Funkcija vraca matricu popunjenu brojevima
def map_matrix(field_size):
    image = screen_grab.screen_grab(field_size)
    matrix = [0] * field_size
    for i in range(field_size):
        matrix[i] = [0] * field_size
    for i in range(10, (field_size - 1) * 20 - 10, 20):
        for j in range(10, (field_size - 1) * 20 - 10, 20):
            if image.getpixel((i, j)) == WHITE:
                matrix[j // 20][i // 20] = 0
            if image.getpixel((i, j)) == GREEN:
                matrix[j // 20][i // 20] = 1
            if image.getpixel((i, j)) == BLACK:
                matrix[j // 20][i // 20] = 2
            if image.getpixel((i, j)) == RED:
                matrix[j // 20][i // 20] = 3
    if apple_exists(matrix) and head_exists(matrix):
        for i in range(field_size):
            print(matrix[i])
        return matrix
    else:
        return None


def find_head(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[j][i] == 1:
                return i, j


def find_apple(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[j][i] == 3:
                return i, j


def field_exists(dot, matrix):
    (x, y) = dot
    if 0 <= x < len(matrix) and 0 <= y < len(matrix):
        return 1
    else:
        return 0


def is_tail(dot, matrix):
    (y, x) = dot
    if matrix[x][y] == 2:
        return 1
    else:
        return 0


def apple_exists(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[j][i] == 3:
                return True
    return False


def head_exists(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[j][i] == 1:
                return True
    return False
