def ventas():
    print("==========\nVENTAS\n==========")
    from listas import ADMIN, PRODUCTOS, VENTAS

from Funciones.funciones import (
    busqueda_por_codigo,
    obtener_caracter,
    obtener_entero,
    volver_al_menu
)

from Promediogeneraldeventas import promedio_ventas
from promediodeventasporcategoria import promedio_ventas_categoria
from conteodeventas import contar_ventas
from conteoventasporcategoria import contar_ventas_categoria
from Porcentajedeventasporcategoria import porcentaje_ventas_categoria
from mayorymenorventa import mayor_menor_venta
from resumenestadisticodeventas import resumen_estadistico
from totalproductosvendidos import total_productos_vendidos


def busqueda_venta_por_id(VENTAS, id_venta):

    pos = 0

    while pos < len(VENTAS) and VENTAS[pos][0] != id_venta:
        pos = pos + 1

    if pos < len(VENTAS):
        return pos

    return -1


def ventas():

    print("\n==========")
    print("VENTAS")
    print("==========")

    if ADMIN == True:

        ask = obtener_entero(
            "0. Retroceder\n"
            "1. Listado de ventas\n"
            "2. Baja de venta\n"
            "3. Alta de venta\n"
            "4. Modificar venta\n"
            "5. Estadisticas de ventas...",
            0,
            5
        )

        match ask:

            case 0:
                volver_al_menu()

            case 1:
                listar_ventas()

            case 2:
                baja_venta()

            case 3:
                alta_venta()

            case 4:
                modificar_venta()

            case 5:
                menu_estadisticas_ventas()

    else:

        ask = obtener_entero(
            "0. Retroceder\n"
            "1. Listado de ventas\n",
            0,
            1
        )

        match ask:

            case 0:
                volver_al_menu()

            case 1:
                listar_ventas()


def alta_venta():

    print("\n========== ALTA DE VENTA ==========")

    id_venta = obtener_entero(
        "Ingrese ID de venta... -1 para salir...",
        -1,
        1000000
    )

    while id_venta == 0:

        id_venta = obtener_entero(
            "Ingrese ID de venta... -1 para salir...",
            -1,
            1000000
        )

    if id_venta == -1:
        volver_al_menu()
        return

    pos = busqueda_venta_por_id(
        VENTAS,
        id_venta
    )

    while pos != -1:

        print("Ya existe una venta con ese ID.")

        id_venta = obtener_entero(
            "Ingrese ID de venta... -1 para salir...",
            -1,
            1000000
        )

        if id_venta == -1:
            volver_al_menu()
            return

        pos = busqueda_venta_por_id(
            VENTAS,
            id_venta
        )

    id_producto = obtener_entero(
        "Ingrese ID del producto...",
        1,
        1000000
    )

    pos_producto = busqueda_por_codigo(
        PRODUCTOS,
        id_producto
    )

    while pos_producto == -1:

        print("Producto inexistente.")

        id_producto = obtener_entero(
            "Ingrese ID del producto...",
            1,
            1000000
        )

        pos_producto = busqueda_por_codigo(
            PRODUCTOS,
            id_producto
        )

    print("\n1. Alimentos")
    print("2. Limpieza")
    print("3. Bebidas")

    categoria = obtener_entero(
        "Ingrese categoria...",
        1,
        3
    )

    cantidad = obtener_entero(
        "Ingrese cantidad vendida...",
        1,
        100000
    )

    importe = float(
        input("Ingrese importe total de la venta...")
    )

    while importe <= 0:

        importe = float(
            input("Importe invalido. Reingrese...")
        )

    VENTAS.append(
        [
            id_venta,
            id_producto,
            categoria,
            cantidad,
            importe
        ]
    )

    print("\nVenta agregada correctamente.")


def baja_venta():

    print("\n========== BAJA DE VENTA ==========")

    id_venta = obtener_entero(
        "Ingrese ID de venta a eliminar...",
        -1,
        1000000
    )

    while id_venta == 0:

        id_venta = obtener_entero(
            "Ingrese ID de venta a eliminar...",
            -1,
            1000000
        )

    if id_venta == -1:
        volver_al_menu()
        return

    pos = busqueda_venta_por_id(
        VENTAS,
        id_venta
    )

    while pos == -1:

        print("Venta inexistente.")

        id_venta = obtener_entero(
            "Ingrese ID de venta a eliminar...",
            -1,
            1000000
        )

        if id_venta == -1:
            volver_al_menu()
            return

        pos = busqueda_venta_por_id(
            VENTAS,
            id_venta
        )

    pregunta_seguridad = obtener_caracter(
        f"Esta seguro de eliminar la venta {id_venta}? Y/N..."
    ).upper()

    if pregunta_seguridad == "Y":

        VENTAS.pop(pos)

        print("Venta eliminada correctamente.")

    else:

        print("Baja de venta cancelada.")


