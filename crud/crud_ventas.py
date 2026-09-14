import listas

from listas import (
    PRODUCTOS,
    PRODUCTOS_NOMBRE,
    PRODUCTOS_CATEGORIA,
    PRODUCTOS_PRECIO,
    PRODUCTOS_STOCK,
    PRODUCTOS_DESCUENTO,
    productos_id_individual,
    lista_clientes,
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
    obtener_entero,
    obtener_respuesta,
    inicio_alta,
    inicio_modificar,
    inicio_baja,
    inicio_listado,
    inicio,
    generar_id_venta,
    buscar_venta,
    pedir_fecha,
    buscar_por_id,
    recortar_texto,
)

from Funciones.estadisticas_ventas import resumen_estadistico, redondear_precio


def ventas():
    texto = "VENTAS"
    inicio(texto)

    if listas.ADMIN == True:
        opcion = obtener_entero(
            "0. Retroceder\n1. Listado de ventas\n2. Baja de venta\n"
            "3. Alta de venta\n4. Modificar venta\n5. Estadisticas\n.",
            0,
            5,
        )

        match opcion:
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
        opcion = obtener_entero(
            "0. Retroceder\n1. Listado de ventas\n2. Estadisticas\n.", 0, 2
        )

        match opcion:
            case 0:
                return
            case 1:
                listar_ventas()
            case 2:
                resumen_estadistico()


def buscar_posicion_producto(codigo):
    if codigo in productos_id_individual:
        return productos_id_individual.index(codigo)

    return -1


def obtener_nombre_cliente(id_cliente):
    posicion = buscar_por_id(lista_clientes, id_cliente)

    if posicion == -2:
        return f"CLIENTE ELIMINADO ({id_cliente})"

    return f"{lista_clientes[posicion]['nombre']} ({id_cliente})"


def obtener_nombre_producto(codigo):
    posicion = buscar_posicion_producto(codigo)

    if posicion == -1:
        return "ELIMINADO"

    return PRODUCTOS[posicion][PRODUCTOS_NOMBRE]


def mostrar_listado_ventas(ventas_a_mostrar):
    ancho = 120
    print("-" * ancho)
    print(
        f"| {'ID':<6} | {'CLIENTE (ID)':<16} | {'PRODUCTO':<10} | "
        f"{'CATEGORIA':<9} | {'FECHA':<10} | {'CANT':<4} | "
        f"{'PRECIO':<9} | {'DESC.':<6} | {'P.FINAL':<9} | {'IMPORTE':<10} |"
    )
    print("-" * ancho)

    for venta in ventas_a_mostrar:
        posicion_producto = buscar_posicion_producto(venta[VENTAS_PRODUCTO])
        cliente = recortar_texto(
            obtener_nombre_cliente(venta[VENTAS_CLIENTE]), 16
        )
        producto = recortar_texto(
            obtener_nombre_producto(venta[VENTAS_PRODUCTO]), 10
        )
        categoria = recortar_texto(venta[VENTAS_CATEGORIA], 9)

        if posicion_producto == -1:
            precio_original = "-"
            descuento = "-"
        else:
            precio_original = f"${PRODUCTOS[posicion_producto][PRODUCTOS_PRECIO]:.2f}"
            descuento = f"{PRODUCTOS[posicion_producto][PRODUCTOS_DESCUENTO]}%"

        precio_final = f"${venta[VENTAS_PRECIO_UNITARIO]:.2f}"
        importe = f"${venta[VENTAS_IMPORTE]:.2f}"

        print(
            f"| {venta[VENTAS_ID]:<6} | {cliente:<16} | {producto:<10} | "
            f"{categoria:<9} | {venta[VENTAS_FECHA]:<10} | "
            f"{venta[VENTAS_CANTIDAD]:<4} | {precio_original:<9} | "
            f"{descuento:<6} | {precio_final:<9} | {importe:<10} |"
        )

    print("-" * ancho)


