





def promedio_ventas_categoria(VENTAS, categoria):
    suma = 0
    contador = 0

    for fila in VENTAS:

        if fila[2] == categoria:
            suma = suma + fila[4]
            contador = contador + 1

    if contador > 0:
        promedio = suma / contador
        return promedio

    return 0