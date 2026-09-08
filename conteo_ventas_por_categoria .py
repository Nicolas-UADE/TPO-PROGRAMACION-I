def contar_ventas_categoria(VENTAS, categoria):
    contador = 0

    for fila in VENTAS:

        if fila[2] == categoria:
            contador = contador + 1

    return contador