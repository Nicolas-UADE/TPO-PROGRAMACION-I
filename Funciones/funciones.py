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
)


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
    precios_finales=[]

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