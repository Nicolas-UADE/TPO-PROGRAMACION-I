from Funciones.funciones import (
    inicio,
    obtener_caracter,
    obtener_entero,
    lista_cabeza_clientes,
    buscar_por_id,
    inicio_alta,
    inicio_baja,
    inicio_modificar,
    inicio_listado,
    buscar_por_nombre,
)
import listas
from listas import ELIMINADO, lista_clientes

#from login import ADMIN


def clientes():
    texto = "CLIENTES"
    inicio(texto)
    if listas.ADMIN == True:
        ask = obtener_entero(
            "0. Retroceder\n1. Listado de clientes\n2. Baja de clientes\n3.Alta de clientes\n4.Modificar clientes\n.",
            0,
            4,
        )
        match ask:
            case 0:
                return
            case 1:
                listado_clientes()
            case 2:
                baja_clientes()
            case 3:
                alta_clientes()
            case 4:
                modificar_clientes()
    else:
        ask = obtener_entero("0. Retroceder\n1. Listado de clientes\n", 0, 1)
        match ask:
            case 0:
                return
            case 1:
                listado_clientes()


def alta_clientes():
    texto = "ALTA DE CLIENTES"
    inicio_alta(texto)

    nombre = obtener_caracter("Nombre y apellido:\n.").upper()

    dni = obtener_entero("DNI:\n.", 1000000, 99999999)

    telefono = obtener_entero("Telefono:\n.", 1000000000, 9999999999)

    email = obtener_caracter("Email:\n.").lower()

    while (
        email.endswith("@gmail.com") == False
        and email.endswith("@hotmail.com") == False
        and email.endswith("@outlook.com") == False
        and email.endswith("@yahoo.com") == False
    ):
        print("\nIngrese un mail valido.\n")
        email = obtener_caracter("Email:\n.").lower()

    el_dni = str(dni)
    el_telefono = str(telefono)

    nuevo_id = len(lista_clientes) + 1

    cliente = {
        "id": nuevo_id,
        "nombre": nombre,
        "dni": el_dni,
        "telefono": el_telefono,
        "email": email,
    }
    pregunta_seguridad = obtener_caracter(
        f"\nEsta seguro de agregar al cliente? Y/N\n."
    ).upper()

    if pregunta_seguridad == "Y":
        lista_clientes.append(cliente)
        print("\n\033[32mCliente agregado correctamente.\033[0m")

    else:
        print("\n\033[31mAlta de cliente cancelada.\033[0m")

    texto = ""
    inicio_alta(texto)


def listado_clientes():
    texto = "LISTADO CLIENTES"
    inicio_listado(texto)
    pregunta_orden = obtener_entero(
        "\nElija metodo de ordenamiento. 1.ID  2.Buscar por nombre. 3.Buscar por codigo. -1 para salir\n.",
        -1,
        4,
    )
    match pregunta_orden:
        case -1:
            return
        case 0:
            pregunta_orden = obtener_entero(
                "\nElija metodo de ordenamiento. 1.ID  2.Buscar por nombre. 3.Buscar por codigo. -1 para salir\n.",
                -1,
                4,
            )
        case 1:
            lista_cabeza_clientes()

            for cliente in lista_clientes:
                if cliente != ELIMINADO:
                    print(
                        f"|{cliente['id']:<20} | {cliente['nombre']:<20} | {cliente['dni']:<20} | {cliente['telefono']:<20} | {cliente['email']:<20}"
                    )

        
        

        case 2:
            pregunta_nombre = obtener_caracter(
                "\n\nIngrese nombre del cliente a buscar. -1 Para salir\n."
            )

            if pregunta_nombre == "-1":
                return
            esta = buscar_por_nombre(lista_clientes, pregunta_nombre)

            while esta == -2:
                print("Cliente inexistente.")
                pregunta_nombre = obtener_caracter(
                    "\nIngrese código del cliente a buscar. -1 Para salir\n."
                )
                if pregunta_nombre == "-1":
                    return
                esta = buscar_por_nombre(lista_clientes, pregunta_nombre)
            print(lista_clientes[esta])

        case 3:

            pregunta_codigo = obtener_entero(
                "\n\nIngrese código del cliente a buscar. -1 Para salir\n.", -1, 1000000
            )

            match pregunta_codigo:
                case 0:
                    pregunta_codigo = obtener_entero(
                        "\nIngrese código del cliente a modificar. -1 Para salir\n.",
                        -1,
                        1000000,
                    )

                case -1:
                    return

            esta = buscar_por_id(lista_clientes, pregunta_codigo)

            while esta == -2:
                print("Cliente inexistente.")
                pregunta_codigo = obtener_entero(
                    "\nIngrese código del cliente a modificar. -1 Para salir\n.",
                    -1,
                    1000000,
                )
                if pregunta_codigo == -1:
                    return
                esta = buscar_por_id(lista_clientes, pregunta_codigo)
            print(lista_clientes[esta])

    texto = ""
    inicio_listado(texto)


