import listas

from crud.crud_productos import productos

from crud.crud_clientes import clientes

from crud.crud_ventas import ventas

from Funciones.funciones import obtener_entero, inicio

que_soy = int(input("1.ADMIN. 2LECTOR.  "))
if que_soy == 1:
    listas.ADMIN = True
else:
    listas.ADMIN = False

def menu_principal():
    texto = "MENU PRINCIPAL"
    inicio(texto)
    ask_menu = obtener_entero("0. Salir\n1. Productos\n2. Clientes\n3.Ventas...", 0, 3)

    if ask_menu == 0:
        print("Saliendo del programa...")
        return 0

    return ask_menu


opcion = -1
while opcion != 0:
    opcion = menu_principal()
    match opcion:
        case 1:
            productos()
        case 2:
            clientes()
        case 3:
            ventas()