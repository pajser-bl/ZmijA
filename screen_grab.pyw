from PIL import ImageGrab

#  Koordinata gornjeg lijevog ugla igre
x_start = 58
y_start = 80

#  Duzina i sirina polja u pikselima
_dim = 20

# Koordinata gornjeg lijevog ugla prozora
x_window_start = 58
y_window_start = 51

# Window padding
_pad = 30


def screen_grab(size):
    box = (x_start, y_start, x_start + size * _dim, y_start + size * _dim)
    return ImageGrab.grab(box)


def save_screen_grab(size, time):
    box = (x_window_start, y_window_start, x_window_start + size * _dim, y_window_start + _pad + size * _dim)
    image = ImageGrab.grab(box)
    image.save(str(size) + 'x' + str(size) + '_' + str(time*1000) + '.png', 'PNG')


def main():
    save_screen_grab(19, 700)


if __name__ == '__main__':
    main()

