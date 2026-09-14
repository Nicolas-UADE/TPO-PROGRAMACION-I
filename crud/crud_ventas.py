import re
import listas

from listas import (
    PRODUCTOS,
    PRODUCTOS_NOMBRE,
    PRODUCTOS_CATEGORIA,
    PRODUCTOS_PRECIO,
    PRODUCTOS_STOCK,
    PRODUCTOS_DESCUENTO,
    productos_id_individual,
    ELIMINADO,
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

from Funciones.funciones import (
    obtener_caracter,
    obtener_entero,
    busqueda_secuencial,
    inicio_alta,
    inicio_modificar,
    inicio_baja,
    inicio_listado,
    inicio,
)

from Funciones.estadisticas_ventas import (
    resumen_estadistico,
    redondear_precio,
)


def ventas():
    texto = "VENTAS"
    inicio(texto)

    if listas.ADMIN == True:
        ask = obtener_entero(
            "0. Retroceder\n1. Listado de ventas\n2. Baja de venta\n3. Alta de venta\n4. Modificar venta\n5. Estadisticas\n.",
            0, 5,)

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
            "0. Retroceder\n1. Listado de ventas\n2. Estadisticas\n.", 0, 2,)

        match ask:
            case 0:
                return
            case 1:
                listar_ventas()
            case 2:
                resumen_estadistico()


def generar_id_venta():
    mayor = 100000

    for venta in VENTAS:
        if venta[VENTAS_ID] != ELIMINADO:
            if venta[VENTAS_ID] > mayor:
                mayor = venta[VENTAS_ID]

    return mayor + 1


def buscar_venta(id_venta):
    posiciones = []

    for i in VENTAS:
        if VENTAS[i][VENTAS_ID] == id_venta:
            posiciones.append(i)

    return posiciones


def pedir_fecha():
    patron = r"^[0-9]{2}/[0-9]{2}/[0-9]{4}$"

    fecha = obtener_caracter("Ingrese fecha DD/MM/AAAA\n.")

    while re.match(patron, fecha) == None:
        print("Fecha invalida.")
        fecha = obtener_caracter("Ingrese fecha DD/MM/AAAA\n.")

    return fecha


def alta_venta():
    texto = "ALTA DE VENTAS"
    inicio_alta(texto)

    id_cliente = obtener_entero("Ingrese ID del cliente. -1 Para salir\n.", -1, 1000000,)

    if id_cliente == -1:
        return

    id_venta = generar_id_venta()
    fecha = pedir_fecha()

    venta_temporal = []
    seguir = "Y"

    while seguir == "Y":

        codigo = obtener_entero("Ingrese codigo del producto. -1 Para cancelar\n.", -1, 1000000,)

        if codigo == -1:
            return

        pos = busqueda_secuencial(productos_id_individual, codigo,)

        if pos == -1:
            print("Producto inexistente.")

        elif PRODUCTOS[pos][PRODUCTOS_STOCK] == 0:
            print("Producto sin stock.")

        else:
            cantidad = obtener_entero("Ingrese cantidad\n.", 1,PRODUCTOS[pos][PRODUCTOS_STOCK],)

            precio = PRODUCTOS[pos][PRODUCTOS_PRECIO]
            descuento = PRODUCTOS[pos][PRODUCTOS_DESCUENTO]

            precio_final = precio - precio * descuento / 100
            precio_final = redondear_precio(precio_final)

            importe = precio_final * cantidad
            importe = redondear_precio(importe)

            venta_temporal.append([
                id_venta,
                id_cliente,
                codigo,
                PRODUCTOS[pos][PRODUCTOS_CATEGORIA],
                fecha,
                cantidad,
                precio_final,
                importe,
            ])

            print(
                f"\nProducto: {PRODUCTOS[pos][PRODUCTOS_NOMBRE]}"
                f"\nCantidad: {cantidad}"
                f"\nImporte: ${importe}\n"
            )

        seguir = obtener_caracter("Desea agregar otro producto? Y/N\n.").upper()

    if len(venta_temporal) == 0:
        print("No se agregaron productos.")
        return

    total = 0

    for venta in venta_temporal:
        total = total + venta[VENTAS_IMPORTE]

    print(f"\nTotal de la venta: ${redondear_precio(total)}")

    pregunta_seguridad = obtener_caracter("Esta seguro de agregar esta venta? Y/N\n.").upper()

    if pregunta_seguridad == "Y":

        for venta in venta_temporal:

            VENTAS.append(venta)

            pos = busqueda_secuencial(productos_id_individual,venta[VENTAS_PRODUCTO],)

            PRODUCTOS[pos][PRODUCTOS_STOCK] = (PRODUCTOS[pos][PRODUCTOS_STOCK] - venta[VENTAS_CANTIDAD])

        print("\n\033[32mVenta agregada correctamente.\033[0m")

    else:
        print("\n\033[31mAlta de venta cancelada.\033[0m")

    texto = ""
    inicio_alta(texto)


