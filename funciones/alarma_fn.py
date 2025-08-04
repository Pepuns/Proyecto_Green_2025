import time
from librerias import playsound

temporizador = True
tiempo = [0, 0, 0]
#[2] horas
#[1] minutos
#[0] segundos
def obtener_tiempo():
    filetemporizador = open("data/temporizador_data.txt", "r")
    contenido = filetemporizador.read()
    filetemporizador.close()
    contenido = contenido.split()
    tiempo[2] = int(contenido[0])
    tiempo[1] = int(contenido[1])
    tiempo[0] = int(contenido[2])

def alarma(temporizador, tiempo):
    while temporizador == True:
        print("segundos:", tiempo[0], "minutos:", tiempo[1], "horas:", tiempo[2])
        if tiempo[1] == 0 and tiempo[2] > 0 and tiempo[0] == 0:
            tiempo[2] -= 1
            tiempo[1] = 60
        if tiempo[0] == 0:
            tiempo[1] -= 1
            tiempo[0] = 60
        tiempo[0] -= 1
        time.sleep(1)
        if tiempo[0] <= 59 and tiempo[1] <= -1 and tiempo[2] <= 0:
            temporizador = False
            #esta linea la pongo como comentario solo para trabajar más rapido
            #playsound.playsound('audio/sound.mp3')
            print("")
    

#import time

#temporizador = True
#tiempo = [0, 0, 0]
#[2] horas
#[1] minutos
#[0] segundos
#def alarma(tiempo, temporizador):
#    while(temporizador == True):
#        if tiempo[0] > 0:
#            tiempo[0] -= 1
#        elif tiempo[1] > 0:
#            tiempo[0] = 59
#            tiempo[1] -= 1
#       elif tiempo[2] > 0:
#           tiempo[0] = 59
#           tiempo[1] = 59
#            tiempo[2] -= 1
#        print ("segundos:", tiempo[0], "minutos:", tiempo[1]," horas:", tiempo[2])
#        time.sleep(1)
#        if tiempo[2] <= 0 and tiempo[1] <= 0 and tiempo[0] <= 0:
#            temporizador = False
#    print("")