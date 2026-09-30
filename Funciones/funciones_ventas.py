import re
from functools import reduce
from modulos.listas import (
    PRODUCTOS,
    PRODUCTOS_NOMBRE,
    PRODUCTOS_CATEGORIA,
    PRODUCTOS_PRECIO,
    PRODUCTOS_STOCK,
    PRODUCTOS_DESCUENTO,
    ELIMINADO,
    VENTAS,
    VENTAS_ID,
    VENTAS_CLIENTE,
    VENTAS_PRODUCTO,
    VENTAS_FECHA,
    VENTAS_CANTIDAD,
    VENTAS_PRECIO_UNITARIO,
    VENTAS_IMPORTE,
    VENTAS_CATEGORIA,
    lista_clientes,
    productos_id_individual,
)

from Funciones.funciones_uni import (
    obtener_entero,
    obtener_respuesta,
    inicio_alta,
    inicio_modificar,
    inicio_baja,
    inicio_listado,
    inicio,
    recortar_texto,
    generador_de_id,
    buscar_por_id,
)


def menu_estadisticas_ventas():
    """Submenu para ver distintos tipos de estadisticas sobre las ventas."""
    texto = "ESTADISTICAS"
    inicio(texto)
    opcion = obtener_entero(
        "[0] Retroceder\n[1] Resumen completo\n"
        "[2] Estadisticas por categoria\n[3] Total de una venta\n.",
        0,
        3,
    )

    match opcion:
        case 0:
            return
        case 1:
            # Muestra un resumen general de todas las ventas.
            resumen_estadistico()
        case 2:
            # Muestra estadisticas filtradas por una categoria elegida.
            categorias = obtener_categorias()

            if len(categorias) == 0:
                print("\n\033[31mNo hay ventas registradas.\033[0m")
                return

            print("\nCATEGORIAS")

            for posicion in range(len(categorias)):
                print(f"{posicion + 1}. {categorias[posicion]}")

            opcion_categoria = obtener_entero(
                "Seleccione una categoria\n.", 1, len(categorias)
            )
            categoria = categorias[opcion_categoria - 1]
            mostrar_estadisticas_categoria(categoria)
        case 3:
            # Muestra el total de una venta puntual buscandola por su id.
            id_venta = obtener_entero(
                "Ingrese ID de venta.\n-1 para salir\n.", -1, 999999
            )

            if id_venta == -1:
                return

            posiciones = buscar_venta(VENTAS, id_venta)

            if len(posiciones) == 0:
                print("\n\033[31mVenta inexistente.\033[0m")
            else:
                total = total_venta(id_venta)
                print(f"\nTotal de la venta {id_venta}: ${total:,.2f}")


