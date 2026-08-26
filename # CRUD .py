# CRUD PRODUCTOS


def alta_producto(IDS, PRODUCTOS, CATEGORIA, PRECIOS, STOCK, descuentos_productos):
    print("\n\n==========ALTA DE PRODUCTOS==========")

    pregunta_codigo = obtener_entero("\nIngrese código del producto... -1 Para salir...",-1,100000)

    while pregunta_codigo == 0:
            print("Codigo inexistente...")
            pregunta_codigo = obtener_entero("\nIngrese código del producto a eliminar. -1 Para salir...",-1,100000)

    if pregunta_codigo == -1:
                menu_principal()
                print("Volviendo al menu principal...\n\n")

    pos = busqueda_secuencial(IDS, pregunta_codigo)

    while pos != -1:
        print("Ya existe un producto con ese código.")

        pregunta_codigo = obtener_entero("\nIngrese código del producto... -1 Para salir...",-1,100000)
        
        pos = busqueda_secuencial(IDS, pregunta_codigo)

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

        IDS.append(pregunta_codigo)
        PRODUCTOS.append(pregunta_nombre)
        CATEGORIA.append(categoria)
        PRECIOS.append(precio)
        STOCK.append(stock)
        descuentos_productos.append(descuento)

        print("\n\nProducto agregado correctamente.\n\n")
        print('===================')


def baja_producto(IDS, PRODUCTOS, CATEGORIA, PRECIOS, STOCK, descuentos_productos):

    print("\n\n==========BAJA DE PRODUCTOS==========")

    pregunta_codigo = obtener_entero("\n\nIngrese código del producto a eliminar. -1 Para salir...",-1,100000)

    

    while pregunta_codigo == 0:
        print("Codigo inexistente...")
        pregunta_codigo = obtener_entero("\nIngrese código del producto a eliminar. -1 Para salir...",-1,100000)

    if pregunta_codigo == -1:
                    menu_principal()
                    print("Volviendo al menu principal...\n\n")

    pos = busqueda_secuencial(IDS, pregunta_codigo)

    if pos == -1:
        print("Producto inexistente.")

    pregunta_seguridad = obtener_caracter(f"\nEsta seguro de eliminar el producto{pregunta_codigo}? Y/N").upper()

    if pregunta_seguridad == "Y":
        
        IDS[pos] = -1
        PRODUCTOS[pos] = -1
        CATEGORIA[pos] = -1
        PRECIOS[pos] = -1
        STOCK[pos] = -1
        descuentos_productos[pos] = -1

        print("Producto eliminado correctamente.")
        print('===================')
    else:
        print("\nBaja de producto cancelada.")
        print('===================')
        


def modificar_producto(IDS, PRODUCTOS, CATEGORIA, PRECIOS, STOCK, descuentos_productos):
    print("\n\n==========MODIFICACION DE PRODUCTOS==========")

    pregunta_codigo = obtener_entero("\nIngrese código del producto... -1 Para salir...",-1,100000)

    while pregunta_codigo == 0:
            print("Codigo inexistente...")
            pregunta_codigo = obtener_entero("\nIngrese código del producto... -1 Para salir...",-1,10000)

    if pregunta_codigo == -1:
                menu_principal()
                print("Volviendo al menu principal...\n\n")


    pos = busqueda_secuencial(IDS, pregunta_codigo)

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

        descuentos_productos[pos] = descuento

        print("Producto modificado correctamente.")
        print('===================')


def listar_productos(IDS, PRODUCTOS, CATEGORIA, PRECIOS, STOCK, descuentos_productos):

    print("\n\n==========LISTA DE PRODUCTOS==========")

    for i in range(len(IDS)):

        if IDS[i] != -1:

            print(f"Código:{IDS[i]} Nombre: {PRODUCTOS[i]}")

            if CATEGORIA[i] == 1:
                print("Categoría: Alimentos")
            elif CATEGORIA[i] == 2:
                print("Categoría: Limpieza")
            else:
                print("Categoría: Bebidas")

            print(f"Precio: {PRECIOS[i]} Stock: {STOCK[i]} Descuento: {descuentos_productos[i]} %")
    print('===================')









