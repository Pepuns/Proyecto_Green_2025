def opcion1():
    print("hola soy la opcion1")

def opcion2():
    print("hola soy la opcion2")

def opcion3():
    print("hola soy la opcion3")

def opcion4():
    print("hola soy la opcion4")

menu = 0
while(menu != 5):
    print("1. opcion1")
    print("2. opcion2")
    print("3. opcion3")
    print("4. opcion4")
    print("5. salir")
    menu = int(input(""))
    match menu:
        case 1:
            opcion1()
        case 2:
            opcion2()
        case 3:
            opcion3()
        case 4:
            opcion4()

