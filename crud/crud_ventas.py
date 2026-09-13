from listas import (
    PRODUCTOS_NOMBRE,
)

from Funciones.funciones import (
    calcular_descuentos,
    inicio,
    productos_activos,
)


def mostrar_precios_con_descuento():
    texto = "PRECIOS CON DESCUENTO"
    inicio(texto)

    activos = productos_activos()
    precios = calcular_descuentos(activos)

    for i in range(len(activos)):
        producto = activos[i]
        precio = precios[i]
        nombre = producto[PRODUCTOS_NOMBRE]
        print(f"{nombre}: {precio}")
