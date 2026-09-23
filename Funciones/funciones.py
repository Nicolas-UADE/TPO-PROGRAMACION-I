import random
import re
from listas import (
    PRODUCTOS_CODIGO,
    PRODUCTOS_NOMBRE,
    PRODUCTOS_CATEGORIA,
    PRODUCTOS_PRECIO,
    USUARIOS_ADMIN,
    USUARIOS_LECTORES,
    productos_nombre_individual,
    lista_clientes,
)
from listas import (
    PRODUCTOS_STOCK,
    PRODUCTOS,
    PRODUCTOS_DESCUENTO,
    ELIMINADO,
    USUARIOS_ADMIN,
    CONTRASENIAS_ADMIN,
    CONTRASENIAS_LECTORES,
    VENTAS_ID,
    VENTAS_CLIENTE,
    VENTAS_IMPORTE,
    VENTAS_CANTIDAD,
    VENTAS,
    VENTAS_CATEGORIA,
    VENTAS_FECHA,
    VENTAS_PRECIO_UNITARIO,
    VENTAS_PRODUCTO,
    productos_id_individual,
)
from functools import reduce


def generador_de_id(lista):
    """Genera un numero random de 6 cifras que no se repita con los que ya existen en la lista."""
    nuevo_id = random.randint(100000, 999999)

    while nuevo_id in lista:
        nuevo_id = random.randint(100000, 999999)

    return nuevo_id


def generar_id_venta(matriz_ventas):
    """Junta los ids de ventas que no fueron eliminadas y genera uno nuevo que no se repita."""
    ids_ventas = []

    for venta in matriz_ventas:
        if venta[VENTAS_ID] != ELIMINADO:
            ids_ventas.append(venta[VENTAS_ID])

    return generador_de_id(ids_ventas)


def buscar_venta(matriz_ventas, id_venta):
    """Devuelve todas las posiciones donde aparece ese id de venta."""
    posiciones = []

    for posicion in range(len(matriz_ventas)):
        if matriz_ventas[posicion][VENTAS_ID] == id_venta:
            posiciones.append(posicion)

    return posiciones


def pedir_fecha():
    """Pide una fecha por teclado y no avanza hasta que tenga el formato DD/MM/AAAA y sea coherente."""
    patron_fecha = r"^[0-9]{2}/[0-9]{2}/[0-9]{4}$"
    fecha_valida = False

    while fecha_valida == False:
        fecha = input("Ingrese fecha DD/MM/AAAA\n.").strip()

        if re.match(patron_fecha, fecha) != None:
            partes_fecha = fecha.split("/")
            dia = int(partes_fecha[0])
            mes = int(partes_fecha[1])
            anio = int(partes_fecha[2])

            # Chequea que el dia, mes y anio tengan valores logicos.
            if dia >= 1 and dia <= 31 and mes >= 1 and mes <= 12 and anio >= 2000:
                fecha_valida = True

        if fecha_valida == False:
            print("\nFecha invalida. Use el formato DD/MM/AAAA.\n")

    return fecha


def validar_email(email):
    """Chequea que el email tenga formato valido y termine en uno de los dominios permitidos."""
    patron_email = r"^[a-zA-Z0-9._-]+@(gmail|hotmail|outlook|yahoo)\.com$"
    return re.match(patron_email, email) != None


def recortar_texto(texto, ancho_maximo):
    """Corta un texto largo y le agrega "..." al final para que no rompa el formato de las tablas."""
    texto = str(texto).strip()

    if len(texto) > ancho_maximo:
        texto = texto[: ancho_maximo - 3] + "..."

    return texto


def positivo(valor):
    """Chequea que un numero sea mayor a cero."""
    return valor > 0


