from modulos.listas import PRODUCTOS_CODIGO, VENTAS_CANTIDAD


def busqueda_secuencial(lista, parametro, i=0):
    """Recorre la lista elemento por elemento (de forma recursiva) hasta encontrar el parametro. Devuelve -1 si no esta."""
    # caso base: llegamos al final de la lista, el parametro no esta
    if i == len(lista):
        return -1

    # caso base: encontramos el parametro en la posicion i
    if lista[i] == parametro:
        return i

    # caso recursivo: seguimos buscando desde la posicion siguiente (se reduce el dominio con i + 1)
    return busqueda_secuencial(lista, parametro, i + 1)


def busqueda_por_codigo(lista, codigo, i=0):
    """Igual que busqueda_secuencial pero para productos, comparando por su codigo. Es recursiva."""
    # caso base: no quedan productos por revisar, el codigo no esta
    if i == len(lista):
        return -1

    # caso base: el producto de la posicion i tiene ese codigo
    if lista[i][PRODUCTOS_CODIGO] == codigo:
        return i

    # caso recursivo: revisamos el siguiente producto
    return busqueda_por_codigo(lista, codigo, i + 1)


def sumar_cantidades_recursivo(filas, i=0):
    """Suma la cantidad vendida de cada fila de ventas, de forma recursiva."""
    # caso base: ya sumamos todas las filas
    if i == len(filas):
        return 0

    # caso recursivo: cantidad de esta fila + la suma del resto (el dominio se reduce con i + 1)
    return filas[i][VENTAS_CANTIDAD] + sumar_cantidades_recursivo(filas, i + 1)