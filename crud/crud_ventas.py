import re
import listas
from functools import reduce

from listas import (
    ELIMINADO,
    PRODUCTOS,
    PRODUCTOS_CODIGO,
    PRODUCTOS_NOMBRE,
    PRODUCTOS_CATEGORIA,
    PRODUCTOS_PRECIO,
    PRODUCTOS_STOCK,
    PRODUCTOS_DESCUENTO,
    VENTAS,
    VENTAS_ID,
    VENTAS_CLIENTE,
    VENTAS_PRODUCTO,
    VENTAS_CATEGORIA,
    VENTAS_FECHA,
    VENTAS_CANTIDAD,
    VENTAS_PRECIO_UNITARIO,
    VENTAS_IMPORTE,
)

from crud.crud_clientes import lista_clientes

from Funciones.funciones import (
    inicio,
    inicio_alta,
    inicio_baja,
    inicio_modificar,
    inicio_listado,
    obtener_caracter,
    obtener_entero,
    buscar_por_id,
    busqueda_por_codigo,
    redondeo,
)

from Funciones.estadisticas_ventas import (
    resumen_estadistico,
    redondear_precio,
)


def ventas():

    inicio("VENTAS")

    if listas.ADMIN == True:

        ask = obtener_entero(
            "0. Retroceder\n"
            "1. Listado de ventas\n"
            "2. Baja de venta\n"
            "3. Alta de venta\n"
            "4. Modificar venta\n"
            "5. Estadisticas\n.",
            0,
            5
        )

        match ask:

            case 0:
                return

            case 1:
                listar_ventas()

            case 2:
                baja_venta()

            case 3:
                alta_venta()

            case 4:
                modificar_venta()

            case 5:
                resumen_estadistico()

    else:

        ask = obtener_entero(
            "0. Retroceder\n"
            "1. Listado de ventas\n"
            "2. Estadisticas\n.",
            0,
            2
        )

        match ask:

            case 0:
                return

            case 1:
                listar_ventas()

            case 2:
                resumen_estadistico()


def confirmar(texto):

    respuesta = obtener_caracter(texto).upper()

    while respuesta != "Y" and respuesta != "N":

        respuesta = obtener_caracter(
            "Ingrese Y o N\n."
        ).upper()

    return respuesta


def generar_id_venta():

    return 100001 + len(VENTAS)


def pedir_fecha():

    patron = r"^[0-9]{2}/[0-9]{2}/[0-9]{4}$"

    fecha = obtener_caracter(
        "Ingrese fecha DD/MM/AAAA\n."
    )

    valida = False

    while valida == False:

        if re.match(patron, fecha) != None:

            partes = fecha.split("/")

            dia = int(partes[0])
            mes = int(partes[1])

            if dia >= 1 and dia <= 31 and mes >= 1 and mes <= 12:

                valida = True

        if valida == False:

            print("Fecha invalida.")

            fecha = obtener_caracter(
                "Ingrese fecha DD/MM/AAAA\n."
            )

    return fecha


def buscar_venta(id_venta):

    posiciones = []

    for i in range(len(VENTAS)):

        if VENTAS[i][VENTAS_ID] == id_venta:

            posiciones.append(i)

    return posiciones


def filtrar_ventas(columna, valor):

    resultado = []

    for fila in VENTAS:

        if fila[VENTAS_ID] != ELIMINADO and fila[columna] == valor:

            resultado.append(fila)

    return resultado