def productos_activos():
    """Devuelve solo los productos que no fueron eliminados, en formato de lista de listas."""
    activos = []
    for i in PRODUCTOS:
        if i[PRODUCTOS_CODIGO] != ELIMINADO:
            activos.append(
                [
                    i[PRODUCTOS_CODIGO],
                    i[PRODUCTOS_NOMBRE],
                    i[PRODUCTOS_CATEGORIA],
                    i[PRODUCTOS_PRECIO],
                    i[PRODUCTOS_STOCK],
                    i[PRODUCTOS_DESCUENTO],
                ]
            )
    return activos


def productos_nombres_activos():
    """Devuelve solo los nombres de productos que no fueron eliminados."""
    activos = []
    for i in productos_nombre_individual:
        if i != ELIMINADO:
            activos.append(i)
    return activos


def inicio(texto):
    """Imprime un titulo centrado, sin color (para menus generales)."""
    print(texto.center(118, "-"))


def inicio_alta(texto):
    """Titulo centrado en verde, para pantallas de alta."""
    linea = texto.center(118, "-")
    print(f"\033[32m{linea}\033[0m")


def inicio_baja(texto):
    """Titulo centrado en rojo, para pantallas de baja."""
    linea = texto.center(118, "-")
    print(f"\033[31m{linea}\033[0m")


def inicio_modificar(texto):
    """Titulo centrado en azul, para pantallas de modificacion."""
    linea = texto.center(118, "-")
    print(f"\033[34m{linea}\033[0m")


def inicio_listado(texto):
    """Titulo centrado en celeste, para pantallas de listado."""
    linea = texto.center(118, "-")
    print(f"\033[36m{linea}\033[0m")


def rango(inicio, hasta, valor):
    """Chequea que un valor este dentro de un rango (inclusive)."""
    return inicio <= valor and hasta >= valor


def redondeo(numero):
    """Le da formato de moneda a un numero, con separador de miles y 2 decimales."""
    return f"$ {numero:,.2f}"


def calcular_descuentos(PRECIOS):
    """Calcula el precio final de cada producto aplicandole su descuento correspondiente."""
    precios_finales = []

    for PRODUCTO in PRECIOS:
        precio = PRODUCTO[PRODUCTOS_PRECIO]
        descuento = PRODUCTO[PRODUCTOS_DESCUENTO]
        precio_con_descuento = precio * (1 - descuento / 100)
        precios_finales.append(redondeo(precio_con_descuento))
    return precios_finales


def coincidencia(pregunta_usu, pregunta_code):
    """Verifica el usuario y contraseña ingresados contra las listas de admin y lector."""
    ADMIN = False
    LECTOR = False
    es_admin_usuario = busqueda_secuencial(USUARIOS_ADMIN, pregunta_usu)

    es_admin_contrasenia = busqueda_secuencial(CONTRASENIAS_ADMIN, pregunta_code)

    es_lector_usuario = busqueda_secuencial(USUARIOS_LECTORES, pregunta_usu)

    es_lector_contrasenia = busqueda_secuencial(CONTRASENIAS_LECTORES, pregunta_code)

    # Si el usuario y la contraseña estan en la misma posicion de las listas de admin, es admin.
    if (
        es_admin_usuario == es_admin_contrasenia
        and es_admin_usuario != -1
        and es_admin_contrasenia != -1
    ):
        ADMIN = True
    # Si no es admin, se chequea lo mismo pero contra las listas de lector.
    elif (
        es_lector_usuario == es_lector_contrasenia
        and es_lector_usuario != -1
        and es_lector_contrasenia != -1
    ):
        LECTOR = True
    return ADMIN, LECTOR


def obtener_caracter(texto):
    """Pide un texto por teclado y no deja continuar si el campo queda vacio."""
    ask = input(texto).strip().upper()
    while len(ask) == 0:
        print("Debe ingresar un valor.")
        ask = input(texto).strip().upper()

    return ask


def obtener_respuesta(texto):
    """Pide una respuesta y solo acepta Y o N."""
    respuesta = obtener_caracter(texto)

    while respuesta != "Y" and respuesta != "N":
        print("Ingrese Y para confirmar o N para cancelar.")
        respuesta = obtener_caracter(texto)

    return respuesta