def modificar_venta():

    print("\n========== MODIFICACION DE VENTA ==========")

    id_venta = obtener_entero(
        "Ingrese ID de venta... -1 para salir...",
        -1,
        1000000
    )

    while id_venta == 0:

        id_venta = obtener_entero(
            "Ingrese ID de venta... -1 para salir...",
            -1,
            1000000
        )

    if id_venta == -1:
        volver_al_menu()
        return

    pos = busqueda_venta_por_id(
        VENTAS,
        id_venta
    )

    if pos == -1:

        print("Venta inexistente.")

    else:

        id_producto = obtener_entero(
            "Ingrese nuevo ID del producto...",
            1,
            1000000
        )

        pos_producto = busqueda_por_codigo(
            PRODUCTOS,
            id_producto
        )

        while pos_producto == -1:

            print("Producto inexistente.")

            id_producto = obtener_entero(
                "Ingrese nuevo ID del producto...",
                1,
                1000000
            )

            pos_producto = busqueda_por_codigo(
                PRODUCTOS,
                id_producto
            )

        VENTAS[pos][1] = id_producto

        print("\n1. Alimentos")
        print("2. Limpieza")
        print("3. Bebidas")

        categoria = obtener_entero(
            "Ingrese nueva categoria...",
            1,
            3
        )

        VENTAS[pos][2] = categoria

        cantidad = obtener_entero(
            "Ingrese nueva cantidad...",
            1,
            100000
        )

        VENTAS[pos][3] = cantidad

        importe = float(
            input("Ingrese nuevo importe...")
        )

        while importe <= 0:

            importe = float(
                input("Importe invalido. Reingrese...")
            )

        VENTAS[pos][4] = importe

        print("Venta modificada correctamente.")


def listar_ventas():

    print("\n========== LISTA DE VENTAS ==========")

    if len(VENTAS) == 0:

        print("No hay ventas registradas.")

    else:

        for fila in VENTAS:

            print(
                f"ID Venta: {fila[0]} "
                f"ID Producto: {fila[1]} "
                f"Categoria: {fila[2]} "
                f"Cantidad: {fila[3]} "
                f"Importe: {fila[4]}"
            )


def menu_estadisticas_ventas():

    print("\n========== ESTADISTICAS DE VENTAS ==========")

    ask = obtener_entero(
        "0. Retroceder\n"
        "1. Promedio general de ventas\n"
        "2. Promedio de ventas por categoria\n"
        "3. Cantidad total de ventas\n"
        "4. Cantidad de ventas por categoria\n"
        "5. Porcentaje de ventas por categoria\n"
        "6. Mayor y menor venta\n"
        "7. Resumen estadistico\n"
        "8. Total de productos vendidos...",
        0,
        8
    )

    match ask:

        case 0:
            ventas()

        case 1:

            promedio = promedio_ventas(VENTAS)

            print(
                "Promedio general de ventas:",
                promedio
            )

        case 2:

            categoria = obtener_entero(
                "Ingrese categoria:\n"
                "1. Alimentos\n"
                "2. Limpieza\n"
                "3. Bebidas...",
                1,
                3
            )

            promedio = promedio_ventas_categoria(
                VENTAS,
                categoria
            )

            print(
                "Promedio de ventas de la categoria:",
                promedio
            )

        case 3:

            cantidad = contar_ventas(VENTAS)

            print(
                "Cantidad total de ventas:",
                cantidad
            )

        case 4:

            categoria = obtener_entero(
                "Ingrese categoria:\n"
                "1. Alimentos\n"
                "2. Limpieza\n"
                "3. Bebidas...",
                1,
                3
            )

            cantidad = contar_ventas_categoria(
                VENTAS,
                categoria
            )

            print(
                "Cantidad de ventas de la categoria:",
                cantidad
            )

        case 5:

            categoria = obtener_entero(
                "Ingrese categoria:\n"
                "1. Alimentos\n"
                "2. Limpieza\n"
                "3. Bebidas...",
                1,
                3
            )

            porcentaje = porcentaje_ventas_categoria(
                VENTAS,
                categoria
            )

            print(
                "Porcentaje de ventas de la categoria:",
                porcentaje,
                "%"
            )

        case 6:

            mayor, menor = mayor_menor_venta(VENTAS)

            print("Mayor venta:", mayor)
            print("Menor venta:", menor)

        case 7:

            resumen_estadistico(VENTAS)

        case 8:

            total = total_productos_vendidos(VENTAS)

            print(
                "Total de productos vendidos:",
                total
            )