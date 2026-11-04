from modulos.listas import (
    PRODUCTOS_CODIGO,
    PRODUCTOS_NOMBRE,
    PRODUCTOS_CATEGORIA,
    ELIMINADO,
)



    
def categorias_distintas(productos):
    """Devuelve un conjunto con las categorias que aparecen en PRODUCTOS (sin repetir)."""

    return {f[PRODUCTOS_CATEGORIA] for f in productos if f[PRODUCTOS_CODIGO] != ELIMINADO}

def codigos_activos(productos):
    """Devuelve un conjunto con los codigos de los productos que no fueron dados de baja."""
    return {fila[PRODUCTOS_CODIGO] for fila in productos if fila[PRODUCTOS_CODIGO] != ELIMINADO}



def nombres_activos(productos):
    """Devuelve la lista de nombres de los productos activos, usando comprension de listas."""
    return [fila[PRODUCTOS_NOMBRE] for fila in productos if fila[PRODUCTOS_CODIGO] != ELIMINADO]



def nombres_por_categoria(productos, categoria):
    """Devuelve los nombres de los productos activos de una categoria."""
    return [
        fila[PRODUCTOS_NOMBRE]
        for fila in productos
        if fila[PRODUCTOS_CATEGORIA] == categoria and fila[PRODUCTOS_CODIGO] != ELIMINADO
    ]