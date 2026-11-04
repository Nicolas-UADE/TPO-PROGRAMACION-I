from modulos.listas import (
    PRODUCTOS_DESCUENTO,
    PRODUCTOS_CODIGO,
    PRODUCTOS_CATEGORIA,
    PRODUCTOS_NOMBRE,
    PRODUCTOS_PRECIO,
    PRODUCTOS_STOCK,
    ELIMINADO,
)
from Funciones.archivos_productos import agregar_producto_archivo, reemplazar_producto_archivo,cargar_productos_archivo
from Funciones.funciones_uni import (
    obtener_caracter,
    obtener_entero,
    ordenar_por_codigo,
    ordenar_alfabeticamente,
    busqueda_por_codigo,
    inicio_alta,
    inicio_modificar,
    inicio_baja,
    inicio_listado,
    generador_de_id,
)


def actualizar_producto(codigo, columna, valor):
    """Modifica un campo del producto en el archivo. Busca por codigo."""
    productos = cargar_productos_archivo()
    pos = busqueda_por_codigo(productos, codigo)
    if pos == -1:
        return False

    producto = productos[pos]
    producto_nuevo = [
        producto[PRODUCTOS_CODIGO],
        producto[PRODUCTOS_NOMBRE],
        producto[PRODUCTOS_CATEGORIA],
        producto[PRODUCTOS_PRECIO],
        producto[PRODUCTOS_STOCK],
        producto[PRODUCTOS_DESCUENTO],
    ]
    producto_nuevo[columna] = valor

    return reemplazar_producto_archivo(codigo, producto_nuevo)


def alta_producto():
    """Permite cargar un producto nuevo con sus datos."""
    texto = "ALTA DE PRODUCTOS"
    inicio_alta(texto)

    try:
        productos = cargar_productos_archivo()

        pregunta_nombre = obtener_caracter("\nIngrese nombre del producto\n.").upper()

        while pregunta_nombre in productos_nombres_activos(productos):
            print("Producto ya vigente...")
            pregunta_nombre = obtener_caracter("\nIngrese nombre del producto\n.").upper()

        categoria = obtener_entero(
            "\nIngrese categoría...  \n[1] Alimentos\n[2] Limpieza\n[3] Bebidas\n[4] Otros\n.",
            1,
            4,
        )

        match categoria:
            case 1:
                categoria = "ALIMENTOS"
            case 2:
                categoria = "LIMPIEZA"
            case 3:
                categoria = "BEBIDAS"
            case 4:
                categoria = "OTROS"

        precio = obtener_entero("Ingrese precio\n.", 0, 100000000)

        stock = obtener_entero("Ingrese stock\n.", 0, 100000)

        descuento = obtener_entero("Ingrese descuento: 0-100 (%)\n.", 0, 100)

        codigos = [producto[PRODUCTOS_CODIGO] for producto in productos]
        codigo = generador_de_id(codigos)

        pregunta_seguridad = obtener_caracter(
            "Esta seguro de agregar este producto? Y/N\n."
        ).upper()
        if pregunta_seguridad == "Y":
            producto = [codigo, pregunta_nombre, categoria, precio, stock, descuento]
            if agregar_producto_archivo(producto):
                print("\n\033[32mProducto agregado correctamente.\033[0m")
        else:
            print("\n\033[31mAlta de producto cancelada.\033[0m")
    except (FileNotFoundError, OSError) as error:
        print(f"\n\033[31mError!:{error}\033[0m")

    texto = ""
    inicio_alta(texto)
 
 