# CRUD CLIENTES 

def buscar_cliente(cod_clientes, pregunta_codigo):
    pos = -1
    i = 0

    while i < len(cod_clientes) and pos == -1:
        if cod_clientes[i] == pregunta_codigo:
            pos = i
        i = i + 1

    return pos


def alta_cliente(cod_clientes, nom_clientes, tipos_clientes):

    pregunta_codigo = int(input("Ingrese código del cliente: "))

    pos = buscar_cliente(cod_clientes, pregunta_codigo)

    if pos != -1:
        print("Ya existe un cliente con ese código.")

    else:
        pregunta_nombre = input("Ingrese nombre del cliente: ")

        print("1. Frecuente")
        print("2. Mayorista")
        print("3. Ocasional")

        tipo = int(input("Ingrese tipo de cliente: "))

        while tipo < 1 or tipo > 3:
            tipo = int(input("Tipo inválido. Reingrese: "))

        cod_clientes.append(pregunta_codigo)
        nom_clientes.append(pregunta_nombre)
        tipos_clientes.append(tipo)

        print("Cliente agregado correctamente.")


def baja_cliente(cod_clientes, nom_clientes, tipos_clientes):

    pregunta_codigo = int(input("Ingrese código del cliente a eliminar: "))

    pos = buscar_cliente(cod_clientes, pregunta_codigo)

    if pos == -1:
        print("Cliente inexistente.")

    else:
        cod_clientes[pos] = -1
        nom_clientes[pos] = -1
        tipos_clientes[pos] = -1

        print("Cliente eliminado correctamente.")


def modificar_cliente(cod_clientes, nom_clientes, tipos_clientes):

    pregunta_codigo = int(input("Ingrese código del cliente a modificar: "))

    pos = buscar_cliente(cod_clientes, pregunta_codigo)

    if pos == -1:
        print("Cliente inexistente.")

    else:
        nom_clientes[pos] = input("Ingrese nuevo nombre: ")

        print("1. Frecuente")
        print("2. Mayorista")
        print("3. Ocasional")

        tipo = int(input("Ingrese nuevo tipo: "))

        while tipo < 1 or tipo > 3:
            tipo = int(input("Tipo inválido. Reingrese: "))

        tipos_clientes[pos] = tipo

        print("Cliente modificado correctamente.")


def listar_clientes(cod_clientes, nom_clientes, tipos_clientes):

    print("----- CLIENTES -----")

    for i in range(len(cod_clientes)):

        if cod_clientes[i] != -1:

            print("Código:", cod_clientes[i])
            print("Nombre:", nom_clientes[i])

            if tipos_clientes[i] == 1:
                print("Tipo: Frecuente")
            elif tipos_clientes[i] == 2:
                print("Tipo: Mayorista")
            else:
                print("Tipo: Ocasional")

            print("--------------------")









#   CRUD VENTAS 

def buscar_venta(cod_ventas, pregunta_codigo):
    pos = -1
    i = 0

    while i < len(cod_ventas) and pos == -1:
        if cod_ventas[i] == pregunta_codigo:
            pos = i
        i = i + 1

    return pos


def alta_venta(cod_ventas, clientes_ventas, productos_ventas, cantidades_ventas, fechas_ventas, cod_clientes, IDS, STOCK):

    pregunta_codigo = int(input("Ingrese código de venta: "))

    pos = buscar_venta(cod_ventas, pregunta_codigo)

    if pos != -1:
        print("Ya existe una venta con ese código.")

    else:
        cod_cliente = int(input("Ingrese código del cliente: "))

        pos_cliente = buscar_cliente(cod_clientes, cod_cliente)

        if pos_cliente == -1:
            print("Cliente inexistente.")

        else:
            cod_producto = int(input("Ingrese código del producto: "))

            pos_producto = busqueda_secuencial(IDS, cod_producto)

            if pos_producto == -1:
                print("Producto inexistente.")

            else:
                cantidad = int(input("Ingrese cantidad: "))

                while cantidad <= 0:
                    cantidad = int(input("Cantidad inválida. Reingrese: "))

                if cantidad > STOCK[pos_producto]:
                    print("Stock insuficiente.")

                else:
                    fecha = input("Ingrese fecha de venta: ")

                    cod_ventas.append(pregunta_codigo)
                    clientes_ventas.append(cod_cliente)
                    productos_ventas.append(cod_producto)
                    cantidades_ventas.append(cantidad)
                    fechas_ventas.append(fecha)

                    STOCK[pos_producto] = STOCK[pos_producto] - cantidad

                    print("Venta registrada correctamente.")


