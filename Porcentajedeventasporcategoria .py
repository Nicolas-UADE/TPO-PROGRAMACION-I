def porcentaje_ventas_categoria(VENTAS, categoria):
    total = contar_ventas(VENTAS)
    cantidad_categoria = contar_ventas_categoria(VENTAS, categoria)

    if total > 0:
        porcentaje = cantidad_categoria * 100 / total
        return porcentaje

    return 0