def alta_venta():

    inicio_alta("ALTA DE VENTAS")

    id_cliente = obtener_entero(
        "Ingrese ID del cliente. -1 Para salir\n.",
        -1,
        1000000
    )

    if id_cliente == -1:
        return

    while buscar_por_id(lista_clientes, id_cliente) == -2:

        print("Cliente inexistente.")

        id_cliente = obtener_entero(
            "Ingrese otro ID. -1 Para salir\n.",
            -1,
            1000000
        )

        if id_cliente == -1:
            return

    id_venta = generar_id_venta()

    fecha = pedir_fecha()

    venta_temporal = []

    seguir = "Y"

    while seguir == "Y":

        codigo = obtener_entero(
            "Ingrese codigo del producto. -1 Para cancelar\n.",
            -1,
            1000000
        )

        if codigo == -1:
            return

        pos_producto = busqueda_por_codigo(
            PRODUCTOS,
            codigo
        )

        while pos_producto == -1:

            print("Producto inexistente.")

            codigo = obtener_entero(
                "Ingrese otro codigo. -1 Para cancelar\n.",
                -1,
                1000000
            )

            if codigo == -1:
                return

            pos_producto = busqueda_por_codigo(
                PRODUCTOS,
                codigo
            )

        codigos_agregados = list(
            map(
                lambda fila: fila[VENTAS_PRODUCTO],
                venta_temporal
            )
        )

        if codigo in codigos_agregados:

            print(
                "Ese producto ya fue agregado a la venta."
            )

        elif PRODUCTOS[pos_producto][PRODUCTOS_STOCK] == 0:

            print("Producto sin stock.")

        else:

            stock = PRODUCTOS[
                pos_producto
            ][PRODUCTOS_STOCK]

            cantidad = obtener_entero(
                "Ingrese cantidad\n.",
                1,
                stock
            )

            precio = PRODUCTOS[
                pos_producto
            ][PRODUCTOS_PRECIO]

            descuento = PRODUCTOS[
                pos_producto
            ][PRODUCTOS_DESCUENTO]

            precio_final = redondear_precio(
                precio - precio * descuento / 100
            )

            importe = redondear_precio(
                precio_final * cantidad
            )

            venta_temporal.append([
                id_venta,
                id_cliente,
                codigo,
                PRODUCTOS[pos_producto][PRODUCTOS_CATEGORIA],
                fecha,
                cantidad,
                precio_final,
                importe
            ])

            print(
                f"{PRODUCTOS[pos_producto][PRODUCTOS_NOMBRE]} "
                f"agregado. Importe: {redondeo(importe)}"
            )

        seguir = confirmar(
            "Desea agregar otro producto? Y/N\n."
        )

    if len(venta_temporal) == 0:

        print("No se agregaron productos.")

        return

    total = reduce(
        lambda acumulador, fila:
        acumulador + fila[VENTAS_IMPORTE],
        venta_temporal,
        0
    )

    print(
        "Total de la venta:",
        redondeo(total)
    )

    if confirmar(
        "Confirma la venta? Y/N\n."
    ) == "Y":

        for fila in venta_temporal:

            VENTAS.append(fila)

            pos_producto = busqueda_por_codigo(
                PRODUCTOS,
                fila[VENTAS_PRODUCTO]
            )

            PRODUCTOS[pos_producto][PRODUCTOS_STOCK] = (
                PRODUCTOS[pos_producto][PRODUCTOS_STOCK]
                - fila[VENTAS_CANTIDAD]
            )

        print(
            "\n\033[32mVenta agregada correctamente.\033[0m"
        )

    else:

        print(
            "\n\033[31mAlta de venta cancelada.\033[0m"
        )


def mostrar_ventas(filas):

    print("-" * 105)

    print(
        f"|{'ID':<9}"
        f"|{'FECHA':<12}"
        f"|{'CLIENTE':<9}"
        f"|{'CODIGO':<9}"
        f"|{'PRODUCTO':<16}"
        f"|{'CANT':<7}"
        f"|{'IMPORTE':<15}"
    )

    print("-" * 105)

    for fila in filas:

        if fila[VENTAS_ID] != ELIMINADO:

            pos = busqueda_por_codigo(
                PRODUCTOS,
                fila[VENTAS_PRODUCTO]
            )

            nombre = "ELIMINADO"

            if pos != -1:

                nombre = PRODUCTOS[
                    pos
                ][PRODUCTOS_NOMBRE]

            print(
                f"|{fila[VENTAS_ID]:<9}"
                f"|{fila[VENTAS_FECHA]:<12}"
                f"|{fila[VENTAS_CLIENTE]:<9}"
                f"|{fila[VENTAS_PRODUCTO]:<9}"
                f"|{nombre:<16}"
                f"|{fila[VENTAS_CANTIDAD]:<7}"
                f"|{redondeo(fila[VENTAS_IMPORTE]):<15}"
            )

    print("-" * 105)


def listar_ventas():

    inicio_listado("LISTA DE VENTAS")

    opcion = obtener_entero(
        "0. Salir\n"
        "1. Todas por ID\n"
        "2. Buscar por ID\n"
        "3. Buscar por cliente\n"
        "4. Buscar por producto\n"
        "5. Buscar por categoria\n"
        "6. Buscar por fecha\n.",
        0,
        6
    )

    if opcion == 0:
        return

    if opcion == 1:

        activas = list(
            filter(
                lambda fila: fila[VENTAS_ID] != ELIMINADO,
                VENTAS
            )
        )

        mostrar_ventas(
            sorted(
                activas,
                key=lambda fila: fila[VENTAS_ID]
            )
        )

        return

    if opcion == 2:

        valor = obtener_entero(
            "Ingrese ID de venta\n.",
            1,
            1000000
        )

        filas = filtrar_ventas(
            VENTAS_ID,
            valor
        )

    elif opcion == 3:

        valor = obtener_entero(
            "Ingrese ID del cliente\n.",
            1,
            1000000
        )

        filas = filtrar_ventas(
            VENTAS_CLIENTE,
            valor
        )

    elif opcion == 4:

        valor = obtener_entero(
            "Ingrese codigo del producto\n.",
            1,
            1000000
        )

        filas = filtrar_ventas(
            VENTAS_PRODUCTO,
            valor
        )

    elif opcion == 5:

        valor = obtener_caracter(
            "Ingrese categoria\n."
        ).upper()

        filas = filtrar_ventas(
            VENTAS_CATEGORIA,
            valor
        )

    else:

        valor = pedir_fecha()

        filas = filtrar_ventas(
            VENTAS_FECHA,
            valor
        )

    if len(filas) == 0:

        print("No se encontraron ventas.")

    else:

        mostrar_ventas(filas)