def buscar(lista, elemento):
    """Busca todas las apariciones de un elemento en una lista y devuelve cuantas veces aparece y en donde."""
    lista_origen = []
    lista_origen.extend(lista)
    contador = 0
    posiciones = []
    while elemento in lista_origen:
        posicion = lista_origen.index(elemento)
        posiciones.append(posicion)

        lista_origen[posicion] = 0
        contador += 1

    return contador, posiciones


def buscar_por_id(lista, id_buscado):
    """Busca un cliente por id, salteando los que fueron eliminados. Devuelve -2 si no lo encuentra."""
    for i in range(len(lista)):
        cliente = lista[i]
        if cliente != ELIMINADO:
            if cliente["id"] == id_buscado:
                return i
    return -2


def buscar_por_nombre(lista, nombre):
    """Busca un cliente por nombre, salteando los que fueron eliminados. Devuelve -2 si no lo encuentra."""
    for i in range(len(lista)):
        cliente = lista[i]
        if cliente != ELIMINADO:
            if cliente["nombre"] == nombre:
                return i
    return -2


def obtener_entero(texto, minimo, maximo):
    """Pide un numero entero por teclado, valida que sea numero y que este dentro del rango permitido."""
    valor_invalido = True
    while valor_invalido == True:
        valor_str = input(texto).strip()

        es_entero = valor_str.isdigit()

        # Contempla el caso de numeros negativos (el signo "-" no lo detecta isdigit()).
        if valor_str.startswith("-") and len(valor_str) > 1:
            es_entero = valor_str[1:].isdigit()

        if es_entero == False:
            print("Debe ingresar un numero entero.")
        else:
            valor = int(valor_str)

            if not rango(minimo, maximo, valor):
                print("Valor no valido.")
            else:
                valor_invalido = False
    return valor


def busqueda_secuencial(lista, parametro):
    """Recorre la lista elemento por elemento hasta encontrar el parametro. Devuelve -1 si no esta."""
    i = 0
    while i < len(lista) and lista[i] != parametro:
        i += 1
    if i < len(lista):
        return i
    else:
        return -1


def busqueda_por_codigo(lista, codigo):
    """Igual que busqueda_secuencial pero para productos, comparando por su codigo."""
    i = 0
    while i < len(lista) and lista[i][PRODUCTOS_CODIGO] != codigo:
        i += 1
    if i < len(lista):
        return i
    else:
        return -1


def ordenar_por_codigo():
    """Imprime la tabla de productos activos ordenada por codigo."""
    ordenados_codigo = sorted(
        productos_activos(), key=lambda fila: fila[PRODUCTOS_CODIGO]
    )
    ancho = 118
    print("-" * ancho)
    for i in ordenados_codigo:
        descuento = f"{i[PRODUCTOS_DESCUENTO]}%"
        print(
            f"|{i[PRODUCTOS_CODIGO]:<15} | {i[PRODUCTOS_NOMBRE]:<15} | {i[PRODUCTOS_CATEGORIA]:<15} | {redondeo(i[PRODUCTOS_PRECIO]):<15} | {i[PRODUCTOS_STOCK]:<15} | {descuento:<15}"
        )
    print("-" * ancho)


def ordenar_alfabeticamente():
    """Imprime la tabla de productos activos ordenada alfabeticamente por nombre."""
    ordenados_codigo = sorted(
        productos_activos(), key=lambda fila: fila[PRODUCTOS_NOMBRE]
    )
    ancho = 118
    print("-" * ancho)
    for i in ordenados_codigo:
        descuento = f"{i[PRODUCTOS_DESCUENTO]}%"
        print(
            f"|{i[PRODUCTOS_CODIGO]:<15} | {i[PRODUCTOS_NOMBRE]:<15} | {i[PRODUCTOS_CATEGORIA]:<15} | {redondeo(i[PRODUCTOS_PRECIO]):<15} | {i[PRODUCTOS_STOCK]:<15} | {descuento:<15}"
        )
    print("-" * ancho)


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