def baja_venta():
    texto = "BAJA DE VENTAS"
    inicio_baja(texto)

    id_venta = obtener_entero("Ingrese ID de venta a eliminar. -1 Para salir\n.",-1, 1000000,)

    if id_venta == -1:
        return

    posiciones = buscar_venta(id_venta)

    if len(posiciones) == 0:
        print("Venta inexistente.")
        return

    pregunta_seguridad = obtener_caracter(f"Esta seguro de eliminar la venta {id_venta}? Y/N\n.").upper()

    if pregunta_seguridad == "Y":

        for pos_venta in posiciones:

            codigo = VENTAS[pos_venta][VENTAS_PRODUCTO]
            cantidad = VENTAS[pos_venta][VENTAS_CANTIDAD]

            pos_producto = busqueda_secuencial(productos_id_individual, codigo,)

            if pos_producto != -1:
                PRODUCTOS[pos_producto][PRODUCTOS_STOCK] = (PRODUCTOS[pos_producto][PRODUCTOS_STOCK] + cantidad)

            VENTAS[pos_venta][VENTAS_ID] = ELIMINADO

        print("\n\033[32mVenta eliminada correctamente.\033[0m")

    else:
        print("\n\033[31mBaja de venta cancelada.\033[0m")

    texto = ""
    inicio_baja(texto)


def modificar_venta():
    texto = "MODIFICACION DE VENTAS"
    inicio_modificar(texto)

    id_venta = obtener_entero(
        "Ingrese ID de venta. -1 Para salir\n.",
        -1,
        1000000,
    )

    if id_venta == -1:
        return

    posiciones = buscar_venta(id_venta)

    if len(posiciones) == 0:
        print("Venta inexistente.")
        return

    opcion = obtener_entero(
        "1. Modificar cliente\n2. Modificar fecha\n3. Modificar cantidad\n.",
        1,
        3,
    )

    if opcion == 1:

        nuevo_cliente = obtener_entero(
            "Ingrese nuevo ID del cliente\n.",
            1,
            1000000,
        )

        for pos in posiciones:
            VENTAS[pos][VENTAS_CLIENTE] = nuevo_cliente

        print("\n\033[32mCliente modificado correctamente.\033[0m")

    if opcion == 2:

        nueva_fecha = pedir_fecha()

        for pos in posiciones:
            VENTAS[pos][VENTAS_FECHA] = nueva_fecha

        print("\n\033[32mFecha modificada correctamente.\033[0m")

    if opcion == 3:

        for pos in posiciones:
            print(
                f"Codigo: {VENTAS[pos][VENTAS_PRODUCTO]} "
                f"Cantidad: {VENTAS[pos][VENTAS_CANTIDAD]}"
            )

        codigo = obtener_entero( "Ingrese codigo del producto\n.", 1, 1000000,)

        pos_venta = -1

        for pos in posiciones:
            if VENTAS[pos][VENTAS_PRODUCTO] == codigo:
                pos_venta = pos

        if pos_venta == -1:
            print("Producto inexistente en esta venta.")
            return

        pos_producto = busqueda_secuencial(productos_id_individual, codigo,)

        cantidad_anterior = VENTAS[pos_venta][VENTAS_CANTIDAD]

        maximo = (PRODUCTOS[pos_producto][PRODUCTOS_STOCK] + cantidad_anterior)

        nueva_cantidad = obtener_entero("Ingrese nueva cantidad\n.", 1, maximo,)

        diferencia = nueva_cantidad - cantidad_anterior

        PRODUCTOS[pos_producto][PRODUCTOS_STOCK] = (PRODUCTOS[pos_producto][PRODUCTOS_STOCK] - diferencia)

        VENTAS[pos_venta][VENTAS_CANTIDAD] = nueva_cantidad

        VENTAS[pos_venta][VENTAS_IMPORTE] = (nueva_cantidad * VENTAS[pos_venta][VENTAS_PRECIO_UNITARIO])

        print("\n\033[32mCantidad modificada correctamente.\033[0m")

    texto = ""
    inicio_modificar(texto)