def alta_venta():
    """Carga una venta nueva. Permite agregar varios productos antes de confirmar."""
    texto = "ALTA DE VENTAS"
    inicio_alta(texto)

    id_cliente = pedir_cliente("Ingrese ID del cliente.\n-1 para salir\n.")

    if id_cliente == -1:
        return

    print(f"Cliente seleccionado: {obtener_nombre_cliente(id_cliente)}")

    id_venta = generar_id_venta(VENTAS)
    fecha = pedir_fecha()
    venta_temporal = []
    seguir = "Y"

    # Loop para ir agregando productos a la venta hasta que el usuario diga que no quiere mas.
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
            # Se suma la cantidad ya reservada de ese producto en esta misma venta
            # para no vender mas stock del que hay disponible.
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
                cantidad = obtener_entero("Ingrese cantidad\n.", 1, stock_disponible)
                # Calcula el precio final aplicando el descuento del producto.
                precio_original = PRODUCTOS[posicion_producto][PRODUCTOS_PRECIO]
                descuento_producto = PRODUCTOS[posicion_producto][PRODUCTOS_DESCUENTO]
                descuento_importe = precio_original * descuento_producto / 100
                precio_final = precio_original - descuento_importe
                precio_final = redondear_precio(precio_final)
                importe = redondear_precio(precio_final * cantidad)
                categoria_producto = PRODUCTOS[posicion_producto][PRODUCTOS_CATEGORIA]

                # Se guarda el producto en una lista temporal hasta confirmar toda la venta.
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

                print(f"""
                        Producto: {PRODUCTOS[posicion_producto][PRODUCTOS_NOMBRE]}
                        Categoria del producto: {categoria_producto}
                        Precio original del producto: ${precio_original:.2f}
                        Descuento del producto: {descuento_producto}%
                        Importe descontado por unidad: ${descuento_importe:.2f}
                        Precio final por unidad: ${precio_final:.2f}
                        Cantidad: {cantidad}
                        Importe del producto: ${importe:.2f}
                        """)

        seguir = obtener_respuesta("Desea agregar otro producto? Y/N\n.")

    if len(venta_temporal) == 0:
        print("No se agregaron productos.")
        return

    # Suma el importe de todos los productos cargados para mostrar el total final.
    total = 0

    for venta in venta_temporal:
        total += venta[VENTAS_IMPORTE]

    print(f"\nID de la nueva venta: {id_venta}")
    print(f"Total final de la venta: ${redondear_precio(total):.2f}")
    mostrar_listado_ventas(venta_temporal)

    confirmacion = obtener_respuesta("Esta seguro de agregar esta venta? Y/N\n.")

    if confirmacion == "Y":
        # Recien aca se guarda de verdad en VENTAS y se descuenta el stock.
        for venta in venta_temporal:
            VENTAS.append(venta)
            posicion_producto = buscar_posicion_producto(venta[VENTAS_PRODUCTO])
            PRODUCTOS[posicion_producto][PRODUCTOS_STOCK] -= venta[VENTAS_CANTIDAD]

        print("\n\033[32mVenta agregada correctamente.\033[0m")
    else:
        print("\n\033[31mAlta de venta cancelada.\033[0m")

    inicio_alta("")


