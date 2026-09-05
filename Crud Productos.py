def alta_producto():
    print("\n\n==========ALTA DE PRODUCTOS==========")

    pregunta_codigo = obtener_entero("\nIngrese código del producto... -1 Para salir...",-1,100000)

    while pregunta_codigo == 0:
            print("Codigo inexistente...")
            pregunta_codigo = obtener_entero("\nIngrese código del producto a eliminar. -1 Para salir...",-1,100000)

    if pregunta_codigo == -1:
                menu_principal()
                print("Volviendo al menu principal...\n\n")

    pos = busqueda_secuencial()

    while pos != -1:
        print("Ya existe un producto con ese código.")

        pregunta_codigo = obtener_entero("\nIngrese código del producto... -1 Para salir...",-1,100000)
        
        pos = busqueda_secuencial()

    else:
        pregunta_nombre = obtener_caracter("\nIngrese nombre del producto... ").upper()

        print("\n1. Alimentos\n2. Limpieza\n3. Bebidas")
       
        categoria = obtener_entero("Ingrese categoría... ",1,3)

        precio = float(input("Ingrese precio... "))

        while precio <= 0:
            precio = float(input("Precio inválido. Reingrese... "))

        stock = obtener_entero("Ingrese stock... ",0,100000)

        descuento = float(input("Ingrese descuento: "))

        while descuento < 0 or descuento > 100:
            descuento = float(input("Descuento inválido. Reingrese: "))

        IDS_PRODUCTOS.append(pregunta_codigo)
        PRODUCTOS.append(pregunta_nombre)
        CATEGORIA.append(categoria)
        PRECIOS.append(precio)
        STOCK.append(stock)
        DESCUENTO.append(descuento)

        print("\n\nProducto agregado correctamente.\n\n")
        print('===================')


def baja_producto():

    print("\n\n==========BAJA DE PRODUCTOS==========")

    pregunta_codigo = obtener_entero("\n\nIngrese código del producto a eliminar. -1 Para salir...",-1,100000)

    

    while pregunta_codigo == 0:
        print("Codigo inexistente...")
        pregunta_codigo = obtener_entero("\nIngrese código del producto a eliminar. -1 Para salir...",-1,100000)

    if pregunta_codigo == -1:
                    menu_principal()
                    print("Volviendo al menu principal...\n\n")

    pos = busqueda_secuencial(IDS_PRODUCTOS, pregunta_codigo)

    if pos == -1:
        print("Producto inexistente.")

    pregunta_seguridad = obtener_caracter(f"\nEsta seguro de eliminar el producto{pregunta_codigo}? Y/N").upper()

    if pregunta_seguridad == "Y":
        
        IDS_PRODUCTOS[pos] = -1
        PRODUCTOS[pos] = -1
        CATEGORIA[pos] = -1
        PRECIOS[pos] = -1
        STOCK[pos] = -1
        DESCUENTO[pos] = -1

        print("Producto eliminado correctamente.")
        print('===================')
    else:
        print("\nBaja de producto cancelada.")
        print('===================')
        


def modificar_producto():
    print("\n\n==========MODIFICACION DE PRODUCTOS==========")

    pregunta_codigo = obtener_entero("\nIngrese código del producto... -1 Para salir...",-1,100000)

    while pregunta_codigo == 0:
            print("Codigo inexistente...")
            pregunta_codigo = obtener_entero("\nIngrese código del producto... -1 Para salir...",-1,10000)

    if pregunta_codigo == -1:
                menu_principal()
                print("Volviendo al menu principal...\n\n")


    pos = busqueda_secuencial(IDS_PRODUCTOS, pregunta_codigo)

    if pos == -1:
        print("Producto inexistente.")

    else:
        PRODUCTOS[pos] = input("Ingrese nuevo nombre... ").upper()

        print("\n1. Alimentos\n2. Limpieza\n3. Bebidas")

        categoria = obtener_caracter("\nIngrese nueva categoría... ")

        CATEGORIA[pos] = categoria

        precio = float(input("Ingrese nuevo precio... "))

        while precio <= 0:
            print("Precio inválido.")
            precio = float(input("Ingrese nuevo precio... "))

        PRECIOS[pos] = precio

        stock = obtener_entero("Ingrese nuevo stock: ",0,1000000)

        STOCK[pos] = stock

        descuento = float(input("Ingrese nuevo descuento: "))

        while descuento < 0 or descuento > 100:
            descuento = float(input("Descuento inválido. Reingrese: "))

        DESCUENTO[pos] = descuento

        print("Producto modificado correctamente.")
        print('===================')


def listar_productos():

    print("\n\n==========LISTA DE PRODUCTOS==========")
    pregunta_orden = obtener_entero("Elija metodo de ordenamiento. 1.ID  2.ALFABETICAMENTE",1,2)
    if pregunta_orden == 1:
         pass
    else:
         pass

    for i in range(len(IDS_PRODUCTOS)):

        if IDS_PRODUCTOS[i] != -1:

            print(f"Código:{IDS_PRODUCTOS[i]} Nombre: {PRODUCTOS[i]} Precio: {PRECIOS[i]} Stock: {STOCK[i]} Descuento: {DESCUENTO[i]} %")

            if CATEGORIA[i] == 1:
                print("Categoría: Alimentos")
            elif CATEGORIA[i] == 2:
                print("Categoría: Limpieza")
            else:
                print("Categoría: Bebidas")
    print('===================')

def clientes():
    print("==========\nCLIENTES\n==========")

def ventas():
    print("==========\nVENTAS\n==========")