def lista_cabeza_clientes():
    """Imprime el encabezado de la tabla de clientes (los titulos de cada columna)."""
    list = []
    codigo = "ID"
    nombre = "Nombre"
    dni = "DNI"
    telefono = "TELEFONO"
    email = "EMAIL"

    list.append(codigo), list.append(nombre), list.append(dni), list.append(
        telefono
    ), list.append(email)
    ancho = 120
    print("-" * ancho)
    print(
        f"|{list[0]:<20} | {list[1]:<20} | {list[2]:<20} | {list[3]:<20} | {list[4]:<20}"
    )

    print("-" * ancho)


def consultar_cliente_y_ventas():
    """Muestra los datos de un cliente y todas las ventas que realizo."""
    id_cliente = pedir_cliente("Ingrese ID del cliente. -1 Para salir\n.")

    if id_cliente == -1:
        return

    posicion_cliente = buscar_por_id(
        lista_clientes,
        id_cliente,
    )
    cliente = lista_clientes[posicion_cliente]

    # Muestra los datos personales del cliente.
    print("\nDATOS DEL CLIENTE")
    print("-" * 30)
    print(f"ID: {cliente['id']}")
    print(f"Nombre: {cliente['nombre']}")
    print(f"DNI: {cliente['dni']}")
    print(f"Telefono: {cliente['telefono']}")
    print(f"Email: {cliente['email']}")

    # Junta todas las ventas activas de ese cliente y suma el total gastado.
    ventas_cliente = []
    total_comprado = 0

    for venta in VENTAS:
        if venta[VENTAS_ID] != ELIMINADO and venta[VENTAS_CLIENTE] == id_cliente:
            ventas_cliente.append(venta)
            total_comprado += venta[VENTAS_IMPORTE]

    if len(ventas_cliente) == 0:
        print("\n\033[31m" "El cliente no tiene ventas registradas." "\033[0m")
    else:
        print("\nVENTAS DEL CLIENTE")
        mostrar_listado_ventas(ventas_cliente)
        print(
            f"\nTotal comprado por el cliente: "
            f"${redondear_precio(total_comprado):.2f}"
        )


def buscar_posicion_producto(codigo):
    """Devuelve la posicion de un producto segun su codigo, o -1 si no existe."""
    if codigo in productos_id_individual:
        return productos_id_individual.index(codigo)

    return -1


def pedir_cliente(mensaje):
    """Pide un id de cliente y no avanza hasta que exista o se cancele con -1."""
    id_cliente = obtener_entero(mensaje, -1, 1000000)

    while id_cliente != -1 and buscar_por_id(lista_clientes, id_cliente) == -2:
        print("\n\033[31mCliente inexistente.\033[0m\n")
        id_cliente = obtener_entero(mensaje, -1, 1000000)

    return id_cliente


def obtener_nombre_cliente(id_cliente):
    """Devuelve el nombre del cliente junto a su id, o un aviso si ya fue eliminado."""
    posicion = buscar_por_id(lista_clientes, id_cliente)

    if posicion == -2:
        return f"CLIENTE ELIMINADO ({id_cliente})"

    return f"{lista_clientes[posicion]['nombre']} ({id_cliente})"


def obtener_nombre_producto(codigo):
    """Devuelve el nombre del producto, o "ELIMINADO" si ya no existe."""
    posicion = buscar_posicion_producto(codigo)

    if posicion == -1:
        return "ELIMINADO"

    return PRODUCTOS[posicion][PRODUCTOS_NOMBRE]


