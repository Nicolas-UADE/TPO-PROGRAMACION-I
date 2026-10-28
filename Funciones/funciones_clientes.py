from Funciones.funciones_uni import (
    obtener_caracter,
    obtener_entero,
    buscar_por_id,
    inicio_alta,
    inicio_baja,
    inicio_modificar,
    inicio_listado,
    buscar_por_nombre,
    validar_email,
)
from modulos.listas import ELIMINADO, lista_clientes

def obtener_cliente(indice):
    assert indice >=0

    cliente=lista_clientes[indice] #HACERLO CON UN ARCHIVO, DESDE EL JSON
    if cliente== ELIMINADO:
        raise ValueError("El Cliente fue dado de baja")

def alta_clientes():
    """
    Registra un nuevo cliente pidiendo sus datos personales.
    Valida formato de email, genera ID automático y pide confirmación antes de guardar.
    """
    texto = "ALTA DE CLIENTES"
    inicio_alta(texto)

    try:
        # Captura de datos básicos
        nombre = obtener_caracter("Nombre y apellido:\n.").upper()
        dni = obtener_entero("DNI:\n.", 1000000, 99999999)
        telefono = obtener_entero("Telefono:\n.", 1000000000, 9999999999)
        email = obtener_caracter("Email:\n.").lower()

        # Bucle de validación para asegurar un email correcto
        while validar_email(email) == False:
            print("\nIngrese un mail valido.\n")
            email = obtener_caracter("Email:\n.").lower()

        # Conversión a string para evitar inconvenientes de formato
        el_dni = str(dni)
        el_telefono = str(telefono)

        # Autoincrementable simple para el ID
        nuevo_id = len(lista_clientes) + 1

        cliente = {
            "id": nuevo_id,
            "nombre": nombre,
            "dni": el_dni,
            "telefono": el_telefono,
            "email": email,
        }

        # Confirmación final de guardado
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
    except (FileNotFoundError, OSError)as error: #futuro, agregar json.JSONDecodeError
        print(f'Error!{error}')

def listado_clientes():
    """
    Muestra la lista de clientes activos o busca uno en específico por nombre o ID.
    Ignora a los usuarios dados de baja (marcados como ELIMINADO).
    """
    texto = "LISTADO CLIENTES"
    inicio_listado(texto)
 
    try:
        pregunta_orden = obtener_entero(
            "\nElija metodo de ordenamiento. \n[1] ID\n[2] Buscar por nombre\n[3] Buscar por codigo.\n-1 para salir\n.",
            -1,
            3,
        )
        match pregunta_orden:
            case -1:
                return
            case 0:
                # Reintento rápido si selecciona una opción fuera del menú
                pregunta_orden = obtener_entero(
                    "\nElija metodo de ordenamiento.\n[1] ID\n[2] Buscar por nombre\n[3] Buscar por codigo.\n-1 para salir\n.",
                    -1,
                    3,
                )
            case 1:
                # Imprime todos los clientes que sigan activos en el sistema
                buscar_por_id()
                for cliente in lista_clientes:
                    if cliente != ELIMINADO:
                        print(
                            f"|{cliente['id']:<20} | {cliente['nombre']:<20} | {cliente['dni']:<20} | {cliente['telefono']:<20} | {cliente['email']:<20}"
                        )
 
            case 2:
                # Búsqueda por Nombre con reintento si no existe
                pregunta_nombre = obtener_caracter(
                    "\n\nIngrese nombre del cliente a buscar.\n-1 para salir\n."
                )
 
                if pregunta_nombre == "-1":
                    return
 
                while True:
                    esta = buscar_por_nombre(lista_clientes, pregunta_nombre)
                    if esta != -2:
                        try:
                            cliente_encontrado = obtener_cliente(esta)
                            break
                        except ValueError:
                            # Estaba en la lista pero dado de baja
                            pass
 
                    print("Cliente inexistente.")
                    pregunta_nombre = obtener_caracter(
                        "\nIngrese nombre del cliente a buscar.\n-1 para salir\n."
                    )
                    if pregunta_nombre == "-1":
                        return
 
                print(
                    f"|{cliente_encontrado['id']:<20} | {cliente_encontrado['nombre']:<20} | {cliente_encontrado['dni']:<20} | {cliente_encontrado['telefono']:<20} | {cliente_encontrado['email']:<20}"
                )
 
            case 3:
                # Búsqueda por ID (código) con reintento si no existe
                pregunta_codigo = obtener_entero(
                    "\n\nIngrese código del cliente a buscar.\n-1 para salir\n.",
                    -1,
                    1000000,
                )
 
                match pregunta_codigo:
                    case 0:
                        pregunta_codigo = obtener_entero(
                            "\nIngrese código del cliente a buscar.\n-1 para salir\n.",
                            -1,
                            1000000,
                        )
                    case -1:
                        return
 
                while True:
                    esta = buscar_por_id(lista_clientes, pregunta_codigo)
                    if esta != -2:
                        try:
                            cliente_encontrado = obtener_cliente(esta)
                            break
                        except ValueError:
                            # Estaba en la lista pero dado de baja
                            pass
 
                    print("Cliente inexistente.")
                    pregunta_codigo = obtener_entero(
                        "\nIngrese código del cliente a buscar.\n-1 para salir\n.",
                        -1,
                        1000000,
                    )
                    if pregunta_codigo == -1:
                        return
 
                print(
                    f"\n|{cliente_encontrado['id']:<20} | {cliente_encontrado['nombre']:<20} | {cliente_encontrado['dni']:<20} | {cliente_encontrado['telefono']:<20} | {cliente_encontrado['email']:<20}"
                )
 
    except (FileNotFoundError, OSError)as error: #futuro, agregar json.JSONDecodeError
            print(f'Error!{error}')


    texto = ""
    inicio_listado(texto)
 
 
