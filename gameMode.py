import mouseControl
import time

#1337 rjesenje MAXIMIZE
#da se rjesiti i preko trazenja koordinata
#ovo dole sam rjesio tako sto sam uzeo screenshoot i vidio
#vrijednosti koordinata
x=0
y=0

#koordinata za izbor velicine polja
x_chose_field=x+180
y_chose_field=y+60

#sredina izbora velicine polja
x_field_first_choice=x_chose_field
y_field_first_choice=y_chose_field+16

#koordinata za izbor brzine zmije
x_chose_interval=x+180
y_chose_interval=y+103

#sredina izbora brzine zmije
x_interval_first_choice=x_chose_interval
y_interval_first_choice=y_chose_interval+16

#visina polja za izbor
_dim=13

#koordinata starta
x_start=x+106
y_start=y+152


def setFieldSize(n):
    mouseControl.setMousePosition(x_chose_field,y_chose_field)
    mouseControl.leftClick()
    time.sleep(.500)
    if n == "7x7":
        mouseControl.setMousePosition(x_field_first_choice,y_field_first_choice)
    if n == "9x9":
        mouseControl.setMousePosition(x_field_first_choice,y_field_first_choice+_dim)
    if n == "11x11":
        mouseControl.setMousePosition(x_field_first_choice,y_field_first_choice+_dim*2)
    if n == "13x13":
        mouseControl.setMousePosition(x_field_first_choice,y_field_first_choice+_dim*3)
    if n == "15x15":
        mouseControl.setMousePosition(x_field_first_choice,y_field_first_choice+_dim*4)
    if n == "17x17":
        mouseControl.setMousePosition(x_field_first_choice,y_field_first_choice+_dim*5)
    if n == "19x19":
        mouseControl.setMousePosition(x_field_first_choice, y_field_first_choice + _dim*6)
    mouseControl.leftClick()
    #time.sleep(.500)



def setMoveInterval(i):
    mouseControl.setMousePosition(x_chose_interval, y_chose_interval)
    mouseControl.leftClick()
    time.sleep(.500)
    if i == 100:
        mouseControl.setMousePosition(x_interval_first_choice,y_interval_first_choice)
    if i == 200:
        mouseControl.setMousePosition(x_interval_first_choice,y_interval_first_choice + _dim * 1)
    if i == 300:
        mouseControl.setMousePosition(x_interval_first_choice,y_interval_first_choice+ _dim * 2)
    if i == 400:
        mouseControl.setMousePosition(x_interval_first_choice,y_interval_first_choice + _dim * 3)
    if i == 500:
        mouseControl.setMousePosition(x_interval_first_choice,y_interval_first_choice + _dim * 4)
    if i == 600:
        mouseControl.setMousePosition(x_interval_first_choice,y_interval_first_choice + _dim * 5)
    if i == 700:
        mouseControl.setMousePosition(x_interval_first_choice,y_interval_first_choice + _dim * 6)
    if i == 800:
        mouseControl.setMousePosition(x_interval_first_choice,y_interval_first_choice + _dim * 7)
    if i == 900:
        mouseControl.setMousePosition(x_interval_first_choice,y_interval_first_choice + _dim * 8)
    if i == 1000:
        mouseControl.setMousePosition(x_interval_first_choice,y_interval_first_choice + _dim * 9)
    mouseControl.leftClick()
    #time.sleep(.500)


def startGame():
    time.sleep(1)
    mouseControl.setMousePosition(x_start,y_start)
    mouseControl.leftClick()
    mouseControl.setMousePosition(0,0)