def baja_venta():
    """Elimina una venta (o todos los productos de esa venta si tiene varios items)."""
    texto = "BAJA DE VENTAS"
    inicio_baja(texto)

    id_venta = obtener_entero(
        "Ingrese ID de venta a eliminar.\n-1 para salir\n.", -1, 999999
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
        # Al eliminar la venta, se le devuelve el stock a cada producto involucrado.
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
    """Permite modificar el cliente, la fecha o la cantidad de un producto de una venta."""
    texto = "MODIFICACION DE VENTAS"
    inicio_modificar(texto)

    id_venta = obtener_entero("Ingrese ID de venta.\n-1 para salir\n.", -1, 999999)

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
        "[1] Modificar cliente\n[2] Modificar fecha\n[3] Modificar cantidad\n.",
        1,
        3,
    )

    match opcion:
        case 1:
            # Cambia el cliente en todos los items de esa venta.
            nuevo_cliente = pedir_cliente(
                "Ingrese nuevo ID del cliente.\n-1 para salir\n."
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
            # Cambia la fecha en todos los items de esa venta.
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
            # Cambia la cantidad de un producto puntual dentro de la venta y ajusta el stock.
            codigo = obtener_entero(
                "Ingrese codigo del producto.\n-1 para salir\n.", -1, 999999
            )

            if codigo == -1:
                return

            # Busca cual de los items de la venta corresponde a ese codigo de producto.
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
            # El maximo permitido es el stock actual mas lo que ya estaba reservado en esta venta.
            cantidad_maxima = (
                PRODUCTOS[posicion_producto][PRODUCTOS_STOCK] + cantidad_anterior
            )
            nueva_cantidad = obtener_entero(
                "Ingrese nueva cantidad\n.", 1, cantidad_maxima
            )
            confirmacion = obtener_respuesta(
                f"Cambiar la cantidad de {cantidad_anterior} a {nueva_cantidad}? Y/N\n."
            )

            if confirmacion == "Y":
                # Ajusta el stock segun la diferencia entre la cantidad vieja y la nueva.
                diferencia = nueva_cantidad - cantidad_anterior
                PRODUCTOS[posicion_producto][PRODUCTOS_STOCK] -= diferencia
                VENTAS[posicion_venta][VENTAS_CANTIDAD] = nueva_cantidad
                VENTAS[posicion_venta][VENTAS_IMPORTE] = redondear_precio(
                    nueva_cantidad * VENTAS[posicion_venta][VENTAS_PRECIO_UNITARIO]
                )
                print("\n\033[32mCantidad modificada correctamente.\033[0m")
            else:
                print("\n\033[31mModificacion cancelada.\033[0m")

    inicio_modificar("")


def listar_ventas():
    """Muestra el listado de ventas, con distintas formas de filtrarlas."""
    texto = "LISTA DE VENTAS"
    inicio_listado(texto)

    opcion = obtener_entero(
        "[1] Todas las ventas\n[2] Buscar por ID\n[3] Consultar cliente y sus ventas\n-1. Salir\n.",
        -1,
        3,
    )

    if opcion == -1:
        return

    ventas_encontradas = []

    match opcion:
        case 1:
            # Junta todas las ventas que no fueron eliminadas.
            for venta in VENTAS:
                if venta[VENTAS_ID] != ELIMINADO:
                    ventas_encontradas.append(venta)

        case 2:
            # Busca los items que pertenecen a un id de venta puntual.
            id_venta = obtener_entero("Ingrese ID de venta\n.", 1, 999999)
            posiciones = buscar_venta(VENTAS, id_venta)

            for posicion in posiciones:
                ventas_encontradas.append(VENTAS[posicion])

        case 3:
            # Muestra los datos del cliente junto con todas sus ventas.
            consultar_cliente_y_ventas()
            return

    if len(ventas_encontradas) == 0:
        print("\n\033[31mNo se encontraron ventas.\033[0m")
    else:
        mostrar_listado_ventas(ventas_encontradas)

    inicio_listado("")


def buscar_venta(matriz_ventas, id_venta):
    """Devuelve todas las posiciones donde aparece ese id de venta."""
    posiciones = []

    for posicion in range(len(matriz_ventas)):
        if matriz_ventas[posicion][VENTAS_ID] == id_venta:
            posiciones.append(posicion)

    return posiciones


def pedir_fecha():
    """Pide una fecha por teclado y no avanza hasta que tenga el formato DD/MM/AAAA y sea coherente."""
    patron_fecha = r"^[0-9]{2}/[0-9]{2}/[0-9]{4}$"
    fecha_valida = False

    while fecha_valida == False:
        fecha = input("Ingrese fecha DD/MM/AAAA\n.").strip()

        if re.match(patron_fecha, fecha) != None:
            partes_fecha = fecha.split("/")
            dia = int(partes_fecha[0])
            mes = int(partes_fecha[1])
            anio = int(partes_fecha[2])

            # Chequea que el dia, mes y anio tengan valores logicos.
            if dia >= 1 and dia <= 31 and mes >= 1 and mes <= 12 and anio >= 2000:
                fecha_valida = True

        if fecha_valida == False:
            print("\nFecha invalida. Use el formato DD/MM/AAAA.\n")

    return fecha


def generar_id_venta(matriz_ventas):
    """Junta los ids de ventas que no fueron eliminadas y genera uno nuevo que no se repita."""
    ids_ventas = []

    for venta in matriz_ventas:
        if venta[VENTAS_ID] != ELIMINADO:
            ids_ventas.append(venta[VENTAS_ID])

    return generador_de_id(ids_ventas)


def mostrar_listado_ventas(ventas_a_mostrar):
    """Imprime una tabla con los datos de las ventas que se le pasen."""
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
        cliente = recortar_texto(obtener_nombre_cliente(venta[VENTAS_CLIENTE]), 16)
        producto = recortar_texto(obtener_nombre_producto(venta[VENTAS_PRODUCTO]), 10)
        categoria = recortar_texto(venta[VENTAS_CATEGORIA], 9)

        # Si el producto ya no existe, se muestra "-" en vez del precio y descuento original.
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


redondear_precio = lambda numero: round(numero, 2)


def obtener_ventas_activas():
    """Devuelve las ventas que no fueron eliminadas."""
    ventas_activas = list(
        filter(
            lambda venta: venta[VENTAS_ID] != ELIMINADO,
            VENTAS,
        )
    )

    return ventas_activas


def obtener_importes_ventas():
    """Devuelve los importes de todas las ventas activas."""
    importes_ventas = list(
        map(
            lambda venta: venta[VENTAS_IMPORTE],
            obtener_ventas_activas(),
        )
    )

    return importes_ventas


def sumar_importes_ventas():
    """Suma los importes de las ventas activas usando reduce."""
    importes_ventas = obtener_importes_ventas()

    if len(importes_ventas) == 0:
        return 0

    suma_total = reduce(
        lambda acumulado, importe: acumulado + importe,
        importes_ventas,
    )

    return suma_total


def obtener_ids_ventas():
    """Devuelve los ID de las ventas activas sin repetirlos."""
    ids_ventas = []

    for fila in obtener_ventas_activas():

        if fila[VENTAS_ID] not in ids_ventas:

            ids_ventas.append(fila[VENTAS_ID])

    return ids_ventas


def obtener_categorias():
    """Devuelve las categorias que aparecen en las ventas activas."""
    categorias = []

    for venta in obtener_ventas_activas():

        categoria = venta[VENTAS_CATEGORIA]

        if categoria not in categorias:

            categorias.append(categoria)

    categorias.sort()

    return categorias


def total_venta(id_venta):
    """Devuelve el importe total de una venta activa."""
    total = 0

    for fila in obtener_ventas_activas():

        if fila[VENTAS_ID] == id_venta:

            total = total + fila[VENTAS_IMPORTE]

    return total


def contar_ventas():
    """Devuelve la cantidad de ventas activas sin repetir sus ID."""
    ids_ventas = obtener_ids_ventas()

    return len(ids_ventas)


def contar_ventas_categoria(categoria):
    """Cuenta los registros de productos vendidos en una categoria."""
    cantidad = 0

    categoria = categoria.upper()

    for fila in obtener_ventas_activas():

        if fila[VENTAS_CATEGORIA] == categoria:

            cantidad = cantidad + 1

    return cantidad


def promedio_ventas():
    """Devuelve el importe promedio por venta."""
    ids_ventas = obtener_ids_ventas()

    suma_total = sumar_importes_ventas()

    if len(ids_ventas) > 0:

        promedio = suma_total / len(ids_ventas)

    else:

        promedio = 0

    return promedio


def promedio_ventas_categoria(categoria):
    """Devuelve el importe promedio por registro de una categoria."""
    categoria = categoria.upper()

    total_categoria = 0

    for fila in obtener_ventas_activas():

        if fila[VENTAS_CATEGORIA] == categoria:

            total_categoria = total_categoria + fila[VENTAS_IMPORTE]

    cantidad = contar_ventas_categoria(categoria)

    if cantidad > 0:

        promedio = total_categoria / cantidad

    else:

        promedio = 0

    return promedio


def porcentaje_ventas_categoria(categoria):
    """Devuelve el porcentaje de registros de una categoria."""
    total = len(obtener_ventas_activas())

    cantidad_categoria = contar_ventas_categoria(categoria)

    if total > 0:

        porcentaje = cantidad_categoria * 100 / total

    else:

        porcentaje = 0

    return porcentaje


def total_productos_vendidos():
    """Devuelve la cantidad total de unidades vendidas."""
    cantidad_total = 0

    for fila in obtener_ventas_activas():

        cantidad_total = cantidad_total + fila[VENTAS_CANTIDAD]

    return cantidad_total


def mayor_menor_venta():
    """Devuelve los ID e importes de la mayor y la menor venta."""
    ids_ventas = obtener_ids_ventas()

    if len(ids_ventas) == 0:

        return 0, 0, 0, 0

    primer_id = ids_ventas[0]

    mayor = total_venta(primer_id)
    menor = total_venta(primer_id)

    id_mayor = primer_id
    id_menor = primer_id

    for id_venta in ids_ventas:

        total = total_venta(id_venta)

        if total > mayor:

            mayor = total
            id_mayor = id_venta

        if total < menor:

            menor = total
            id_menor = id_venta

    return (id_mayor, mayor, id_menor, menor)


def mostrar_estadisticas_categoria(categoria):
    """Muestra el resumen estadistico de una categoria."""
    cantidad = contar_ventas_categoria(categoria)
    promedio = promedio_ventas_categoria(categoria)
    porcentaje = porcentaje_ventas_categoria(categoria)

    print(
        f"\nCategoria: {categoria}"
        f"\nRegistros de productos vendidos: {cantidad}"
        f"\nPromedio por registro: ${redondear_precio(promedio):,.2f}"
        f"\nPorcentaje de registros: {redondear_precio(porcentaje):.2f}%"
    )


def resumen_estadistico():
    """Muestra un resumen general y por categoria de las ventas."""
    cantidad_ventas = contar_ventas()

    importe_total = redondear_precio(sumar_importes_ventas())

    promedio_general = redondear_precio(promedio_ventas())

    productos_vendidos = total_productos_vendidos()

    categorias = obtener_categorias()

    print(
        "\n=============================="
        "\n   ESTADISTICAS DE VENTAS"
        "\n=============================="
        f"\nCantidad total de ventas: {cantidad_ventas}"
        f"\nImporte total vendido: ${importe_total:,.2f}"
        f"\nPromedio por venta: ${promedio_general:,.2f}"
        f"\nTotal de productos vendidos: {productos_vendidos}"
        "\n"
    )

    print("ESTADISTICAS POR CATEGORIA")
    print("------------------------------")

    for categoria in categorias:
        mostrar_estadisticas_categoria(categoria)
        print("------------------------------")

    if cantidad_ventas > 0:

        (
            id_mayor,
            mayor,
            id_menor,
            menor,
        ) = mayor_menor_venta()

        print(
            f"Mayor venta: {id_mayor}"
            f"\nImporte: ${redondear_precio(mayor):,.2f}"
            "\n"
            f"\nMenor venta: {id_menor}"
            f"\nImporte: ${redondear_precio(menor):,.2f}"
            "\n=============================="
        )

    else:

        print("\nNo hay ventas registradas." "\n==============================")


def consultar_cliente_y_ventas():
    """Muestra los datos de un cliente y todas las ventas que realizo."""
    id_cliente = pedir_cliente("Ingrese ID del cliente.\n-1 para salir\n.")

    if id_cliente == -1:
        return

    posicion_cliente = buscar_por_id(
        lista_clientes,
        id_cliente,
    )
    cliente = lista_clientes[posicion_cliente]

    # Muestra los datos personales del cliente.
    print("\nDATOS DEL CLIENTE")
    print("-" * 30)
    print(f"ID: {cliente['id']}")
    print(f"Nombre: {cliente['nombre']}")
    print(f"DNI: {cliente['dni']}")
    print(f"Telefono: {cliente['telefono']}")
    print(f"Email: {cliente['email']}")

    # Junta todas las ventas activas de ese cliente y suma el total gastado.
    ventas_cliente = []
    total_comprado = 0

    for venta in VENTAS:
        if venta[VENTAS_ID] != ELIMINADO and venta[VENTAS_CLIENTE] == id_cliente:
            ventas_cliente.append(venta)
            total_comprado += venta[VENTAS_IMPORTE]

    if len(ventas_cliente) == 0:
        print("\n\033[31m" "El cliente no tiene ventas registradas." "\033[0m")
    else:
        print("\nVENTAS DEL CLIENTE")
        mostrar_listado_ventas(ventas_cliente)
        print(
            f"\nTotal comprado por el cliente: "
            f"${redondear_precio(total_comprado):.2f}"
        )


def buscar_posicion_producto(codigo):
    """Devuelve la posicion de un producto segun su codigo, o -1 si no existe."""
    if codigo in productos_id_individual:
        return productos_id_individual.index(codigo)

    return -1


def pedir_cliente(mensaje):
    """Pide un id de cliente y no avanza hasta que exista o se cancele con -1."""
    id_cliente = obtener_entero(mensaje, -1, 1000000)

    while id_cliente != -1 and buscar_por_id(lista_clientes, id_cliente) == -2:
        print("\n\033[31mCliente inexistente.\033[0m\n")
        id_cliente = obtener_entero(mensaje, -1, 1000000)

    return id_cliente


def obtener_nombre_cliente(id_cliente):
    """Devuelve el nombre del cliente junto a su id, o un aviso si ya fue eliminado."""
    posicion = buscar_por_id(lista_clientes, id_cliente)

    if posicion == -2:
        return f"CLIENTE ELIMINADO ({id_cliente})"

    return f"{lista_clientes[posicion]['nombre']} ({id_cliente})"


def obtener_nombre_producto(codigo):
    """Devuelve el nombre del producto, o "ELIMINADO" si ya no existe."""
    posicion = buscar_posicion_producto(codigo)

    if posicion == -1:
        return "ELIMINADO"

    return PRODUCTOS[posicion][PRODUCTOS_NOMBRE]
