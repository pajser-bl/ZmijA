from PIL import Image
import screenGrab

#koordinata gornjeg lijevog ugla
x_start=58
y_start=81

#sirina i duzina polja u pikselima
_dim=20

#funkcija vraca matricu popunjenu brojevima
def mapMatrix(field_size,image_path):
    image=Image.open(image_path)
    pixels=image.load()
    matrix=[0]*field_size
    for i in range(field_size):
        matrix[i]=[0]*field_size
    for i in range(10,(field_size-1)*20-10,20):
        for j in range(10,(field_size-1)*20-10,20):

            # print("[%d,%d]m[%d,%d]/n"%(i,j,i//20,j//20))

            #BIJELO(255,255,255) - PRAZNO 0
            if pixels[i,j]==(255,255,255):
                matrix[j//20][i//20]=0

            # ZELENO(0,0,128) - GLAVA 1
            if pixels[i,j]==(0,128,0):
                print(1)
                matrix[j//20][i//20]=1

            #CRNO(255,255,255) - REP 2
            if pixels[i,j]==(0,0,0):
                matrix[j//20][i//20] = 2

            #CRVENO(255,0,0) - JABUKA 3
            if pixels[i,j]==(255,0,0):
                matrix[j//20][i//20]=3
    return matrix


