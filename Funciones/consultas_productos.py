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