def pedir_cliente(mensaje):
    id_cliente = obtener_entero(mensaje, -1, 1000000)

    while id_cliente != -1 and buscar_por_id(lista_clientes, id_cliente) == -2:
        print("\n\033[31mCliente inexistente.\033[0m\n")
        id_cliente = obtener_entero(mensaje, -1, 1000000)

    return id_cliente


def alta_venta():
    texto = "ALTA DE VENTAS"
    inicio_alta(texto)

    id_cliente = pedir_cliente("Ingrese ID del cliente. -1 Para salir\n.")

    if id_cliente == -1:
        return

    print(f"Cliente seleccionado: {obtener_nombre_cliente(id_cliente)}")

    id_venta = generar_id_venta(VENTAS)
    fecha = pedir_fecha()
    venta_temporal = []
    seguir = "Y"

    while seguir == "Y":
        codigo = obtener_entero(
            "Ingrese codigo del producto. -1 Para cancelar\n.", -1, 1000000
        )

        if codigo == -1:
            return

        posicion_producto = buscar_posicion_producto(codigo)

        if posicion_producto == -1:
            print("\n\033[31mProducto inexistente.\033[0m\n")
        else:
            cantidad_reservada = 0

            for venta in venta_temporal:
                if venta[VENTAS_PRODUCTO] == codigo:
                    cantidad_reservada += venta[VENTAS_CANTIDAD]

            stock_disponible = (
                PRODUCTOS[posicion_producto][PRODUCTOS_STOCK] - cantidad_reservada
            )

            if stock_disponible == 0:
                print("\n\033[31mProducto sin stock disponible.\033[0m\n")
            else:
                cantidad = obtener_entero(
                    "Ingrese cantidad\n.", 1, stock_disponible
                )
                precio_original = PRODUCTOS[posicion_producto][PRODUCTOS_PRECIO]
                descuento_producto = PRODUCTOS[posicion_producto][
                    PRODUCTOS_DESCUENTO
                ]
                descuento_importe = precio_original * descuento_producto / 100
                precio_final = precio_original - descuento_importe
                precio_final = redondear_precio(precio_final)
                importe = redondear_precio(precio_final * cantidad)
                categoria_producto = PRODUCTOS[posicion_producto][
                    PRODUCTOS_CATEGORIA
                ]

                venta_temporal.append(
                    [
                        id_venta,
                        id_cliente,
                        codigo,
                        categoria_producto,
                        fecha,
                        cantidad,
                        precio_final,
                        importe,
                    ]
                )

                print(
                    f"\nProducto: {PRODUCTOS[posicion_producto][PRODUCTOS_NOMBRE]}"
                    f"\nCategoria del producto: {categoria_producto}"
                    f"\nPrecio original del producto: ${precio_original:.2f}"
                    f"\nDescuento del producto: {descuento_producto}%"
                    f"\nImporte descontado por unidad: ${descuento_importe:.2f}"
                    f"\nPrecio final por unidad: ${precio_final:.2f}"
                    f"\nCantidad: {cantidad}"
                    f"\nImporte del producto: ${importe:.2f}\n"
                )

        seguir = obtener_respuesta("Desea agregar otro producto? Y/N\n.")

    if len(venta_temporal) == 0:
        print("No se agregaron productos.")
        return

    total = 0

    for venta in venta_temporal:
        total += venta[VENTAS_IMPORTE]

    print(f"\nID de la nueva venta: {id_venta}")
    print(f"Total final de la venta: ${redondear_precio(total):.2f}")
    mostrar_listado_ventas(venta_temporal)

    confirmacion = obtener_respuesta(
        "Esta seguro de agregar esta venta? Y/N\n."
    )

    if confirmacion == "Y":
        for venta in venta_temporal:
            VENTAS.append(venta)
            posicion_producto = buscar_posicion_producto(venta[VENTAS_PRODUCTO])
            PRODUCTOS[posicion_producto][PRODUCTOS_STOCK] -= venta[
                VENTAS_CANTIDAD
            ]

        print("\n\033[32mVenta agregada correctamente.\033[0m")
    else:
        print("\n\033[31mAlta de venta cancelada.\033[0m")

    inicio_alta("")


