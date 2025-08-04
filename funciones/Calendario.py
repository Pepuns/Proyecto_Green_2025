import time
import datetime
tiempo = [0, 0, 0]
tiempot = [0, 0, 0]

def get_time(tiempo):
    filetempo = open("data/Registrodata.txt", "a")
    fecha_actual = datetime.datetime.now()
    año = fecha_actual.year
    mes = fecha_actual.month
    dia = fecha_actual.day
    filetempo.write(f"{año} {mes} {dia} {tiempo[2]} {tiempo[1]} {tiempo[0]}\n")
    filetempo.close()

#def semana():
    #dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    #fecha_actual = datetime.datetime.now()
    #dia_semana = fecha_actual.weekday()
    #print (dias [dia_semana])
    #print (fecha_actual.isocalendar()[1])

def read_time():
    tiempot = [0, 0, 0]
    filetempo = open("data/Registrodata.txt", "r")
    contenido = filetempo.readlines()
    filetempo.close()
    lineas = len(contenido)
    filetempo = open("data/Registrodata.txt", "w")

    for i in range(lineas):
        z = contenido[i].split()
        print(z[0], z[1], z[2], z[3], z[4], z[5])
        tiempo = [int(z[3]), int(z[4]), int(z[5])]
        #print("Tiempo registrado:", tiempo[2], "segundos,", tiempo[1], "minutos,", tiempo[0], "horas")
        fecha_registro = datetime.date(int(z[0]), int(z[1]), int(z[2]))
        if fecha_registro.isocalendar()[1] == datetime.date.today().isocalendar()[1]:
            Sumo(tiempot, tiempo, z, filetempo)
    while tiempot[0] >= 60:
        tiempot[0] -= 60
        tiempot[1] += 1
    while tiempot[1] >= 60:
        tiempot[1] -= 60
        tiempot[2] += 1
    print("Tiempo total acumulado:", tiempot[0], "segundos,", tiempot[1], "minutos,", tiempot[2], "horas")
    filetempo.close
    

def Sumo(tiempot, tiempo, z, filetempo):
    tiempot[0] = tiempot[0] + tiempo[0]
    tiempot[1] = tiempot[1] + tiempo[1]
    tiempot[2] = tiempot[2] + tiempo[2]
    filetempo.write(f"{z[0]} {z[1]} {z[2]} {z[3]} {z[4]} {z[5]}\n")

    
