from listas import (
    PRODUCTOS_DESCUENTO,
    PRODUCTOS,
    PRODUCTOS_CODIGO,
    PRODUCTOS_CATEGORIA,
    PRODUCTOS_NOMBRE,
    PRODUCTOS_PRECIO,
    PRODUCTOS_STOCK,
    productos_id_individual,
    productos_nombre_individual,
    ELIMINADO,
)
from Funciones.funciones import (
    obtener_caracter,
    obtener_entero,
    ordenar_por_codigo,
    ordenar_alfabeticamente,
    busqueda_secuencial,
)
from Funciones.funciones import (
    buscar,
    lista_cabeza_productos,
    generador_de_id,
    inicio,
    productos_nombres_activos,
)
import listas


def productos():
    texto = "PRODUCTOS"
    inicio(texto)

    if listas.ADMIN == True:
        ask = obtener_entero(
            "0. Retroceder\n1. Listado de producto\n2. Baja de producto\n3.Alta de producto\n4.Modificar producto...",
            0,
            4,
        )
        match ask:
            case 0:
                return
            case 1:
                listar_productos()
            case 2:
                baja_producto()
            case 3:
                alta_producto()
            case 4:
                modificar_producto()
    else:
        ask = obtener_entero("0. Retroceder\n1. Listado de producto\n", 0, 1)
        match ask:
            case 0:
                return
            case 1:
                listar_productos()


