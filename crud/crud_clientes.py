import listas

from listas import (
    CLIENTES,
    CLIENTES_ID,
    CLIENTES_NOMBRE,
    CLIENTES_APELLIDO,
    CLIENTES_DNI,
    CLIENTES_TELEFONO,
    CLIENTES_EMAIL,
    clientes_id_individual,
    clientes_nombre_individual,
    ELIMINADO,
)

from Funciones.funciones import obtener_caracter, obtener_entero
from Funciones.funciones import busqueda_secuencial, buscar, generador_de_id


def clientes():
    print("==========\nCLIENTES\n==========")

    # Se consulta listas.ADMIN directamente para que tome el valor
    # actualizado por el login/menu.
    if listas.ADMIN:
        ask = obtener_entero(
            "0. Retroceder\n"
            "1. Listado de clientes\n"
            "2. Baja de cliente\n"
            "3. Alta de cliente\n"
            "4. Modificar cliente...\n",
            0,
            4,
        )

        match ask:
            case 0:
                return
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
            1,
        )

        match ask:
            case 0:
                return
            case 1:
                listar_clientes()


def alta_cliente():
    print("\n\n==========ALTA DE CLIENTES==========")

    nombre = obtener_caracter("\nIngrese nombre del cliente... ").upper()
    apellido = obtener_caracter("Ingrese apellido del cliente... ").upper()

    dni = obtener_entero(
        "Ingrese DNI del cliente... ",
        1000000,
        99999999,
    )

    telefono = obtener_entero(
        "Ingrese teléfono del cliente... ",
        100000000,
        9999999999,
    )

    email = obtener_caracter("Ingrese email del cliente... ")

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
            email,
        ])

        clientes_id_individual.append(codigo)
        clientes_nombre_individual.append(nombre)

        print("\n\nCliente agregado correctamente.\n")
        print("===================")
    else:
        print("\nAlta de cliente cancelada.")
        print("===================")


def baja_cliente():
    print("\n\n==========BAJA DE CLIENTES==========")

    pregunta_codigo = obtener_entero(
        "\nIngrese código del cliente a eliminar. -1 Para salir... ",
        -1,
        1000000,
    )

    if pregunta_codigo == -1:
        return

    pos = busqueda_secuencial(clientes_id_individual, pregunta_codigo)

    while pos == -1 or clientes_id_individual[pos] == ELIMINADO:
        print("Cliente inexistente.")

        pregunta_codigo = obtener_entero(
            "\nIngrese código del cliente a eliminar. -1 Para salir... ",
            -1,
            1000000,
        )

        if pregunta_codigo == -1:
            return

        pos = busqueda_secuencial(clientes_id_individual, pregunta_codigo)

    pregunta_seguridad = obtener_caracter(
        f"\nEsta seguro de eliminar el cliente {pregunta_codigo}? Y/N..."
    ).upper()

    if pregunta_seguridad == "Y":
        CLIENTES[pos][CLIENTES_ID] = ELIMINADO
        clientes_id_individual[pos] = ELIMINADO

        print("Cliente eliminado correctamente.")
    else:
        print("\nBaja de cliente cancelada.")

    print("===================")


def modificar_cliente():
    print("\n\n==========MODIFICACION DE CLIENTES==========")

    pregunta_codigo = obtener_entero(
        "\nIngrese código del cliente... -1 Para salir... ",
        -1,
        1000000,
    )

    if pregunta_codigo == -1:
        return

    pos = busqueda_secuencial(clientes_id_individual, pregunta_codigo)

    if pos == -1 or clientes_id_individual[pos] == ELIMINADO:
        print("Cliente inexistente.")
        return

    nuevo_nombre = obtener_caracter("Ingrese nuevo nombre... ").upper()
    CLIENTES[pos][CLIENTES_NOMBRE] = nuevo_nombre
    clientes_nombre_individual[pos] = nuevo_nombre

    nuevo_apellido = obtener_caracter("Ingrese nuevo apellido... ").upper()
    CLIENTES[pos][CLIENTES_APELLIDO] = nuevo_apellido

    nuevo_dni = obtener_entero(
        "Ingrese nuevo DNI... ",
        1000000,
        99999999,
    )
    CLIENTES[pos][CLIENTES_DNI] = nuevo_dni

    nuevo_telefono = obtener_entero(
        "Ingrese nuevo teléfono... ",
        100000000,
        9999999999,
    )
    CLIENTES[pos][CLIENTES_TELEFONO] = nuevo_telefono

    nuevo_email = obtener_caracter("Ingrese nuevo email... ")
    CLIENTES[pos][CLIENTES_EMAIL] = nuevo_email

    print("Cliente modificado correctamente.")
    print("===================")


def _clientes_activos():
    """Devuelve los clientes que no fueron dados de baja."""
    return [
        cliente for cliente in CLIENTES
        if cliente[CLIENTES_ID] != ELIMINADO
    ]


def listar_clientes():
    print("\n\n==========LISTA DE CLIENTES==========")

    pregunta_orden = obtener_entero(
        "Elija metodo de listado.\n"
        "1. ID\n"
        "2. ALFABETICAMENTE\n"
        "3. Buscar por nombre\n"
        "4. Buscar por codigo\n"
        "-1. Salir\n",
        -1,
        4,
    )

    if pregunta_orden == -1:
        return

    activos = _clientes_activos()

    if pregunta_orden == 1:
        # Ordena SOLO clientes, no PRODUCTOS.
        resultado = sorted(activos, key=lambda cliente: cliente[CLIENTES_ID])

        print("\nClientes ordenados por ID:")
        for cliente in resultado:
            print(cliente)

    elif pregunta_orden == 2:
        # Ordena SOLO clientes por apellido y luego nombre.
        resultado = sorted(
            activos,
            key=lambda cliente: (
                cliente[CLIENTES_APELLIDO],
                cliente[CLIENTES_NOMBRE],
            ),
        )

        print("\nClientes ordenados alfabeticamente:")
        for cliente in resultado:
            print(cliente)

    elif pregunta_orden == 3:
        pregunta = obtener_caracter(
            "\nIngrese nombre del cliente... "
        ).upper()

        encontrados = [
            cliente
            for cliente in activos
            if pregunta in cliente[CLIENTES_NOMBRE]
        ]

        if not encontrados:
            print("Cliente no encontrado.")
        else:
            print(f"\nCantidad de clientes encontrados: {len(encontrados)}")
            for cliente in encontrados:
                print(cliente)

    elif pregunta_orden == 4:
        pregunta = obtener_entero(
            "\nIngrese codigo del cliente... ",
            100000,
            1000000,
        )

        encontrados = [
            cliente
            for cliente in activos
            if cliente[CLIENTES_ID] == pregunta
        ]

        if not encontrados:
            print("Cliente no encontrado.")
        else:
            print("\nCliente encontrado:")
            for cliente in encontrados:
                print(cliente)

    print("===================")

