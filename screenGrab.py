from PIL import ImageGrab,Image
import os
import time

#koordinata gornjeg lijevog ugla
x_start=58
y_start=81

#duzina i sirina polja u pikselima
_dim=20

def screenGrab(size):
    box = (x_start,y_start,x_start+size*_dim,y_start+size*_dim)
    im = ImageGrab.grab(box)
    im.save("pic.png", 'PNG')