def baja_producto():
    """Permite dar de baja un producto existente."""
    texto = "BAJA DE PRODUCTOS"
    inicio_baja(texto)

    try:
        productos = cargar_productos_archivo()

        pregunta_codigo = obtener_entero(
            "\n\nIngrese código del producto a eliminar.\n-1 para salir\n.", -1, 1000000
        )

        while pregunta_codigo == 0:
            pregunta_codigo = obtener_entero(
                "\nIngrese código del producto a eliminar.\n-1 para salir\n.", -1, 1000000
            )

        if pregunta_codigo == -1:
            return

        pos = busqueda_por_codigo(productos, pregunta_codigo)

        while pos == -1:
            print("Producto inexistente.")
            pregunta_codigo = obtener_entero(
                "\nIngrese código del producto a eliminar.\n-1 para salir\n.", -1, 1000000
            )
            if pregunta_codigo == -1:
                return
            pos = busqueda_por_codigo(productos, pregunta_codigo)

        pregunta_seguridad = obtener_caracter(
            f"\nEsta seguro de eliminar el producto {pregunta_codigo}? Y/N\n."
        ).upper()

        if pregunta_seguridad == "Y":
            producto = productos[pos]
            producto_nuevo = [
                ELIMINADO,
                producto[PRODUCTOS_NOMBRE],
                producto[PRODUCTOS_CATEGORIA],
                producto[PRODUCTOS_PRECIO],
                producto[PRODUCTOS_STOCK],
                producto[PRODUCTOS_DESCUENTO],
            ]
            if reemplazar_producto_archivo(pregunta_codigo, producto_nuevo):
                print("\n\033[32mProducto eliminado correctamente.\033[0m")
        else:
            print("\n\033[31mBaja de producto cancelada.\033[0m")
    except (FileNotFoundError, OSError) as error:
        print(f"\n\033[31mError!: {error}\033[0m")

    texto = ""
    inicio_baja(texto)



def modificar_producto():
    """Permite modificar los datos de un producto."""
    texto = "MODIFICACION DE PRODUCTOS"
    inicio_modificar(texto)

    try:
        productos = cargar_productos_archivo()

        pregunta_codigo = obtener_entero(
            "\nIngrese código del producto.\n-1 para salir\n.", -1, 1000000
        )

        while pregunta_codigo == 0:
            pregunta_codigo = obtener_entero(
                "\nIngrese código del producto.\n-1 para salir\n.", -1, 1000000
            )

        if pregunta_codigo == -1:
            return

        pos = busqueda_por_codigo(productos, pregunta_codigo)

        if pos == -1:
            print("Producto inexistente.")
            return

        pregunta_eleccion = obtener_entero(
            "Que quieres modificar.\n[1] Nombre\n[2] Categoria\n[3] Precio\n[4] Stock\n[5] Descuento\n.",
            1,
            5,
        )

        match pregunta_eleccion:
            case 1:
                columna = PRODUCTOS_NOMBRE
                nuevo_valor = obtener_caracter("\nIngrese nuevo nombre.\n.")
                while nuevo_valor in productos_nombres_activos(productos):
                    print("Producto ya vigente...")
                    nuevo_valor = obtener_caracter("\nIngrese nuevo nombre.\n.")

            case 2:
                columna = PRODUCTOS_CATEGORIA
                nuevo_valor = obtener_entero(
                    "\nIngrese nueva categoría... \n[1] Alimentos\n[2] Limpieza\n[3] Bebidas\n[4] Otros\n.",
                    1,
                    4,
                )
                match nuevo_valor:
                    case 1:
                        nuevo_valor = "ALIMENTOS"
                    case 2:
                        nuevo_valor = "LIMPIEZA"
                    case 3:
                        nuevo_valor = "BEBIDAS"
                    case 4:
                        nuevo_valor = "OTROS"

            case 3:
                columna = PRODUCTOS_PRECIO
                nuevo_valor = obtener_entero("\nIngrese nuevo precio.\n.", 0, 100000000)

            case 4:
                columna = PRODUCTOS_STOCK
                nuevo_valor = obtener_entero("\nIngrese nuevo stock.\n.", 0, 100000)

            case 5:
                columna = PRODUCTOS_DESCUENTO
                nuevo_valor = obtener_entero("\nIngrese nuevo descuento.\n.", 0, 100)

        pregunta_seguridad = obtener_caracter(
            f"\nEsta seguro de modificar el producto {pregunta_codigo}? Y/N\n."
        ).upper()

        if pregunta_seguridad == "Y":
            if not actualizar_producto(pregunta_codigo, columna, nuevo_valor):
                return
            print("\n\033[32mProducto modificado correctamente.\033[0m")

            pregunta_otra = obtener_caracter(
                "Desea hacer otra modificacion? Y/N\n."
            ).upper()
            if pregunta_otra == "Y":
                modificar_producto()
        else:
            print("\n\033[31mModificacion de producto cancelada.\033[0m")

    except (FileNotFoundError, OSError) as error:
        print(f"\n\033[31mError!: {error}\033[0m")
 