def baja_venta(cod_ventas, clientes_ventas, productos_ventas, cantidades_ventas, fechas_ventas):

    pregunta_codigo = int(input("Ingrese código de venta a eliminar: "))

    pos = buscar_venta(cod_ventas, pregunta_codigo)

    if pos == -1:
        print("Venta inexistente.")

    else:
        cod_ventas[pos] = -1
        clientes_ventas[pos] = -1
        productos_ventas[pos] = -1
        cantidades_ventas[pos] = -1
        fechas_ventas[pos] = -1

        print("Venta eliminada correctamente.")


def modificar_venta(cod_ventas, clientes_ventas, productos_ventas, cantidades_ventas, fechas_ventas, cod_clientes, IDS):

    pregunta_codigo = int(input("Ingrese código de venta a modificar: "))

    pos = buscar_venta(cod_ventas, pregunta_codigo)

    if pos == -1:
        print("Venta inexistente.")

    else:
        cod_cliente = int(input("Ingrese nuevo código de cliente: "))

        pos_cliente = buscar_cliente(cod_clientes, cod_cliente)

        if pos_cliente == -1:
            print("Cliente inexistente.")

        else:
            cod_producto = int(input("Ingrese nuevo código de producto: "))

            pos_producto = busqueda_secuencial(IDS, cod_producto)

            if pos_producto == -1:
                print("Producto inexistente.")

            else:
                cantidad = int(input("Ingrese nueva cantidad: "))

                while cantidad <= 0:
                    cantidad = int(input("Cantidad inválida. Reingrese: "))

                fecha = input("Ingrese nueva fecha: ")

                clientes_ventas[pos] = cod_cliente
                productos_ventas[pos] = cod_producto
                cantidades_ventas[pos] = cantidad
                fechas_ventas[pos] = fecha

                print("Venta modificada correctamente.")


def listar_ventas(cod_ventas, clientes_ventas, productos_ventas, cantidades_ventas, fechas_ventas):

    print("----- VENTAS -----")

    for i in range(len(cod_ventas)):

        if cod_ventas[i] != -1:

            print("Código venta:", cod_ventas[i])
            print("Cliente:", clientes_ventas[i])
            print("Producto:", productos_ventas[i])
            print("Cantidad:", cantidades_ventas[i])
            print("Fecha:", fechas_ventas[i])
            print("--------------------")









            def menu_productos(IDS, PRODUCTOS, CATEGORIA, PRECIOS, STOCK, descuentos_productos, rol):

    opcion = 0

    while opcion != 5:

        print("----- PRODUCTOS -----")
        print("1. Alta")
        print("2. Baja")
        print("3. Modificar")
        print("4. Listar")
        print("5. Volver")

        opcion = int(input("Opción: "))

        if opcion == 1:

            if rol == "ADMIN":
                alta_producto(IDS, PRODUCTOS, CATEGORIA, PRECIOS, STOCK, descuentos_productos)
            else:
                print("No tiene permisos.")

        elif opcion == 2:

            if rol == "ADMIN":
                baja_producto(IDS, PRODUCTOS, CATEGORIA, PRECIOS, STOCK, descuentos_productos)
            else:
                print("No tiene permisos.")

        elif opcion == 3:

            if rol == "ADMIN":
                modificar_producto(IDS, PRODUCTOS, CATEGORIA, PRECIOS, STOCK, descuentos_productos)
            else:
                print("No tiene permisos.")

        elif opcion == 4:

            listar_productos(IDS, PRODUCTOS, CATEGORIA, PRECIOS, STOCK, descuentos_productos)