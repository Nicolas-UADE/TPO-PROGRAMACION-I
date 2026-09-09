from listas import CLIENTES, CLIENTES_ID, CLIENTES_NOMBRE, CLIENTES_APELLIDO, CLIENTES_DNI, CLIENTES_TELEFONO, CLIENTES_EMAIL
from listas import clientes_id_individual, clientes_nombre_individual, ELIMINADO, ADMIN

from Funciones.funciones import obtener_caracter, obtener_entero
from Funciones.funciones import busqueda_secuencial, ordenar_por_codigo
from Funciones.funciones import ordenar_alfabeticamente, volver_al_menu
from Funciones.funciones import buscar, generador_de_id


def clientes():
    print("==========\nCLIENTES\n==========")

    if ADMIN == True:
        ask = obtener_entero(
            "0. Retroceder\n"
            "1. Listado de clientes\n"
            "2. Baja de cliente\n"
            "3. Alta de cliente\n"
            "4. Modificar cliente...",
            0,
            4,
        )

        match ask:
            case 0:
                volver_al_menu()

            case 1:
                listar_clientes()

            case 2:
                baja_cliente()

            case 3:
                alta_cliente()

            case 4:
                modificar_cliente()

    else:
        ask = obtener_entero(
            "0. Retroceder\n"
            "1. Listado de clientes\n",
            0,
            1
        )

        match ask:
            case 0:
                volver_al_menu()

            case 1:
                listar_clientes()


def alta_cliente():

    print("\n\n==========ALTA DE CLIENTES==========")

    nombre = obtener_caracter(
        "\nIngrese nombre del cliente... "
    ).upper()

    apellido = obtener_caracter(
        "Ingrese apellido del cliente... "
    ).upper()

    dni = obtener_entero(
        "Ingrese DNI del cliente... ",
        1000000,
        99999999
    )

    telefono = obtener_entero(
        "Ingrese teléfono del cliente... ",
        100000000,
        9999999999
    )

    email = obtener_caracter(
        "Ingrese email del cliente... "
    )

    codigo = generador_de_id(clientes_id_individual)

    pregunta_seguridad = obtener_caracter(
        "Esta seguro de agregar este cliente? Y/N..."
    ).upper()

    if pregunta_seguridad == "Y":

        CLIENTES.append([
            codigo,
            nombre,
            apellido,
            dni,
            telefono,
            email
        ])

        clientes_id_individual.append(codigo)
        clientes_nombre_individual.append(nombre)

        print("\n\nCliente agregado correctamente.\n\n")
        print("===================")

    else:

        print(
            "Alta de cliente cancelada...\n"
            "Volviendo al menu principal..."
        )

        print("===================")

        volver_al_menu()


def baja_cliente():

    print("\n\n==========BAJA DE CLIENTES==========")

    pregunta_codigo = obtener_entero(
        "\n\nIngrese código del cliente a eliminar. "
        "-1 Para salir...",
        -1,
        1000000
    )

    while pregunta_codigo == 0:

        pregunta_codigo = obtener_entero(
            "\nIngrese código del cliente a eliminar. "
            "-1 Para salir...",
            -1,
            1000000
        )

    if pregunta_codigo == -1:
        volver_al_menu()

    pos = busqueda_secuencial(
        clientes_id_individual,
        pregunta_codigo
    )

    while pos == -1:

        print("Cliente inexistente.")

        pregunta_codigo = obtener_entero(
            "\nIngrese código del cliente a eliminar. "
            "-1 Para salir...",
            -1,
            1000000
        )

        if pregunta_codigo == -1:
            volver_al_menu()

        pos = busqueda_secuencial(
            clientes_id_individual,
            pregunta_codigo
        )

    pregunta_seguridad = obtener_caracter(
        f"\nEsta seguro de eliminar el cliente "
        f"{pregunta_codigo}? Y/N..."
    ).upper()

    if pregunta_seguridad == "Y":

        CLIENTES[pos][CLIENTES_ID] = ELIMINADO
        clientes_id_individual[pos] = ELIMINADO

        print("Cliente eliminado correctamente.")
        print("===================")

    else:

        print("\nBaja de cliente cancelada.")
        print("===================")