def baja_venta():

    inicio_baja("BAJA DE VENTAS")

    id_venta = obtener_entero(
        "Ingrese ID de venta. -1 Para salir\n.",
        -1,
        1000000
    )

    if id_venta == -1:
        return

    posiciones = buscar_venta(id_venta)

    while len(posiciones) == 0:

        print("Venta inexistente.")

        id_venta = obtener_entero(
            "Ingrese otro ID. -1 Para salir\n.",
            -1,
            1000000
        )

        if id_venta == -1:
            return

        posiciones = buscar_venta(
            id_venta
        )

    if confirmar(
        f"Esta seguro de eliminar la venta {id_venta}? Y/N\n."
    ) == "Y":

        for pos in posiciones:

            codigo = VENTAS[
                pos
            ][VENTAS_PRODUCTO]

            cantidad = VENTAS[
                pos
            ][VENTAS_CANTIDAD]

            pos_producto = busqueda_por_codigo(
                PRODUCTOS,
                codigo
            )

            if pos_producto != -1:

                PRODUCTOS[
                    pos_producto
                ][PRODUCTOS_STOCK] = (
                    PRODUCTOS[
                        pos_producto
                    ][PRODUCTOS_STOCK]
                    + cantidad
                )

            VENTAS[pos][VENTAS_ID] = ELIMINADO

        print(
            "\n\033[32mVenta eliminada correctamente.\033[0m"
        )

    else:

        print(
            "\n\033[31mBaja de venta cancelada.\033[0m"
        )


def modificar_venta():

    inicio_modificar(
        "MODIFICACION DE VENTAS"
    )

    id_venta = obtener_entero(
        "Ingrese ID de venta. -1 Para salir\n.",
        -1,
        1000000
    )

    if id_venta == -1:
        return

    posiciones = buscar_venta(id_venta)

    while len(posiciones) == 0:

        print("Venta inexistente.")

        id_venta = obtener_entero(
            "Ingrese otro ID. -1 Para salir\n.",
            -1,
            1000000
        )

        if id_venta == -1:
            return

        posiciones = buscar_venta(
            id_venta
        )

    opcion = obtener_entero(
        "0. Salir\n"
        "1. Cambiar cliente\n"
        "2. Cambiar fecha\n"
        "3. Cambiar cantidad\n.",
        0,
        3
    )

    if opcion == 0:
        return

    if opcion == 1:

        nuevo = obtener_entero(
            "Nuevo ID de cliente\n.",
            1,
            1000000
        )

        while buscar_por_id(
            lista_clientes,
            nuevo
        ) == -2:

            print("Cliente inexistente.")

            nuevo = obtener_entero(
                "Nuevo ID de cliente\n.",
                1,
                1000000
            )

        if confirmar(
            "Confirma la modificacion? Y/N\n."
        ) == "Y":

            for pos in posiciones:

                VENTAS[
                    pos
                ][VENTAS_CLIENTE] = nuevo

            print(
                "\n\033[32mCliente modificado correctamente.\033[0m"
            )

    elif opcion == 2:

        nueva_fecha = pedir_fecha()

        if confirmar(
            "Confirma la modificacion? Y/N\n."
        ) == "Y":

            for pos in posiciones:

                VENTAS[
                    pos
                ][VENTAS_FECHA] = nueva_fecha

            print(
                "\n\033[32mFecha modificada correctamente.\033[0m"
            )

    else:

        for pos in posiciones:

            print(
                "Codigo:",
                VENTAS[pos][VENTAS_PRODUCTO],
                "Cantidad:",
                VENTAS[pos][VENTAS_CANTIDAD]
            )

        codigo = obtener_entero(
            "Codigo del producto a modificar\n.",
            1,
            1000000
        )

        pos_venta = -1

        for pos in posiciones:

            if VENTAS[pos][VENTAS_PRODUCTO] == codigo:

                pos_venta = pos

        if pos_venta == -1:

            print(
                "El producto no pertenece a la venta."
            )

            return

        pos_producto = busqueda_por_codigo(
            PRODUCTOS,
            codigo
        )

        if pos_producto == -1:

            print("Producto inexistente.")

            return

        anterior = VENTAS[
            pos_venta
        ][VENTAS_CANTIDAD]

        maximo = (
            anterior
            + PRODUCTOS[
                pos_producto
            ][PRODUCTOS_STOCK]
        )

        nueva = obtener_entero(
            f"Nueva cantidad. Maximo: {maximo}\n.",
            1,
            maximo
        )

        if confirmar(
            "Confirma la modificacion? Y/N\n."
        ) == "Y":

            diferencia = nueva - anterior

            PRODUCTOS[
                pos_producto
            ][PRODUCTOS_STOCK] = (
                PRODUCTOS[
                    pos_producto
                ][PRODUCTOS_STOCK]
                - diferencia
            )

            VENTAS[
                pos_venta
            ][VENTAS_CANTIDAD] = nueva

            VENTAS[
                pos_venta
            ][VENTAS_IMPORTE] = redondear_precio(
                nueva
                * VENTAS[
                    pos_venta
                ][VENTAS_PRECIO_UNITARIO]
            )

            print(
                "\n\033[32mCantidad modificada correctamente.\033[0m"
            )