def listar_ventas():
    texto = "LISTA DE VENTAS"
    inicio_listado(texto)

    opcion = obtener_entero("1. Todas las ventas\n2. Buscar por ID\n3. Buscar por cliente\n-1. Salir\n.", -1, 3,)

    if opcion == -1:
        return

    if opcion == 1:

        for venta in VENTAS:

            if venta[VENTAS_ID] != ELIMINADO:

                pos = busqueda_secuencial( productos_id_individual, venta[VENTAS_PRODUCTO],)

                print(
                    f"\nID Venta: {venta[VENTAS_ID]}"
                    f"\nCliente: {venta[VENTAS_CLIENTE]}"
                    f"\nProducto: {PRODUCTOS[pos][PRODUCTOS_NOMBRE]}"
                    f"\nFecha: {venta[VENTAS_FECHA]}"
                    f"\nCantidad: {venta[VENTAS_CANTIDAD]}"
                    f"\nImporte: ${venta[VENTAS_IMPORTE]}\n"
                )

    if opcion == 2:

        id_venta = obtener_entero("Ingrese ID de venta\n.", 1, 1000000,)

        posiciones = buscar_venta(id_venta)

        if len(posiciones) == 0:
            print("Venta no encontrada.")

        else:
            for pos_venta in posiciones:

                venta = VENTAS[pos_venta]

                pos_producto = busqueda_secuencial( productos_id_individual, venta[VENTAS_PRODUCTO],)

                print(
                    f"\nID Venta: {venta[VENTAS_ID]}"
                    f"\nCliente: {venta[VENTAS_CLIENTE]}"
                    f"\nProducto: {PRODUCTOS[pos_producto][PRODUCTOS_NOMBRE]}"
                    f"\nFecha: {venta[VENTAS_FECHA]}"
                    f"\nCantidad: {venta[VENTAS_CANTIDAD]}"
                    f"\nImporte: ${venta[VENTAS_IMPORTE]}\n"
                )

    if opcion == 3:

        id_cliente = obtener_entero( "Ingrese ID del cliente\n.", 1, 1000000,)

        encontrado = False

        for venta in VENTAS:

            if (venta[VENTAS_ID] != ELIMINADO and venta[VENTAS_CLIENTE] == id_cliente ):

                encontrado = True

                pos = busqueda_secuencial( productos_id_individual, venta[VENTAS_PRODUCTO],)

                print(
                    f"\nID Venta: {venta[VENTAS_ID]}"
                    f"\nProducto: {PRODUCTOS[pos][PRODUCTOS_NOMBRE]}"
                    f"\nFecha: {venta[VENTAS_FECHA]}"
                    f"\nCantidad: {venta[VENTAS_CANTIDAD]}"
                    f"\nImporte: ${venta[VENTAS_IMPORTE]}\n"
                )

        if encontrado == False:
            print("No hay ventas para ese cliente.")

    texto = ""
    inicio_listado(texto)