from modulos.listas import PRODUCTOS_CODIGO, VENTAS_CANTIDAD


def sumar_cantidades_recursivo(filas, i=0):
    """Suma la cantidad vendida de cada fila de ventas, de forma recursiva."""
    # caso base: ya sumamos todas las filas
    if i == len(filas):
        return 0

    # caso recursivo: cantidad de esta fila + la suma del resto (el dominio se reduce con i + 1)
    return filas[i][VENTAS_CANTIDAD] + sumar_cantidades_recursivo(filas, i + 1)