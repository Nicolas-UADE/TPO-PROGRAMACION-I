from listas import ADMIN

from crud.crud_productos import listar_productos,baja_producto,alta_producto,modificar_producto

from crud.crud_clientes import clientes

from crud.crud_ventas import ventas

from Funciones.funciones import volver_al_menu,obtener_entero

que_soy = int(input("1.ADMIN. 2LECTOR.  "))
if que_soy == 1:
    ADMIN = True
else:
    ADMIN = False

def menu_principal():
    print("\n\n==========\nMENU PRINCIPAL\n==========")
    ask_menu = obtener_entero("0. Salir\n1. Productos\n2. Clientes\n3.Ventas...", 0, 3)

    if ask_menu == 0:
        print("Saliendo del programa...")
        return 0

    return ask_menu


def productos():
    print("\n\n==========\nPRODUCTOS\n==========")
    if ADMIN == True:
        ask = obtener_entero(
            "0. Retroceder\n1. Listado de producto\n2. Baja de producto\n3.Alta de producto\n4.Modificar producto...",
            0,
            4,
        )
        match ask:
            case 0:
                volver_al_menu()
            case 1:
                listar_productos()
            case 2:
                baja_producto()
            case 3:
                alta_producto()
            case 4:
                modificar_producto()
    else:
        ask = obtener_entero("0. Retroceder\n1. Listado de producto\n", 0, 1)
        match ask:
            case 0:
                volver_al_menu()
            case 1:
                listar_productos()

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