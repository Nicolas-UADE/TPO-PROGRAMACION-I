from functools import reduce

from listas import (
    VENTAS,
    VENTAS_ID,
    VENTAS_CATEGORIA,
    VENTAS_CANTIDAD,
    VENTAS_IMPORTE,
    ELIMINADO,
)




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

            total = (total + fila[VENTAS_IMPORTE])

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

        promedio = ( suma_total / len(ids_ventas)
        )

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

    cantidad_categoria = (contar_ventas_categoria(categoria))

    if total > 0:

        porcentaje = (cantidad_categoria * 100 / total)

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

    promedio_general = redondear_precio(
        promedio_ventas()
    )

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

        print(
            "\nNo hay ventas registradas."
            "\n==============================")