def alta_producto():
    texto = "ALTA DE PRODUCTOS"
    inicio(texto)
    pregunta_nombre = obtener_caracter("\nIngrese nombre del producto... ").upper()

    while pregunta_nombre in productos_nombres_activos():
        print("Poducto ya vigente...")
        pregunta_nombre = obtener_caracter("\nIngrese nombre del producto... ").upper()

    categoria = obtener_entero(
        "Ingrese categoría...  \n1.Alimentos\n2.Limpieza\n3.Bebidas\n4.Otros...", 1, 4
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

    precio = obtener_entero("Ingrese precio... ", 0, 100000000)

    stock = obtener_entero("Ingrese stock... ", 0, 100000)

    descuento = obtener_entero("Ingrese descuento: 1-100 (%)...", 1, 100)

    # aca hacer funcion de porcentaje y restarle el descuento al valor inicial del producto

    codigo = generador_de_id(productos_id_individual)

    pregunta_seguridad = obtener_caracter(
        "Esta seguro de agregar este producto? Y/N..."
    ).upper()
    if pregunta_seguridad == "Y":
        PRODUCTOS.append([codigo, pregunta_nombre, categoria, precio, stock, descuento])
        productos_id_individual.append(codigo)
        productos_nombre_individual.append(pregunta_nombre)
        print("\n\nProducto agregado correctamente.\n\n")
    else:
        print("Alta de producto cancelada...\n Volviendo al menu principal...")
    texto = ""
    inicio(texto)


def baja_producto():

    texto = "BAJA DE PRODUCTOS"
    inicio(texto)

    pregunta_codigo = obtener_entero(
        "\n\nIngrese código del producto a eliminar. -1 Para salir...", -1, 1000000
    )

    while pregunta_codigo == 0:
        pregunta_codigo = obtener_entero(
            "\nIngrese código del producto a eliminar. -1 Para salir...", -1, 1000000
        )

    if pregunta_codigo == -1:
        return

    pos = busqueda_secuencial(productos_id_individual, pregunta_codigo)

    while pos == -1:
        print("Producto inexistente.")
        pregunta_codigo = obtener_entero(
            "\nIngrese código del producto a eliminar. -1 Para salir...", -1, 1000000
        )
        if pregunta_codigo == -1:
            return
        pos = busqueda_secuencial(productos_id_individual, pregunta_codigo)

    pregunta_seguridad = obtener_caracter(
        f"\nEsta seguro de eliminar el producto {pregunta_codigo}? Y/N..."
    ).upper()

    if pregunta_seguridad == "Y":

        PRODUCTOS[pos][PRODUCTOS_CODIGO] = ELIMINADO
        productos_id_individual[pos] = ELIMINADO
        productos_nombre_individual[pos] = ELIMINADO

        print("Producto eliminado correctamente.")
        
    else:
        print("\nBaja de producto cancelada.")
    texto = ""
    inicio(texto)


def modificar_producto():
    texto = "MODIFICACION DE PRODUCTOS"
    inicio(texto)

    pregunta_codigo = obtener_entero(
        "\nIngrese código del producto... -1 Para salir...", -1, 1000000
    )

    while pregunta_codigo == 0:
        pregunta_codigo = obtener_entero(
            "\nIngrese código del producto... -1 Para salir...", -1, 1000000
        )

    if pregunta_codigo == -1:
        return
    pos = busqueda_secuencial(productos_id_individual, pregunta_codigo)

    if pos == -1 or pos == ELIMINADO:
        print("Producto inexistente.")

    else:
        #
        nuevo_nombre = obtener_caracter("Ingrese nuevo nombre... ")
        PRODUCTOS[pos][PRODUCTOS_NOMBRE] = nuevo_nombre
        productos_nombre_individual[pos] = nuevo_nombre

        nueva_categoria = obtener_entero(
            "\nIngrese nueva categoría... \n1. Alimentos\n2. Limpieza\n3. Bebidas\n4.Otros...",
            1,
            4,
        )

        match nueva_categoria:
            case 1:
                nueva_categoria = "ALIMENTOS"
            case 2:
                nueva_categoria = "LIMPIEZA"
            case 3:
                nueva_categoria = "BEBIDAS"
            case 4:
                nueva_categoria = "OTROS"
        precio = obtener_entero("Ingrese nuevo precio... ", 1, 100000)
            
        stock = obtener_entero("Ingrese nuevo stock: ", 0, 1000000)

        descuento = obtener_entero("Ingrese nuevo descuento: ", 1, 100)
        pregunta_seguridad = obtener_caracter(
                        f"\nEsta seguro de modificar el producto {pregunta_codigo}? Y/N..."
                    ).upper()
                
        if pregunta_seguridad == "Y":

            PRODUCTOS[pos][PRODUCTOS_DESCUENTO] = descuento

            PRODUCTOS[pos][PRODUCTOS_CATEGORIA] = nueva_categoria

            PRODUCTOS[pos][PRODUCTOS_PRECIO] = precio

            PRODUCTOS[pos][PRODUCTOS_STOCK] = stock
            print("Producto modificado correctamente.")
            texto = ""
            inicio(texto)
        else: 
            print("Modificacion cancelada...")
            texto = ""
            inicio(texto)



def listar_productos():

    texto = "LISTA DE PRODUCTOS"
    inicio(texto)
    pregunta_orden = obtener_entero(
        "\nElija metodo de ordenamiento. 1.ID  2.ALFABETICAMENTE 3.Buscar por nombre. 4.Buscar por codigo. -1 para salir...",
        -1,
        4,
    )
    if pregunta_orden == -1:
        return
    if pregunta_orden == 0:
        pregunta_orden = obtener_entero(
            "\nElija metodo de ordenamiento. 1.ID  2.ALFABETICAMENTE 3.Buscar por nombre. 4.Buscar por codigo. -1 para salir...",
            -1,
            4,
        )

    if pregunta_orden == 1:
        lista_cabeza_productos()
        print()
        ordenar_por_codigo()
    if pregunta_orden == 2:
        lista_cabeza_productos()
        print()
        ordenar_alfabeticamente()

    if pregunta_orden == 3:
        pregunta = obtener_caracter("\nIngrese nombre del producto...").upper()
        cuenta_busqueda, busqueda_posiciones = buscar(
            productos_nombre_individual, pregunta
        )
        if cuenta_busqueda == 0:
            print("Producto no encontrado...")
            return
        else:
            i = 0
            print(f"\nCantidad de productos encontrados...{cuenta_busqueda}\n")
            while i < cuenta_busqueda:
                producto = PRODUCTOS[busqueda_posiciones[i]]
                if producto[PRODUCTOS_CODIGO] != ELIMINADO:
                    print(f"\n{producto}\n")
                i += 1
            texto = ""
            inicio(texto)

    if pregunta_orden == 4:
        pregunta = obtener_entero("\nIngrese codigo del producto...", 100000, 1000000)
        cuenta_busqueda, busqueda_posiciones = buscar(productos_id_individual, pregunta)
        if cuenta_busqueda == 0:
            print("Producto no encontrado...")
            return
        else:
            i = 0
            while i < cuenta_busqueda:
                producto = PRODUCTOS[busqueda_posiciones[i]]
                if producto[PRODUCTOS_CODIGO] != ELIMINADO:
                    print(f"\nProducto encontrado...{cuenta_busqueda}\n")
                    print(f"\n{producto}\n")
                i += 1
            texto = ""
            inicio(texto)