def listar_productos():
    """Muestra los productos y permite ordenarlos o buscarlos."""
    texto = "LISTA DE PRODUCTOS"
    inicio_listado(texto)

    try:
        productos = cargar_productos_archivo()

        pregunta_orden = obtener_entero(
            "\nElija metodo de ordenamiento.\n[1] ID\n[2] ALFABETICAMENTE\n[3] Buscar por nombre\n[4] Buscar por codigo.\n-1 para salir\n.",
            -1,
            4,
        )

        while pregunta_orden == 0:
            pregunta_orden = obtener_entero(
                "\nElija metodo de ordenamiento.\n[1] ID\n[2] ALFABETICAMENTE\n[3] Buscar por nombre\n[4] Buscar por codigo.\n-1 para salir\n.",
                -1,
                4,
            )

        match pregunta_orden:
            case -1:
                return

            case 1:
                lista_cabeza_productos()
                print()
                ordenar_por_codigo(productos)

            case 2:
                lista_cabeza_productos()
                print()
                ordenar_alfabeticamente(productos)

            case 3:
                pregunta = obtener_caracter("\nIngrese nombre del producto\n.").upper()
                encontrados = [
                    p
                    for p in productos
                    if p[PRODUCTOS_CODIGO] != ELIMINADO and p[PRODUCTOS_NOMBRE] == pregunta
                ]

                if len(encontrados) == 0:
                    print("Producto no encontrado...")
                    return

                print(f"\nCantidad de productos encontrados: {len(encontrados)}\n")
                for producto in encontrados:
                    print(f"\n{producto}\n")

            case 4:
                pregunta = obtener_entero(
                    "\nIngrese codigo del producto\n.", 100000, 1000000
                )
                pos = busqueda_por_codigo(productos, pregunta)

                if pos == -1:
                    print("Producto no encontrado...")
                    return

                print("\nProducto encontrado...\n")
                print(f"\n{productos[pos]}\n")

    except (FileNotFoundError, OSError) as error:
        print(f"\n\033[31mError!: {error}\033[0m")

    texto = ""
    inicio_listado(texto)
 

def lista_cabeza_productos():
    """Imprime el encabezado de la tabla de productos (los titulos de cada columna)."""
    list = []
    codigo = "Codigo"
    nombre = "Nombre"
    tipo = "Categoria"
    precio = "Precio"
    stock = "Stock"
    descuento = "Descuento"
    list.append(codigo), list.append(nombre), list.append(tipo), list.append(
        precio
    ), list.append(stock), list.append(descuento)
    ancho = 118
    print("-" * ancho)
    print(
        f"|{list[0]:<15} | {list[1]:<15} | {list[2]:<15} | {list[3]:<15} | {list[4]:<15} | {list[5]:<15}"
    )

    print("-" * ancho)


def productos_nombres_activos(productos):
    """Devuelve solo los nombres de productos que no fueron eliminados."""
    return [p[PRODUCTOS_NOMBRE] for p in productos if p[PRODUCTOS_CODIGO] != ELIMINADO]