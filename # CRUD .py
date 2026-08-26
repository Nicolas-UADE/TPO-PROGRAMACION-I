# CRUD PRODUCTOS

def buscar_producto(cod_productos, codigo):
    pos = -1
    i = 0

    while i < len(cod_productos) and pos == -1:
        if cod_productos[i] == codigo:
            pos = i
        i = i+1

    return pos


def alta_producto(cod_productos, nom_productos, categorias_productos, precios_productos, stock_productos, descuentos_productos):

    codigo = int(input("Ingrese código del producto: "))

    pos = buscar_producto(cod_productos, codigo)

    if pos != -1:
        print("Ya existe un producto con ese código.")

    else:
        nombre = input("Ingrese nombre del producto: ")

        print("1. Alimentos")
        print("2. Limpieza")
        print("3. Bebidas")
        categoria = int(input("Ingrese categoría: "))

        while categoria < 1 or categoria > 3:
            categoria = int(input("Categoría inválida. Reingrese: "))

        precio = float(input("Ingrese precio: "))

        while precio <= 0:
            precio = float(input("Precio inválido. Reingrese: "))

        stock = int(input("Ingrese stock: "))

        while stock < 0:
            stock = int(input("Stock inválido. Reingrese: "))

        descuento = float(input("Ingrese descuento: "))

        while descuento < 0 or descuento > 100:
            descuento = float(input("Descuento inválido. Reingrese: "))

        cod_productos.append(codigo)
        nom_productos.append(nombre)
        categorias_productos.append(categoria)
        precios_productos.append(precio)
        stock_productos.append(stock)
        descuentos_productos.append(descuento)

        print("Producto agregado correctamente.")


def baja_producto(cod_productos, nom_productos, categorias_productos, precios_productos, stock_productos, descuentos_productos):

    codigo = int(input("Ingrese código del producto a eliminar: "))

    pos = buscar_producto(cod_productos, codigo)

    if pos == -1:
        print("Producto inexistente.")

    else:
        cod_productos[pos] = -1
        nom_productos[pos] = -1
        categorias_productos[pos] = -1
        precios_productos[pos] = -1
        stock_productos[pos] = -1
        descuentos_productos[pos] = -1

        print("Producto eliminado correctamente.")


def modificar_producto(cod_productos, nom_productos, categorias_productos, precios_productos, stock_productos, descuentos_productos):

    codigo = int(input("Ingrese código del producto a modificar: "))

    pos = buscar_producto(cod_productos, codigo)

    if pos == -1:
        print("Producto inexistente.")

    else:
        nom_productos[pos] = input("Ingrese nuevo nombre: ")

        print("1. Alimentos")
        print("2. Limpieza")
        print("3. Bebidas")

        categoria = int(input("Ingrese nueva categoría: "))

        while categoria < 1 or categoria > 3:
            categoria = int(input("Categoría inválida. Reingrese: "))

        categorias_productos[pos] = categoria

        precio = float(input("Ingrese nuevo precio: "))

        while precio <= 0:
            precio = float(input("Precio inválido. Reingrese: "))

        precios_productos[pos] = precio

        stock = int(input("Ingrese nuevo stock: "))

        while stock < 0:
            stock = int(input("Stock inválido. Reingrese: "))

        stock_productos[pos] = stock

        descuento = float(input("Ingrese nuevo descuento: "))

        while descuento < 0 or descuento > 100:
            descuento = float(input("Descuento inválido. Reingrese: "))

        descuentos_productos[pos] = descuento

        print("Producto modificado correctamente.")


def listar_productos(cod_productos, nom_productos, categorias_productos, precios_productos, stock_productos, descuentos_productos):

    print("----- PRODUCTOS -----")

    for i in range(len(cod_productos)):

        if cod_productos[i] != -1:

            print("Código:", cod_productos[i])
            print("Nombre:", nom_productos[i])

            if categorias_productos[i] == 1:
                print("Categoría: Alimentos")
            elif categorias_productos[i] == 2:
                print("Categoría: Limpieza")
            else:
                print("Categoría: Bebidas")

            print("Precio:", precios_productos[i])
            print("Stock:", stock_productos[i])
            print("Descuento:", descuentos_productos[i], "%")
            print("--------------------")









# CRUD CLIENTES 

def buscar_cliente(cod_clientes, codigo):
    pos = -1
    i = 0

    while i < len(cod_clientes) and pos == -1:
        if cod_clientes[i] == codigo:
            pos = i
        i = i + 1

    return pos