def baja_clientes():
    """
    Aplica una baja lógica a un cliente reemplazándolo por la constante 'ELIMINADO'
    en la lista, preservando así la integridad de los índices.
    """
    texto = "BAJA DE CLIENTES"
    inicio_baja(texto)
 
    try:
        pregunta_codigo = obtener_entero(
            "\n\nIngrese código del cliente a eliminar.\n-1 para salir\n.", -1, 1000000
        )
 
        match pregunta_codigo:
            case 0:
                pregunta_codigo = obtener_entero(
                    "\nIngrese código del cliente a eliminar.\n-1 para salir\n.",
                    -1,
                    1000000,
                )
            case -1:
                return
 
        # Validación de existencia del ID (y de que no esté ya dado de baja)
        while True:
            esta = buscar_por_id(lista_clientes, pregunta_codigo)
            if esta != -2:
                try:
                    obtener_cliente(esta)
                    break
                except ValueError:
                    pass
 
            print("Cliente inexistente.")
            pregunta_codigo = obtener_entero(
                "\nIngrese código del cliente a eliminar.\n-1 para salir\n.",
                -1,
                1000000,
            )
            if pregunta_codigo == -1:
                return
 
        # Confirmación de la baja
        pregunta_seguridad = obtener_caracter(
            f"\nEsta seguro de eliminar al cliente {pregunta_codigo}? Y/N\n."
        ).upper()
 
        if pregunta_seguridad == "Y":
            # Se reemplaza por constante ELIMINADO para mantener las posiciones de la lista
            lista_clientes[esta] = ELIMINADO
            print("\n\033[32mCliente eliminado correctamente.\033[0m")
        else:
            print("\n\033[31mBaja de cliente cancelada.\033[0m")
 
    except (FileNotFoundError, OSError)as error: #futuro, agregar json.JSONDecodeError
            print(f'Error!{error}')
 
    texto = ""
    inicio_baja(texto)
 


