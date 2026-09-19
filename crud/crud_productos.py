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
    inicio_alta,
    inicio_modificar,
    inicio_baja,
    inicio_listado,
)
from Funciones.funciones import (
    buscar,
    lista_cabeza_productos,
    generador_de_id,
    inicio,
    productos_nombres_activos,
)
import listas

# from login import ADMIN


def productos():
    # Menu principal del modulo productos. Cambia segun si el usuario es admin o no.
    texto = "PRODUCTOS"
    inicio(texto)

    if listas.ADMIN == True:
        # Admin ve todas las opciones: listar, dar de baja, dar de alta y modificar.
        ask = obtener_entero(
            "0. Retroceder\n1. Listado de producto\n2. Baja de producto\n3.Alta de producto\n4.Modificar producto\n.",
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
        # Usuario normal solo puede ver el listado.
        ask = obtener_entero("0. Retroceder\n1. Listado de producto\n", 0, 1)
        match ask:
            case 0:
                return
            case 1:
                listar_productos()


def alta_producto():
    # Carga un producto nuevo pidiendo sus datos uno por uno.
    texto = "ALTA DE PRODUCTOS"
    inicio_alta(texto)
    pregunta_nombre = obtener_caracter("\nIngrese nombre del producto\n.").upper()

    # No deja cargar un producto si ya existe uno activo con ese mismo nombre.
    while pregunta_nombre in productos_nombres_activos():
        print("Poducto ya vigente...")
        pregunta_nombre = obtener_caracter("\nIngrese nombre del producto\n.").upper()

    categoria = obtener_entero(
        "\nIngrese categoría...  \n1.Alimentos\n2.Limpieza\n3.Bebidas\n4.Otros\n.", 1, 4
    )

    # Convierte el numero elegido en el texto de la categoria.
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

    descuento = obtener_entero("Ingrese descuento: 1-100 (%)\n.", 1, 100)

    # aca hacer funcion de porcentaje y restarle el descuento al valor inicial del producto

    # Genera un codigo unico para el producto nuevo.
    codigo = generador_de_id(productos_id_individual)

    # Confirmacion antes de guardar el producto.
    pregunta_seguridad = obtener_caracter(
        "Esta seguro de agregar este producto? Y/N\n."
    ).upper()
    if pregunta_seguridad == "Y":
        # Se guarda tanto en la lista principal de productos como en las listas auxiliares de id y nombre.
        PRODUCTOS.append([codigo, pregunta_nombre, categoria, precio, stock, descuento])
        productos_id_individual.append(codigo)
        productos_nombre_individual.append(pregunta_nombre)
        print("\n\033[32mProducto agregado correctamente.\033[0m")
    else:
        print("\n\033[31mAlta de producto cancelada.\033[0m")
    texto = ""
    inicio_alta(texto)


def baja_producto():
    # Elimina un producto (lo marca como ELIMINADO en las 3 listas relacionadas).
    texto = "BAJA DE PRODUCTOS"
    inicio_baja(texto)

    pregunta_codigo = obtener_entero(
        "\n\nIngrese código del producto a eliminar. -1 Para salir\n.", -1, 1000000
    )

    # Si ingresa 0 (no es una opcion valida), se lo vuelve a pedir.
    while pregunta_codigo == 0:
        pregunta_codigo = obtener_entero(
            "\nIngrese código del producto a eliminar. -1 Para salir\n.", -1, 1000000
        )

    if pregunta_codigo == -1:
        return

    pos = busqueda_secuencial(productos_id_individual, pregunta_codigo)

    # Si el codigo no existe, se lo vuelve a pedir hasta encontrar uno valido o salir.
    while pos == -1:
        print("Producto inexistente.")
        pregunta_codigo = obtener_entero(
            "\nIngrese código del producto a eliminar. -1 Para salir\n.", -1, 1000000
        )
        if pregunta_codigo == -1:
            return
        pos = busqueda_secuencial(productos_id_individual, pregunta_codigo)

    # Confirmacion antes de borrar.
    pregunta_seguridad = obtener_caracter(
        f"\nEsta seguro de eliminar el producto {pregunta_codigo}? Y/N\n."
    ).upper()

    if pregunta_seguridad == "Y":
        # Se marca como eliminado en las 3 listas para mantenerlas sincronizadas.
        PRODUCTOS[pos][PRODUCTOS_CODIGO] = ELIMINADO
        productos_id_individual[pos] = ELIMINADO
        productos_nombre_individual[pos] = ELIMINADO

        print("\n\033[32mProductos eliminado correctamente.\033[0m")

    else:
        print("\n\033[31mBaja de producto cancelada.\033[0m")
    texto = ""
    inicio_baja(texto)


def modificar_producto():
    # Permite modificar un dato puntual de un producto ya existente.
    texto = "MODIFICACION DE PRODUCTOS"
    inicio_modificar(texto)

    pregunta_codigo = obtener_entero(
        "\nIngrese código del producto... -1 Para salir\n.", -1, 1000000
    )

    while pregunta_codigo == 0:
        pregunta_codigo = obtener_entero(
            "\nIngrese código del producto... -1 Para salir\n.", -1, 1000000
        )

    if pregunta_codigo == -1:
        return
    pos = busqueda_secuencial(productos_id_individual, pregunta_codigo)

    if pos == -1 or pos == ELIMINADO:
        print("Producto inexistente.")

    else:
        # Pregunta que campo se quiere modificar.
        pregunta_eleccion = obtener_entero(
            "Que quieres modificar.\n1.Nombre\n2.Categoria\n3.Precio\n4.Stock\n5.Descuento\n.",
            1,
            5,
        )
        match pregunta_eleccion:
            case 1:
                # Modificar nombre.
                nuevo_nombre = obtener_caracter("\nIngrese nuevo nombre.\n.")
                pregunta_seguridad = obtener_caracter(
                    f"\nEsta seguro de modificar el producto {pregunta_codigo}? Y/N\n."
                ).upper()

                if pregunta_seguridad == "Y":
                    # Se actualiza en la lista principal y tambien en la lista auxiliar de nombres.
                    PRODUCTOS[pos][PRODUCTOS_NOMBRE] = nuevo_nombre
                    productos_nombre_individual[pos] = nuevo_nombre
                    print("\n\033[32mProducto modificado correctamente.\033[0m")
                    pregunta_eleccion_otra = obtener_caracter(
                        "Desea hacer otra modificacion? Y/N\n"
                    )
                    if pregunta_eleccion_otra == "Y":
                        # Si quiere seguir modificando, arranca todo el proceso de nuevo.
                        texto = ""
                        inicio_modificar(texto)
                        modificar_producto()
                else:
                    print("\n\033[31mModificacion de producto cancelada.\033[0m")

            case 3:
                # Modificar precio.
                precio = obtener_entero("\nIngrese nuevo precio.\n.", 1, 100000)
                pregunta_seguridad = obtener_caracter(
                    f"\nEsta seguro de modificar el producto {pregunta_codigo}? Y/N\n."
                ).upper()

                if pregunta_seguridad == "Y":
                    PRODUCTOS[pos][PRODUCTOS_PRECIO] = precio
                    print("\n\033[32mProducto modificado correctamente.\033[0m")
                    pregunta_eleccion_otra = obtener_caracter(
                        "Desea hacer otra modificacion? Y/N\n"
                    )
                    if pregunta_eleccion_otra == "Y":
                        texto = ""
                        inicio_modificar(texto)
                        modificar_producto()
                else:
                    print("\n\033[31mModificacion de producto cancelada.\033[0m")

            case 4:
                # Modificar stock.
                stock = obtener_entero("\nIngrese nuevo stock.\n.", 0, 1000000)
                pregunta_seguridad = obtener_caracter(
                    f"\nEsta seguro de modificar el producto {pregunta_codigo}? Y/N\n."
                ).upper()

                if pregunta_seguridad == "Y":
                    PRODUCTOS[pos][PRODUCTOS_STOCK] = stock
                    print("\n\033[32mProducto modificado correctamente.\033[0m")
                    pregunta_eleccion_otra = obtener_caracter(
                        "Desea hacer otra modificacion? Y/N\n"
                    )
                    if pregunta_eleccion_otra == "Y":
                        texto = ""
                        inicio_modificar(texto)
                        modificar_producto()
                else:
                    print("\n\033[31mModificacion de producto cancelada.\033[0m")

            case 5:
                # Modificar descuento.
                descuento = obtener_entero("\nIngrese nuevo descuento.\n.", 1, 100)
                pregunta_seguridad = obtener_caracter(
                    f"\nEsta seguro de modificar el producto {pregunta_codigo}? Y/N\n."
                ).upper()

                if pregunta_seguridad == "Y":
                    PRODUCTOS[pos][PRODUCTOS_DESCUENTO] = descuento
                    print("\n\033[32mProducto modificado correctamente.\033[0m")
                    pregunta_eleccion_otra = obtener_caracter(
                        "Desea hacer otra modificacion? Y/N\n"
                    )
                    if pregunta_eleccion_otra == "Y":
                        texto = ""
                        inicio_modificar(texto)
                        modificar_producto()
                else:
                    print("\n\033[31mModificacion de producto cancelada.\033[0m")

            case 2:
                # Modificar categoria.
                nueva_categoria = obtener_entero(
                    "\nIngrese nueva categoría... \n1. Alimentos\n2. Limpieza\n3. Bebidas\n4.Otros\n.",
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
                pregunta_seguridad = obtener_caracter(
                    f"\nEsta seguro de modificar el producto {pregunta_codigo}? Y/N\n."
                ).upper()

                if pregunta_seguridad == "Y":
                    PRODUCTOS[pos][PRODUCTOS_CATEGORIA] = nueva_categoria

                    print("\n\033[32mProducto modificado correctamente.\033[0m")

                    pregunta_eleccion_otra = obtener_caracter(
                        "Desea hacer otra modificacion? Y/N\n"
                    )
                    if pregunta_eleccion_otra == "Y":
                        texto = ""
                        inicio_modificar(texto)
                        modificar_producto()
                else:
                    print("\n\033[31mModificacion de producto cancelada.\033[0m")


def listar_productos():
    # Muestra el listado de productos, con distintas formas de ordenar o buscar.
    texto = "LISTA DE PRODUCTOS"
    inicio_listado(texto)
    pregunta_orden = obtener_entero(
        "\nElija metodo de ordenamiento. 1.ID  2.ALFABETICAMENTE 3.Buscar por nombre. 4.Buscar por codigo. -1 para salir\n.",
        -1,
        4,
    )
    if pregunta_orden == -1:
        return
    if pregunta_orden == 0:
        # Vuelve a preguntar si ingreso 0 (no es una opcion valida del menu).
        pregunta_orden = obtener_entero(
            "\nElija metodo de ordenamiento. 1.ID  2.ALFABETICAMENTE 3.Buscar por nombre. 4.Buscar por codigo. -1 para salir\n.",
            -1,
            4,
        )

    if pregunta_orden == 1:
        # Lista todos los productos ordenados por codigo.
        lista_cabeza_productos()
        print()
        ordenar_por_codigo()
    if pregunta_orden == 2:
        # Lista todos los productos ordenados alfabeticamente.
        lista_cabeza_productos()
        print()
        ordenar_alfabeticamente()

    if pregunta_orden == 3:
        # Busca uno o varios productos por nombre (puede haber nombres repetidos).
        pregunta = obtener_caracter("\nIngrese nombre del producto\n.").upper()
        cuenta_busqueda, busqueda_posiciones = buscar(
            productos_nombre_individual, pregunta
        )
        if cuenta_busqueda == 0:
            print("Producto no encontrado...")
            return
        else:
            i = 0
            print(f"\nCantidad de productos encontrados: {cuenta_busqueda}\n")
            while i < cuenta_busqueda:
                producto = PRODUCTOS[busqueda_posiciones[i]]
                if producto[PRODUCTOS_CODIGO] != ELIMINADO:
                    print(f"\n{producto}\n")
                i += 1

    if pregunta_orden == 4:
        # Busca un producto puntual por codigo.
        pregunta = obtener_entero("\nIngrese codigo del producto\n.", 100000, 1000000)
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
    inicio_listado(texto)