def mostrar_listado_ventas(ventas_a_mostrar):
    """Imprime una tabla con los datos de las ventas que se le pasen."""
    ancho = 120
    print("-" * ancho)
    print(
        f"| {'ID':<6} | {'CLIENTE (ID)':<16} | {'PRODUCTO':<10} | "
        f"{'CATEGORIA':<9} | {'FECHA':<10} | {'CANT':<4} | "
        f"{'PRECIO':<9} | {'DESC.':<6} | {'P.FINAL':<9} | {'IMPORTE':<10} |"
    )
    print("-" * ancho)

    for venta in ventas_a_mostrar:
        posicion_producto = buscar_posicion_producto(venta[VENTAS_PRODUCTO])
        cliente = recortar_texto(obtener_nombre_cliente(venta[VENTAS_CLIENTE]), 16)
        producto = recortar_texto(obtener_nombre_producto(venta[VENTAS_PRODUCTO]), 10)
        categoria = recortar_texto(venta[VENTAS_CATEGORIA], 9)

        # Si el producto ya no existe, se muestra "-" en vez del precio y descuento original.
        if posicion_producto == -1:
            precio_original = "-"
            descuento = "-"
        else:
            precio_original = f"${PRODUCTOS[posicion_producto][PRODUCTOS_PRECIO]:.2f}"
            descuento = f"{PRODUCTOS[posicion_producto][PRODUCTOS_DESCUENTO]}%"

        precio_final = f"${venta[VENTAS_PRECIO_UNITARIO]:.2f}"
        importe = f"${venta[VENTAS_IMPORTE]:.2f}"

        print(
            f"| {venta[VENTAS_ID]:<6} | {cliente:<16} | {producto:<10} | "
            f"{categoria:<9} | {venta[VENTAS_FECHA]:<10} | "
            f"{venta[VENTAS_CANTIDAD]:<4} | {precio_original:<9} | "
            f"{descuento:<6} | {precio_final:<9} | {importe:<10} |"
        )

    print("-" * ancho)


redondear_precio = lambda numero: round(numero, 2)


def obtener_ventas_activas():
    """Devuelve las ventas que no fueron eliminadas."""
    ventas_activas = list(
        filter(
            lambda venta: venta[VENTAS_ID] != ELIMINADO,
            VENTAS,
        )
    )

    return ventas_activas


def obtener_importes_ventas():
    """Devuelve los importes de todas las ventas activas."""
    importes_ventas = list(
        map(
            lambda venta: venta[VENTAS_IMPORTE],
            obtener_ventas_activas(),
        )
    )

    return importes_ventas


def sumar_importes_ventas():
    """Suma los importes de las ventas activas usando reduce."""
    importes_ventas = obtener_importes_ventas()

    if len(importes_ventas) == 0:
        return 0

    suma_total = reduce(
        lambda acumulado, importe: acumulado + importe,
        importes_ventas,
    )

    return suma_total


def obtener_ids_ventas():
    """Devuelve los ID de las ventas activas sin repetirlos."""
    ids_ventas = []

    for fila in obtener_ventas_activas():

        if fila[VENTAS_ID] not in ids_ventas:

            ids_ventas.append(fila[VENTAS_ID])

    return ids_ventas


def obtener_categorias():
    """Devuelve las categorias que aparecen en las ventas activas."""
    categorias = []

    for venta in obtener_ventas_activas():

        categoria = venta[VENTAS_CATEGORIA]

        if categoria not in categorias:

            categorias.append(categoria)

    categorias.sort()

    return categorias


def total_venta(id_venta):
    """Devuelve el importe total de una venta activa."""
    total = 0

    for fila in obtener_ventas_activas():

        if fila[VENTAS_ID] == id_venta:

            total = total + fila[VENTAS_IMPORTE]

    return total


def contar_ventas():
    """Devuelve la cantidad de ventas activas sin repetir sus ID."""
    ids_ventas = obtener_ids_ventas()

    return len(ids_ventas)


def contar_ventas_categoria(categoria):
    """Cuenta los registros de productos vendidos en una categoria."""
    cantidad = 0

    categoria = categoria.upper()

    for fila in obtener_ventas_activas():

        if fila[VENTAS_CATEGORIA] == categoria:

            cantidad = cantidad + 1

    return cantidad


def promedio_ventas():
    """Devuelve el importe promedio por venta."""
    ids_ventas = obtener_ids_ventas()

    suma_total = sumar_importes_ventas()

    if len(ids_ventas) > 0:

        promedio = suma_total / len(ids_ventas)

    else:

        promedio = 0

    return promedio