def modificar_clientes():
    """
    Permite seleccionar y actualizar un campo específico (Nombre, DNI, Teléfono o Email)
    de un cliente existente en el sistema.
    """
    texto = "MODIFICAR CLIENTES"
    inicio_modificar(texto)
 
    try:
        pregunta_codigo = obtener_entero(
            "\n\nIngrese código del cliente a modificar.\n-1 para salir\n.", -1, 1000000
        )
 
        match pregunta_codigo:
            case 0:
                pregunta_codigo = obtener_entero(
                    "\nIngrese código del cliente a modificar.\n-1 para salir\n.",
                    -1,
                    1000000,
                )
            case -1:
                return
 
        # Comprobación de que el ID existe (y de que no esté dado de baja)
        while True:
            esta = buscar_por_id(lista_clientes, pregunta_codigo)
            if esta != -2:
                try:
                    obtener_cliente(esta)
                    break
                except ValueError:
                    pass
 
            print("Cliente inexistente.")
            pregunta_codigo = obtener_entero(
                "\nIngrese código del cliente a modificar.\n-1 para salir\n.",
                -1,
                1000000,
            )
            if pregunta_codigo == -1:
                return
 
        # Selección de campo a modificar
        pregunta_eleccion = obtener_entero(
            "Que quieres modificar.\n[1] Nombre\n[2] DNI\n[3] Telefono\n[4] Email\n.",
            1,
            4,
        )
 
        match pregunta_eleccion:
            case 1:
                # Cambio de Nombre
                nombre = obtener_caracter("Nombre y apellido:\n.").upper()
                pregunta_seguridad = obtener_caracter(
                    f"\nEsta seguro de modificar el cliente {pregunta_codigo}? Y/N\n."
                ).upper()
 
                if pregunta_seguridad == "Y":
                    lista_clientes[esta]["nombre"] = nombre
                    print("\n\033[32mCliente modificado correctamente.\033[0m")
 
                    pregunta_eleccion_otra = obtener_caracter(
                        "Desea hacer otra modificacion? Y/N\n"
                    ).upper()
                    if pregunta_eleccion_otra == "Y":
                        texto = ""
                        inicio_modificar(texto)
                        modificar_clientes()
                else:
                    print("\n\033[31mModificacion de cliente cancelada.\033[0m")
 
            case 2:
                # Cambio de DNI
                dni = obtener_entero("DNI:\n.", 1000000, 99999999)
                pregunta_seguridad = obtener_caracter(
                    f"\nEsta seguro de modificar el cliente {pregunta_codigo}? Y/N\n."
                ).upper()
 
                if pregunta_seguridad == "Y":
                    el_dni = str(dni)
                    lista_clientes[esta]["dni"] = el_dni
                    print("\n\033[32mCliente modificado correctamente.\033[0m")
 
                    pregunta_eleccion_otra = obtener_caracter(
                        "Desea hacer otra modificacion? Y/N\n"
                    ).upper()
                    if pregunta_eleccion_otra == "Y":
                        texto = ""
                        inicio_modificar(texto)
                        modificar_clientes()
                else:
                    print("\n\033[31mModificacion de cliente cancelada.\033[0m")
 
            case 3:
                # Cambio de Teléfono
                telefono = obtener_entero("Telefono:\n.", 1000000000, 9999999999)
                pregunta_seguridad = obtener_caracter(
                    f"\nEsta seguro de modificar el cliente {pregunta_codigo}? Y/N\n."
                ).upper()
 
                if pregunta_seguridad == "Y":
                    el_telefono = str(telefono)
                    lista_clientes[esta]["telefono"] = el_telefono
                    print("\n\033[32mCliente modificado correctamente.\033[0m")
 
                    pregunta_eleccion_otra = obtener_caracter(
                        "Desea hacer otra modificacion? Y/N\n"
                    ).upper()
                    if pregunta_eleccion_otra == "Y":
                        texto = ""
                        inicio_modificar(texto)
                        modificar_clientes()
                else:
                    print("\n\033[31mModificacion de cliente cancelada.\033[0m")
 
    except (FileNotFoundError, OSError)as error: #futuro, agregar json.JSONDecodeError
        print(f'Error!{error}')

    texto = ""
    inicio_modificar(texto)
