from listas import ADMIN,PRODUCTOS_DESCUENTO,PRODUCTOS,PRODUCTOS_CODIGO,PRODUCTOS_CATEGORIA,PRODUCTOS_NOMBRE,PRODUCTOS_PRECIO,PRODUCTOS_STOCK,productos_id_individual,productos_nombre_individual
from Funciones.funciones import busqueda_por_codigo,obtener_caracter,obtener_entero,ordenar_por_codigo,ordenar_alfabeticamente,volver_al_menu,busqueda_secuencial
from Funciones.funciones import buscar,lista_cabeza_productos
from menu import menu_principal
def productos():
    print("\n\n==========\nPRODUCTOS\n==========")
    if ADMIN == True:
        ask = obtener_entero(
            "0. Retroceder\n1. Listado de producto\n2. Baja de producto\n3.Alta de producto\n4.Modificar producto...",
            0,
            4,
        )
        match ask:
            case 0:
                volver_al_menu()
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
                volver_al_menu()
            case 1:
                listar_productos()


def alta_producto():
    print("\n\n==========ALTA DE PRODUCTOS==========")

    pregunta_codigo = obtener_entero(
        "\nIngrese código del producto... -1 Para salir...", -1, 1000000
    )

    while pregunta_codigo == 0:pregunta_codigo = obtener_entero("\nIngrese código del producto a eliminar. -1 Para salir...", -1, 1000000)

    if pregunta_codigo == -1:
        volver_al_menu()

    pos = busqueda_secuencial()

    while pos != -1:
        print("Ya existe un producto con ese código.")

        pregunta_codigo = obtener_entero(
            "\nIngrese código del producto... -1 Para salir...", -1, 1000000
        )

        if pregunta_codigo == -1:
                volver_al_menu()

        pos = busqueda_secuencial()

    else:
        pregunta_nombre = obtener_caracter("\nIngrese nombre del producto... ").upper()

        print("\n1. Alimentos\n2. Limpieza\n3. Bebidas")

        categoria = obtener_entero("Ingrese categoría... ", 1, 3)

        precio = float(input("Ingrese precio... "))

        while precio <= 0:
            precio = float(input("Precio inválido. Reingrese... "))

        stock = obtener_entero("Ingrese stock... ", 0, 100000)

        descuento = float(input("Ingrese descuento: "))

        while descuento < 0 or descuento > 100:
            descuento = float(input("Descuento inválido. Reingrese: "))

        PRODUCTOS.append(
            pregunta_codigo, pregunta_nombre, categoria, precio, stock, descuento
        )
        print("\n\nProducto agregado correctamente.\n\n")
        print("===================")


def baja_producto():

    print("\n\n==========BAJA DE PRODUCTOS==========")

    pregunta_codigo = obtener_entero(
        "\n\nIngrese código del producto a eliminar. -1 Para salir...", -1, 1000000
    )

    while pregunta_codigo == 0:
        pregunta_codigo = obtener_entero("\nIngrese código del producto a eliminar. -1 Para salir...", -1, 1000000)

    if pregunta_codigo == -1:
        volver_al_menu()

    pos = busqueda_secuencial(PRODUCTOS, pregunta_codigo)

    while pos == -1:
        print("Producto inexistente.")
        pregunta_codigo = obtener_entero(
            "\nIngrese código del producto a eliminar. -1 Para salir...", -1, 1000000
        )
        if pregunta_codigo == -1:
                volver_al_menu()
        pos = busqueda_secuencial(PRODUCTOS, pregunta_codigo)

    pregunta_seguridad = obtener_caracter(
        f"\nEsta seguro de eliminar el producto {pregunta_codigo}? Y/N..."
    ).upper()

    if pregunta_seguridad == "Y":

        PRODUCTOS[PRODUCTOS_CODIGO][pos] = -1

        print("Producto eliminado correctamente.")
        print("===================")
    else:
        print("\nBaja de producto cancelada.")
        print("===================")


def modificar_producto():
    print("\n\n==========MODIFICACION DE PRODUCTOS==========")

    pregunta_codigo = obtener_entero("\nIngrese código del producto... -1 Para salir...", -1, 1000000)

    while pregunta_codigo == 0:
        pregunta_codigo = obtener_entero("\nIngrese código del producto... -1 Para salir...", -1, 1000000)
    
    if pregunta_codigo == -1:
        volver_al_menu()

    pos = busqueda_por_codigo(PRODUCTOS, pregunta_codigo)

    if pos == -1:
        print("Producto inexistente.")

    else:
        PRODUCTOS[PRODUCTOS_NOMBRE][pos] = obtener_caracter("Ingrese nuevo nombre... ")

        print("\n1. Alimentos\n2. Limpieza\n3. Bebidas")

        categoria = obtener_caracter("\nIngrese nueva categoría... ")

        PRODUCTOS[PRODUCTOS_CATEGORIA][pos] = categoria

        precio = float(input("Ingrese nuevo precio... "))

        while precio <= 0:
            print("Precio inválido.")
            precio = float(input("Ingrese nuevo precio... "))

        PRODUCTOS[PRODUCTOS_PRECIO][pos] = precio

        stock = obtener_entero("Ingrese nuevo stock: ", 0, 1000000)

        PRODUCTOS[PRODUCTOS_STOCK][pos] = stock

        descuento = float(input("Ingrese nuevo descuento: "))

        while descuento < 0 or descuento > 100:
            descuento = float(input("Descuento inválido. Reingrese: "))

        PRODUCTOS[PRODUCTOS_DESCUENTO][pos] = descuento

        print("Producto modificado correctamente.")
        print("===================")


def listar_productos():

    print("\n\n==========LISTA DE PRODUCTOS==========")
    pregunta_orden = obtener_entero("Elija metodo de ordenamiento. 1.ID  2.ALFABETICAMENTE 3.Buscar por nombre. 4.Buscar por codigo. -1 para salir...", -1, 4)
    if pregunta_orden == -1:
        volver_al_menu()
    if pregunta_orden == 0:
        pregunta_orden = obtener_entero("Elija metodo de ordenamiento. 1.ID  2.ALFABETICAMENTE 3.Buscar por nombre. 4.Buscar por codigo. -1 para salir...", -1, 4)

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
        cuenta_busqueda,busqueda_posiciones = buscar(productos_nombre_individual,pregunta)
        if cuenta_busqueda == 0:
            print("Producto no encontrado...")
            menu_principal()
        else:
            i = 0
            print(f"\nCantidad de productos encontrados...{cuenta_busqueda}\n")
            while i < cuenta_busqueda:
                
                print(f"\n{PRODUCTOS[busqueda_posiciones[i]]}\n")
                i += 1


    if pregunta_orden == 4:
        pregunta = obtener_entero("\nIngrese codigo del producto...",100000,1000000)
        cuenta_busqueda, busqueda_posiciones = buscar(productos_id_individual,pregunta)
        if cuenta_busqueda == 0:
                    print("Producto no encontrado...")
                    menu_principal()
        else:
            i = 0
            while i < cuenta_busqueda:
                print(f"\nProducto encontrado...{cuenta_busqueda}\n")
                print(f"\n{PRODUCTOS[busqueda_posiciones[i]]}\n")
                i += 1
        
    print("===================")