def promedio_ventas_categoria(categoria):
    """Devuelve el importe promedio por registro de una categoria."""
    categoria = categoria.upper()

    total_categoria = 0

    for fila in obtener_ventas_activas():

        if fila[VENTAS_CATEGORIA] == categoria:

            total_categoria = total_categoria + fila[VENTAS_IMPORTE]

    cantidad = contar_ventas_categoria(categoria)

    if cantidad > 0:

        promedio = total_categoria / cantidad

    else:

        promedio = 0

    return promedio


def porcentaje_ventas_categoria(categoria):
    """Devuelve el porcentaje de registros de una categoria."""
    total = len(obtener_ventas_activas())

    cantidad_categoria = contar_ventas_categoria(categoria)

    if total > 0:

        porcentaje = cantidad_categoria * 100 / total

    else:

        porcentaje = 0

    return porcentaje


def total_productos_vendidos():
    """Devuelve la cantidad total de unidades vendidas."""
    cantidad_total = 0

    for fila in obtener_ventas_activas():

        cantidad_total = cantidad_total + fila[VENTAS_CANTIDAD]

    return cantidad_total


def mayor_menor_venta():
    """Devuelve los ID e importes de la mayor y la menor venta."""
    ids_ventas = obtener_ids_ventas()

    if len(ids_ventas) == 0:

        return 0, 0, 0, 0

    primer_id = ids_ventas[0]

    mayor = total_venta(primer_id)
    menor = total_venta(primer_id)

    id_mayor = primer_id
    id_menor = primer_id

    for id_venta in ids_ventas:

        total = total_venta(id_venta)

        if total > mayor:

            mayor = total
            id_mayor = id_venta

        if total < menor:

            menor = total
            id_menor = id_venta

    return (id_mayor, mayor, id_menor, menor)


def mostrar_estadisticas_categoria(categoria):
    """Muestra el resumen estadistico de una categoria."""
    cantidad = contar_ventas_categoria(categoria)
    promedio = promedio_ventas_categoria(categoria)
    porcentaje = porcentaje_ventas_categoria(categoria)

    print(
        f"\nCategoria: {categoria}"
        f"\nRegistros de productos vendidos: {cantidad}"
        f"\nPromedio por registro: ${redondear_precio(promedio):,.2f}"
        f"\nPorcentaje de registros: {redondear_precio(porcentaje):.2f}%"
    )


def resumen_estadistico():
    """Muestra un resumen general y por categoria de las ventas."""
    cantidad_ventas = contar_ventas()

    importe_total = redondear_precio(sumar_importes_ventas())

    promedio_general = redondear_precio(promedio_ventas())

    productos_vendidos = total_productos_vendidos()

    categorias = obtener_categorias()

    print(
        "\n=============================="
        "\n   ESTADISTICAS DE VENTAS"
        "\n=============================="
        f"\nCantidad total de ventas: {cantidad_ventas}"
        f"\nImporte total vendido: ${importe_total:,.2f}"
        f"\nPromedio por venta: ${promedio_general:,.2f}"
        f"\nTotal de productos vendidos: {productos_vendidos}"
        "\n"
    )

    print("ESTADISTICAS POR CATEGORIA")
    print("------------------------------")

    for categoria in categorias:
        mostrar_estadisticas_categoria(categoria)
        print("------------------------------")

    if cantidad_ventas > 0:

        (
            id_mayor,
            mayor,
            id_menor,
            menor,
        ) = mayor_menor_venta()

        print(
            f"Mayor venta: {id_mayor}"
            f"\nImporte: ${redondear_precio(mayor):,.2f}"
            "\n"
            f"\nMenor venta: {id_menor}"
            f"\nImporte: ${redondear_precio(menor):,.2f}"
            "\n=============================="
        )

    else:

        print("\nNo hay ventas registradas." "\n==============================")
