from PIL import ImageGrab

#  Koordinata gornjeg lijevog ugla
x_start=58
y_start=81

#  Duzina i sirina polja u pikselima
_dim=20


def screen_grab(size):
    box = (x_start, y_start, x_start+size*_dim, y_start+size*_dim)
    im = ImageGrab.grab(box)
    im.save("pic.png", 'PNG')


