



def promedio_ventas(VENTAS):
    suma = 0

    for fila in VENTAS:
        suma = suma + fila[4]

    if len(VENTAS) > 0:
        promedio = suma / len(VENTAS)
        return promedio

    return 0