def alta_cliente(cod_clientes, nom_clientes, tipos_clientes):

    codigo = int(input("Ingrese código del cliente: "))

    pos = buscar_cliente(cod_clientes, codigo)

    if pos != -1:
        print("Ya existe un cliente con ese código.")

    else:
        nombre = input("Ingrese nombre del cliente: ")

        print("1. Frecuente")
        print("2. Mayorista")
        print("3. Ocasional")

        tipo = int(input("Ingrese tipo de cliente: "))

        while tipo < 1 or tipo > 3:
            tipo = int(input("Tipo inválido. Reingrese: "))

        cod_clientes.append(codigo)
        nom_clientes.append(nombre)
        tipos_clientes.append(tipo)

        print("Cliente agregado correctamente.")


def baja_cliente(cod_clientes, nom_clientes, tipos_clientes):

    codigo = int(input("Ingrese código del cliente a eliminar: "))

    pos = buscar_cliente(cod_clientes, codigo)

    if pos == -1:
        print("Cliente inexistente.")

    else:
        cod_clientes[pos] = -1
        nom_clientes[pos] = -1
        tipos_clientes[pos] = -1

        print("Cliente eliminado correctamente.")


def modificar_cliente(cod_clientes, nom_clientes, tipos_clientes):

    codigo = int(input("Ingrese código del cliente a modificar: "))

    pos = buscar_cliente(cod_clientes, codigo)

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

def buscar_venta(cod_ventas, codigo):
    pos = -1
    i = 0

    while i < len(cod_ventas) and pos == -1:
        if cod_ventas[i] == codigo:
            pos = i
        i = i + 1

    return pos


def alta_venta(cod_ventas, clientes_ventas, productos_ventas, cantidades_ventas, fechas_ventas, cod_clientes, cod_productos, stock_productos):

    codigo = int(input("Ingrese código de venta: "))

    pos = buscar_venta(cod_ventas, codigo)

    if pos != -1:
        print("Ya existe una venta con ese código.")

    else:
        cod_cliente = int(input("Ingrese código del cliente: "))

        pos_cliente = buscar_cliente(cod_clientes, cod_cliente)

        if pos_cliente == -1:
            print("Cliente inexistente.")

        else:
            cod_producto = int(input("Ingrese código del producto: "))

            pos_producto = buscar_producto(cod_productos, cod_producto)

            if pos_producto == -1:
                print("Producto inexistente.")

            else:
                cantidad = int(input("Ingrese cantidad: "))

                while cantidad <= 0:
                    cantidad = int(input("Cantidad inválida. Reingrese: "))

                if cantidad > stock_productos[pos_producto]:
                    print("Stock insuficiente.")

                else:
                    fecha = input("Ingrese fecha de venta: ")

                    cod_ventas.append(codigo)
                    clientes_ventas.append(cod_cliente)
                    productos_ventas.append(cod_producto)
                    cantidades_ventas.append(cantidad)
                    fechas_ventas.append(fecha)

                    stock_productos[pos_producto] = stock_productos[pos_producto] - cantidad

                    print("Venta registrada correctamente.")


def baja_venta(cod_ventas, clientes_ventas, productos_ventas, cantidades_ventas, fechas_ventas):

    codigo = int(input("Ingrese código de venta a eliminar: "))

    pos = buscar_venta(cod_ventas, codigo)

    if pos == -1:
        print("Venta inexistente.")

    else:
        cod_ventas[pos] = -1
        clientes_ventas[pos] = -1
        productos_ventas[pos] = -1
        cantidades_ventas[pos] = -1
        fechas_ventas[pos] = -1

        print("Venta eliminada correctamente.")


def modificar_venta(cod_ventas, clientes_ventas, productos_ventas, cantidades_ventas, fechas_ventas, cod_clientes, cod_productos):

    codigo = int(input("Ingrese código de venta a modificar: "))

    pos = buscar_venta(cod_ventas, codigo)

    if pos == -1:
        print("Venta inexistente.")

    else:
        cod_cliente = int(input("Ingrese nuevo código de cliente: "))

        pos_cliente = buscar_cliente(cod_clientes, cod_cliente)

        if pos_cliente == -1:
            print("Cliente inexistente.")

        else:
            cod_producto = int(input("Ingrese nuevo código de producto: "))

            pos_producto = buscar_producto(cod_productos, cod_producto)

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









            def menu_productos(cod_productos, nom_productos, categorias_productos, precios_productos, stock_productos, descuentos_productos, rol):

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
                alta_producto(cod_productos, nom_productos, categorias_productos, precios_productos, stock_productos, descuentos_productos)
            else:
                print("No tiene permisos.")

        elif opcion == 2:

            if rol == "ADMIN":
                baja_producto(cod_productos, nom_productos, categorias_productos, precios_productos, stock_productos, descuentos_productos)
            else:
                print("No tiene permisos.")

        elif opcion == 3:

            if rol == "ADMIN":
                modificar_producto(cod_productos, nom_productos, categorias_productos, precios_productos, stock_productos, descuentos_productos)
            else:
                print("No tiene permisos.")

        elif opcion == 4:

            listar_productos(cod_productos, nom_productos, categorias_productos, precios_productos, stock_productos, descuentos_productos)