def modificar_cliente():

    print("\n\n==========MODIFICACION DE CLIENTES==========")

    pregunta_codigo = obtener_entero(
        "\nIngrese código del cliente... "
        "-1 Para salir...",
        -1,
        1000000
    )

    while pregunta_codigo == 0:

        pregunta_codigo = obtener_entero(
            "\nIngrese código del cliente... "
            "-1 Para salir...",
            -1,
            1000000
        )

    if pregunta_codigo == -1:
        volver_al_menu()

    pos = busqueda_secuencial(
        clientes_id_individual,
        pregunta_codigo
    )

    if pos == -1 or pos == ELIMINADO:

        print("Cliente inexistente.")

    else:

        nuevo_nombre = obtener_caracter(
            "Ingrese nuevo nombre... "
        ).upper()

        CLIENTES[pos][CLIENTES_NOMBRE] = nuevo_nombre
        clientes_nombre_individual[pos] = nuevo_nombre

        nuevo_apellido = obtener_caracter(
            "Ingrese nuevo apellido... "
        ).upper()

        CLIENTES[pos][CLIENTES_APELLIDO] = nuevo_apellido

        nuevo_dni = obtener_entero(
            "Ingrese nuevo DNI... ",
            1000000,
            99999999
        )

        CLIENTES[pos][CLIENTES_DNI] = nuevo_dni

        nuevo_telefono = obtener_entero(
            "Ingrese nuevo teléfono... ",
            100000000,
            9999999999
        )

        CLIENTES[pos][CLIENTES_TELEFONO] = nuevo_telefono

        nuevo_email = obtener_caracter(
            "Ingrese nuevo email... "
        )

        CLIENTES[pos][CLIENTES_EMAIL] = nuevo_email

        print("Cliente modificado correctamente.")
        print("===================")


def listar_clientes():

    print("\n\n==========LISTA DE CLIENTES==========")

    pregunta_orden = obtener_entero(
        "Elija metodo de ordenamiento. "
        "1.ID  "
        "2.ALFABETICAMENTE "
        "3.Buscar por nombre. "
        "4.Buscar por codigo. "
        "-1 para salir...",
        -1,
        4
    )

    if pregunta_orden == -1:
        volver_al_menu()

    if pregunta_orden == 0:

        pregunta_orden = obtener_entero(
            "Elija metodo de ordenamiento. "
            "1.ID  "
            "2.ALFABETICAMENTE "
            "3.Buscar por nombre. "
            "4.Buscar por codigo. "
            "-1 para salir...",
            -1,
            4
        )

    if pregunta_orden == 1:

        print()

        ordenar_por_codigo()

    if pregunta_orden == 2:

        print()

        ordenar_alfabeticamente()

    if pregunta_orden == 3:

        pregunta = obtener_caracter(
            "\nIngrese nombre del cliente..."
        ).upper()

        cuenta_busqueda, busqueda_posiciones = buscar(
            clientes_nombre_individual,
            pregunta
        )

        if cuenta_busqueda == 0:

            print("Cliente no encontrado...")

            from menu import menu_principal
            menu_principal()

        else:

            i = 0

            print(
                f"\nCantidad de clientes encontrados..."
                f"{cuenta_busqueda}\n"
            )

            while i < cuenta_busqueda:

                print(
                    f"\n{CLIENTES[busqueda_posiciones[i]]}\n"
                )

                i += 1

    if pregunta_orden == 4:

        pregunta = obtener_entero(
            "\nIngrese codigo del cliente...",
            100000,
            1000000
        )

        cuenta_busqueda, busqueda_posiciones = buscar(
            clientes_id_individual,
            pregunta
        )

        if cuenta_busqueda == 0:

            print("Cliente no encontrado...")

            from menu import menu_principal
            menu_principal()

        else:

            i = 0

            while i < cuenta_busqueda:

                print(
                    f"\nCliente encontrado..."
                    f"{cuenta_busqueda}\n"
                )

                print(
                    f"\n{CLIENTES[busqueda_posiciones[i]]}\n"
                )

                i += 1

    print("===================")