def baja_clientes():
    texto = "BAJA DE CLIENTES"
    inicio_baja(texto)

    pregunta_codigo = obtener_entero(
        "\n\nIngrese código del cliente a eliminar. -1 Para salir\n.", -1, 1000000
    )

    match pregunta_codigo:
        case 0:
            pregunta_codigo = obtener_entero(
                "\nIngrese código del cliente a eliminar. -1 Para salir\n.", -1, 1000000
            )

        case -1:
            return

    esta = buscar_por_id(lista_clientes, pregunta_codigo)
    while esta == -2:
        print("Cliente inexistente.")
        pregunta_codigo = obtener_entero(
            "\nIngrese código del cliente a eliminar. -1 Para salir\n.", -1, 1000000
        )
        if pregunta_codigo == -1:
            return
        esta = buscar_por_id(lista_clientes, pregunta_codigo)

    pregunta_seguridad = obtener_caracter(
        f"\nEsta seguro de eliminar al cliente {pregunta_codigo}? Y/N\n."
    ).upper()

    if pregunta_seguridad == "Y":

        lista_clientes[esta] = ELIMINADO

        print("\n\033[32mCliente eliminado correctamente.\033[0m")

    else:
        print("\n\033[31mBaja de cliente cancelada.\033[0m")
    texto = ""
    inicio_baja(texto)


def modificar_clientes():
    texto = "MODIFICAR CLIENTES"
    inicio_modificar(texto)
    pregunta_codigo = obtener_entero(
        "\n\nIngrese código del cliente a modificar. -1 Para salir\n.", -1, 1000000
    )

    match pregunta_codigo:
        case 0:
            pregunta_codigo = obtener_entero(
                "\nIngrese código del cliente a modificar. -1 Para salir\n.",
                -1,
                1000000,
            )

        case -1:
            return

    esta = buscar_por_id(lista_clientes, pregunta_codigo)
    while esta == -2:
        print("Cliente inexistente.")
        pregunta_codigo = obtener_entero(
            "\nIngrese código del cliente a modificar. -1 Para salir\n.", -1, 1000000
        )
        if pregunta_codigo == -1:
            return
        esta = buscar_por_id(lista_clientes, pregunta_codigo)

    pregunta_eleccion = obtener_entero("Que quieres modificar. \n1.Nombre\n 2.DNI\n3.Telefono\n4.Email.\n.",1,4)
    match pregunta_eleccion:
        case 1:
            nombre = obtener_caracter("Nombre y apellido:\n.").upper()
            pregunta_seguridad = obtener_caracter(
                    f"\nEsta seguro de modificar el cliente {pregunta_codigo}? Y/N\n."
                ).upper()

            if pregunta_seguridad == "Y":
                lista_clientes[esta]["nombre"] = nombre
    
                    
                print("\n\033[32mCliente modificado correctamente.\033[0m")
                pregunta_eleccion_otra = obtener_caracter("Desea hacer otra modificacion? Y/N\n")
                if pregunta_eleccion_otra == "Y":
                    texto = ""
                    inicio_modificar(texto)
                    modificar_clientes()
            else:
                print("\n\033[31mModificacion de cliente cancelada.\033[0m")


        case 2:

            dni = obtener_entero("DNI:\n.", 1000000, 99999999)

            
            pregunta_seguridad = obtener_caracter(
                    f"\nEsta seguro de modificar el cliente {pregunta_codigo}? Y/N\n."
                ).upper()

            if pregunta_seguridad == "Y":
                el_dni = str(dni)
                lista_clientes[esta]["dni"] = el_dni
                
    
     
                print("\n\033[32mCliente modificado correctamente.\033[0m")
                pregunta_eleccion_otra = obtener_caracter("Desea hacer otra modificacion? Y/N\n")
                if pregunta_eleccion_otra == "Y":
                    texto = ""
                    inicio_modificar(texto)
                    modificar_clientes()
            else:
                print("\n\033[31mModificacion de cliente cancelada.\033[0m")


        case 3:
            telefono = obtener_entero("Telefono:\n.", 1000000000, 9999999999)
            pregunta_seguridad = obtener_caracter(
                                f"\nEsta seguro de modificar el cliente {pregunta_codigo}? Y/N\n."
                            ).upper()
            
            if pregunta_seguridad == "Y":
                el_telefono = str(telefono)

                
                lista_clientes[esta]["telefono"] = el_telefono
                
    
        
                print("\n\033[32mCliente modificado correctamente.\033[0m")
                pregunta_eleccion_otra = obtener_caracter("Desea hacer otra modificacion? Y/N\n")
                if pregunta_eleccion_otra == "Y":
                    texto = ""
                    inicio_modificar(texto)
                    modificar_clientes()
            else:
                print("\n\033[31mModificacion de cliente cancelada.\033[0m")


        case 4:
            email = obtener_caracter("Email:\n.").lower()
            while (
                    email.endswith("@gmail.com") == False
                    and email.endswith("@hotmail.com") == False
                    and email.endswith("@outlook.com") == False
                    and email.endswith("@yahoo.com") == False
                ):
                    print("\nIngrese un mail valido.\n")
                    email = obtener_caracter("Email:\n.").lower()

            pregunta_seguridad = obtener_caracter(
                                f"\nEsta seguro de modificar el cliente {pregunta_codigo}? Y/N\n."
                            ).upper()
            
            if pregunta_seguridad == "Y":
                         
                lista_clientes[esta]["email"] = email
                
                print("\n\033[32mCliente modificado correctamente.\033[0m")
                pregunta_eleccion_otra = obtener_caracter("Desea hacer otra modificacion? Y/N\n")
                if pregunta_eleccion_otra == "Y":
                    texto = ""
                    inicio_modificar(texto)
                    modificar_clientes()
            else:
                print("\n\033[31mModificacion de cliente cancelada.\033[0m")
    
    texto = ""
    inicio_modificar(texto)
