tiempo =[0, 0, 0]

def cambiarHora(tiempo):
    filetemporizador = open("data/temporizador_data.txt", "w")
    while True:
        tiempo[2] = int(input("Ingrese horas: "))
        tiempo[1] = int(input("Ingrese minutos: "))
        tiempo[0] = int(input("Ingrese segundos: "))
        if tiempo[0] > 59 or tiempo[1] > 59 or tiempo[2] > 24:
            print("Error, ingrese un tiempo valido")
        else:
            break
    if tiempo[2] < 10:
        tiempo[2] = "0" + str(tiempo[2])
    if tiempo[1] < 10:
        tiempo[1] = "0" + str(tiempo[1])
    if tiempo[0] < 10:
        tiempo[0] = "0" + str(tiempo[0])
    filetemporizador.write(f"{tiempo[2]} {tiempo[1]} {tiempo[0]}")
    filetemporizador.close()