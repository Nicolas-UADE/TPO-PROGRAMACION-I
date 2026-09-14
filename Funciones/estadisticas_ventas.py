from functools import reduce

from listas import (
    VENTAS,
    VENTAS_ID,
    VENTAS_CATEGORIA,
    VENTAS_CANTIDAD,
    VENTAS_IMPORTE,
    PRODUCTOS,
    PRODUCTOS_CODIGO,
    PRODUCTOS_CATEGORIA,
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

    ids_ventas = []

    for fila in obtener_ventas_activas():

        if fila[VENTAS_ID] not in ids_ventas:

            ids_ventas.append(fila[VENTAS_ID])

    return ids_ventas




def obtener_categorias():

    categorias = []

    for producto in PRODUCTOS:

        if producto[PRODUCTOS_CODIGO] != ELIMINADO:

            categoria = producto[PRODUCTOS_CATEGORIA]

            if categoria not in categorias:

                categorias.append(categoria)

    categorias.sort()

    return categorias




def total_venta(id_venta):

    total = 0

    for fila in VENTAS:

        if fila[VENTAS_ID] == id_venta:

            total = (total + fila[VENTAS_IMPORTE])

    return total




def contar_ventas():

    ids_ventas = obtener_ids_ventas()

    return len(ids_ventas)




def contar_ventas_categoria(categoria):

    ids_ventas = []

    categoria = categoria.upper()

    for fila in VENTAS:

        if fila[VENTAS_ID] != ELIMINADO:

            if (fila[VENTAS_CATEGORIA] == categoria):

                if (fila[VENTAS_ID] not in ids_ventas):

                    ids_ventas.append(fila[VENTAS_ID])

    return len(ids_ventas)




def promedio_ventas():

    ids_ventas = obtener_ids_ventas()

    suma_total = sumar_importes_ventas()

    if len(ids_ventas) > 0:

        promedio = ( suma_total / len(ids_ventas)
        )

    else:

        promedio = 0

    return promedio




def promedio_ventas_categoria(categoria):

    categoria = categoria.upper()

    ids_ventas = []

    total_categoria = 0

    for fila in VENTAS:

        if fila[VENTAS_ID] != ELIMINADO:

            if (fila[VENTAS_CATEGORIA] == categoria):

                total_categoria = (total_categoria + fila[VENTAS_IMPORTE])

                if ( fila[VENTAS_ID] not in ids_ventas):

                    ids_ventas.append(fila[VENTAS_ID])

    if len(ids_ventas) > 0:

        promedio = (total_categoria / len(ids_ventas))

    else:

        promedio = 0

    return promedio




def porcentaje_ventas_categoria(categoria):

    total = contar_ventas()

    cantidad_categoria = (contar_ventas_categoria(categoria))

    if total > 0:

        porcentaje = (cantidad_categoria * 100 / total)

    else:

        porcentaje = 0

    return porcentaje




def total_productos_vendidos():

    cantidad_total = 0

    for fila in VENTAS:

        if fila[VENTAS_ID] != ELIMINADO:

            cantidad_total = (cantidad_total + fila[VENTAS_CANTIDAD])

    return cantidad_total




def mayor_menor_venta():

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



def resumen_estadistico():

    cantidad_ventas = contar_ventas()

    promedio_general = redondear_precio(
        promedio_ventas()
    )

    productos_vendidos = total_productos_vendidos()

    categorias = obtener_categorias()

    texto_categorias = ""

    for categoria in categorias:

        cantidad = contar_ventas_categoria(categoria)

        promedio = redondear_precio(promedio_ventas_categoria(categoria))

        porcentaje = redondear_precio(porcentaje_ventas_categoria(categoria))

        texto_categorias = (texto_categorias
            + f"\nCategoria: {categoria}"
            + f"\nCantidad de ventas: {cantidad}"
            + f"\nPromedio: ${promedio}"
            + f"\nPorcentaje: {porcentaje}%"
            + "\n")

    print(
        "\n=============================="
        "\n   ESTADISTICAS DE VENTAS"
        "\n=============================="
        f"\nCantidad total de ventas: {cantidad_ventas}"
        f"\nPromedio general: ${promedio_general}"
        f"\nTotal de productos vendidos: {productos_vendidos}"
        "\n"
    )

    print(
        "ESTADISTICAS POR CATEGORIA"
        "\n------------------------------"
        f"{texto_categorias}")

    if cantidad_ventas > 0:

        (
            id_mayor,
            mayor,
            id_menor,
            menor,
        ) = mayor_menor_venta()

        print(
            "------------------------------"
            f"\nMayor venta: {id_mayor}"
            f"\nImporte: ${redondear_precio(mayor)}"
            "\n"
            f"\nMenor venta: {id_menor}"
            f"\nImporte: ${redondear_precio(menor)}"
            "\n=============================="
        )

    else:

        print(
            "\nNo hay ventas registradas."
            "\n==============================")