def baja_venta():
    texto = "BAJA DE VENTAS"
    inicio_baja(texto)

    id_venta = obtener_entero(
        "Ingrese ID de venta a eliminar. -1 Para salir\n.", -1, 999999
    )

    if id_venta == -1:
        return

    posiciones = buscar_venta(VENTAS, id_venta)

    if len(posiciones) == 0:
        print("\n\033[31mVenta inexistente.\033[0m")
        return

    ventas_encontradas = []

    for posicion in posiciones:
        ventas_encontradas.append(VENTAS[posicion])

    mostrar_listado_ventas(ventas_encontradas)
    confirmacion = obtener_respuesta(
        f"Esta seguro de eliminar la venta {id_venta}? Y/N\n."
    )

    if confirmacion == "Y":
        for posicion_venta in posiciones:
            codigo = VENTAS[posicion_venta][VENTAS_PRODUCTO]
            cantidad = VENTAS[posicion_venta][VENTAS_CANTIDAD]
            posicion_producto = buscar_posicion_producto(codigo)

            if posicion_producto != -1:
                PRODUCTOS[posicion_producto][PRODUCTOS_STOCK] += cantidad

            VENTAS[posicion_venta][VENTAS_ID] = ELIMINADO

        print("\n\033[32mVenta eliminada correctamente.\033[0m")
    else:
        print("\n\033[31mBaja de venta cancelada.\033[0m")

    inicio_baja("")


def modificar_venta():
    texto = "MODIFICACION DE VENTAS"
    inicio_modificar(texto)

    id_venta = obtener_entero("Ingrese ID de venta. -1 Para salir\n.", -1, 999999)

    if id_venta == -1:
        return

    posiciones = buscar_venta(VENTAS, id_venta)

    if len(posiciones) == 0:
        print("\n\033[31mVenta inexistente.\033[0m")
        return

    ventas_encontradas = []

    for posicion in posiciones:
        ventas_encontradas.append(VENTAS[posicion])

    mostrar_listado_ventas(ventas_encontradas)

    opcion = obtener_entero(
        "1. Modificar cliente\n2. Modificar fecha\n3. Modificar cantidad\n.",
        1,
        3,
    )

    match opcion:
        case 1:
            nuevo_cliente = pedir_cliente(
                "Ingrese nuevo ID del cliente. -1 Para salir\n."
            )

            if nuevo_cliente == -1:
                return

            print(f"Nuevo cliente: {obtener_nombre_cliente(nuevo_cliente)}")
            confirmacion = obtener_respuesta(
                "Esta seguro de modificar el cliente de la venta? Y/N\n."
            )

            if confirmacion == "Y":
                for posicion in posiciones:
                    VENTAS[posicion][VENTAS_CLIENTE] = nuevo_cliente

                print("\n\033[32mCliente modificado correctamente.\033[0m")
            else:
                print("\n\033[31mModificacion cancelada.\033[0m")

        case 2:
            nueva_fecha = pedir_fecha()
            confirmacion = obtener_respuesta(
                f"Cambiar la fecha a {nueva_fecha}? Y/N\n."
            )

            if confirmacion == "Y":
                for posicion in posiciones:
                    VENTAS[posicion][VENTAS_FECHA] = nueva_fecha

                print("\n\033[32mFecha modificada correctamente.\033[0m")
            else:
                print("\n\033[31mModificacion cancelada.\033[0m")

        case 3:
            codigo = obtener_entero(
                "Ingrese codigo del producto. -1 Para salir\n.", -1, 999999
            )

            if codigo == -1:
                return

            posicion_venta = -1

            for posicion in posiciones:
                if VENTAS[posicion][VENTAS_PRODUCTO] == codigo:
                    posicion_venta = posicion

            if posicion_venta == -1:
                print("\n\033[31mProducto inexistente en esta venta.\033[0m")
                return

            posicion_producto = buscar_posicion_producto(codigo)

            if posicion_producto == -1:
                print("\n\033[31mEl producto fue eliminado.\033[0m")
                return

            cantidad_anterior = VENTAS[posicion_venta][VENTAS_CANTIDAD]
            cantidad_maxima = (
                PRODUCTOS[posicion_producto][PRODUCTOS_STOCK]
                + cantidad_anterior
            )
            nueva_cantidad = obtener_entero(
                "Ingrese nueva cantidad\n.", 1, cantidad_maxima
            )
            confirmacion = obtener_respuesta(
                f"Cambiar la cantidad de {cantidad_anterior} a {nueva_cantidad}? Y/N\n."
            )

            if confirmacion == "Y":
                diferencia = nueva_cantidad - cantidad_anterior
                PRODUCTOS[posicion_producto][PRODUCTOS_STOCK] -= diferencia
                VENTAS[posicion_venta][VENTAS_CANTIDAD] = nueva_cantidad
                VENTAS[posicion_venta][VENTAS_IMPORTE] = redondear_precio(
                    nueva_cantidad
                    * VENTAS[posicion_venta][VENTAS_PRECIO_UNITARIO]
                )
                print("\n\033[32mCantidad modificada correctamente.\033[0m")
            else:
                print("\n\033[31mModificacion cancelada.\033[0m")

    inicio_modificar("")


