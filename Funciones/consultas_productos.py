from modulos.listas import (
    PRODUCTOS,
    PRODUCTOS_CODIGO,
    PRODUCTOS_NOMBRE,
    PRODUCTOS_CATEGORIA,
    ELIMINADO,
)


def categorias_distintas():
    """Devuelve un conjunto con las categorias que aparecen en PRODUCTOS (sin repetir)."""
    return {fila[PRODUCTOS_CATEGORIA] for fila in PRODUCTOS}


def codigos_activos():
    """Devuelve un conjunto con los codigos de los productos que no fueron dados de baja."""
    return {fila[PRODUCTOS_CODIGO] for fila in PRODUCTOS if fila[PRODUCTOS_CODIGO] != ELIMINADO}



