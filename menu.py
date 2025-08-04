import asyncio
from funciones import Gordoctavio
from funciones import alarma_fn
from funciones import CH
import datetime
from funciones import Calendario

tiempo =[0, 0, 0]

def opcion1():
    temporizador = True
    tiempo =[0, 0, 0]
    print("hola soy la opcion1")
    asyncio.run(Gordoctavio.main(tiempo, temporizador))
    Calendario.get_time(tiempo)

def opcion2():
    print("hola soy la opcion2")
    temporizador = True
    alarma_fn.obtener_tiempo()
    Calendario.get_time(tiempo)
    alarma_fn.alarma(temporizador, tiempo)

def opcion3():
    CH.cambiarHora(tiempo)

def opcion4():
    print("Iniciando ")
    Calendario.read_time()
    pressbtn = input("")


menu = 0

while(menu != 5):
    print("1. opcion1")
    print("2. opcion2")
    print("3. opcion3")
    print("4. opcion4")
    print("5. salir")
    menu = int(input(""))
    print("")
    match menu:
        case 1:
            opcion1()
        case 2:
            opcion2()
        case 3:
            opcion3()
        case 4:
            opcion4()