def consultar_cliente_y_ventas():
    """Muestra los datos de un cliente y todas las ventas que realizo."""
    id_cliente = pedir_cliente(
        "Ingrese ID del cliente. -1 Para salir\n."
    )

    if id_cliente == -1:
        return

    posicion_cliente = buscar_por_id(
        lista_clientes,
        id_cliente,
    )
    cliente = lista_clientes[posicion_cliente]

    print("\nDATOS DEL CLIENTE")
    print("-" * 30)
    print(f"ID: {cliente['id']}")
    print(f"Nombre: {cliente['nombre']}")
    print(f"DNI: {cliente['dni']}")
    print(f"Telefono: {cliente['telefono']}")
    print(f"Email: {cliente['email']}")

    ventas_cliente = []
    total_comprado = 0

    for venta in VENTAS:
        if (
            venta[VENTAS_ID] != ELIMINADO
            and venta[VENTAS_CLIENTE] == id_cliente
        ):
            ventas_cliente.append(venta)
            total_comprado += venta[VENTAS_IMPORTE]

    if len(ventas_cliente) == 0:
        print(
            "\n\033[31m"
            "El cliente no tiene ventas registradas."
            "\033[0m"
        )
    else:
        print("\nVENTAS DEL CLIENTE")
        mostrar_listado_ventas(ventas_cliente)
        print(
            f"\nTotal comprado por el cliente: "
            f"${redondear_precio(total_comprado):.2f}"
        )


def listar_ventas():
    texto = "LISTA DE VENTAS"
    inicio_listado(texto)

    opcion = obtener_entero(
        "1. Todas las ventas\n2. Buscar por ID\n"
        "3. Consultar cliente y sus ventas\n-1. Salir\n.",
        -1,
        3,
    )

    if opcion == -1:
        return

    ventas_encontradas = []

    match opcion:
        case 1:
            for venta in VENTAS:
                if venta[VENTAS_ID] != ELIMINADO:
                    ventas_encontradas.append(venta)

        case 2:
            id_venta = obtener_entero("Ingrese ID de venta\n.", 1, 999999)
            posiciones = buscar_venta(VENTAS, id_venta)

            for posicion in posiciones:
                ventas_encontradas.append(VENTAS[posicion])

        case 3:
            consultar_cliente_y_ventas()
            return

    if len(ventas_encontradas) == 0:
        print("\n\033[31mNo se encontraron ventas.\033[0m")
    else:
        mostrar_listado_ventas(ventas_encontradas)

    inicio_listado("")
