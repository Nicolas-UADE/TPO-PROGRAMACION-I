import random
from listas import (
    CONTRASENIAS_ADMIN,
    CONTRASENIAS_LECTORES,
    ELIMINADO,
    PRODUCTOS,
    PRODUCTOS_CATEGORIA,
    PRODUCTOS_CODIGO,
    PRODUCTOS_DESCUENTO,
    PRODUCTOS_NOMBRE,
    PRODUCTOS_PRECIO,
    PRODUCTOS_STOCK,
    USUARIOS_ADMIN,
    USUARIOS_LECTORES,
)


def normalizar_texto(texto):
    texto = texto.strip()
    palabras = texto.split()
    texto = " ".join(palabras)
    return texto


def cadenas_iguales(texto_uno, texto_dos):
    texto_uno = normalizar_texto(texto_uno).lower()
    texto_dos = normalizar_texto(texto_dos).lower()
    return texto_uno == texto_dos


def recortar_texto(texto, cantidad):
    if len(texto) > cantidad:
        texto = texto[:cantidad - 3] + "..."
    return texto


def generador_de_id(lista):
    nuevo_id = random.randint(100000, 1000000)

    while nuevo_id in lista:
        nuevo_id = random.randint(100000, 1000000)

    return nuevo_id


def positivo(valor):
    return valor > 0


def productos_activos():
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


def buscar_productos_por_nombre(matriz_productos, texto_buscado):
    productos_encontrados = []
    texto_buscado = normalizar_texto(texto_buscado).lower()

    for producto in matriz_productos:
        nombre_producto = normalizar_texto(producto[PRODUCTOS_NOMBRE]).lower()

        if producto[PRODUCTOS_CODIGO] != ELIMINADO and texto_buscado in nombre_producto:
            productos_encontrados.append(producto)

    return productos_encontrados


def inicio(texto):
    print(texto.center(96, "-"))

def rango(inicio, hasta, valor):
    return inicio <= valor and hasta >= valor

def redondeo(numero):
    return f'$ {numero:,.2f}'


def mostrar_producto(producto):
    nombre = normalizar_texto(producto[PRODUCTOS_NOMBRE]).upper()
    categoria = normalizar_texto(producto[PRODUCTOS_CATEGORIA]).upper()
    nombre = recortar_texto(nombre, 15)
    categoria = recortar_texto(categoria, 15)
    precio = redondeo(producto[PRODUCTOS_PRECIO])
    descuento = f"{producto[PRODUCTOS_DESCUENTO]} %"

    print(
        f"{producto[PRODUCTOS_CODIGO]:<15} | {nombre:<15} | {categoria:<15} | {precio:<15} | {producto[PRODUCTOS_STOCK]:<15} | {descuento:<15}"
    )
    

def coincidencia(pregunta_usu,pregunta_code):
    ADMIN = False
    LECTOR = False
    es_admin_usuario = busqueda_secuencial(USUARIOS_ADMIN,pregunta_usu) 
    
    es_admin_contrasenia = busqueda_secuencial(CONTRASENIAS_ADMIN,pregunta_code)

    es_lector_usuario = busqueda_secuencial(USUARIOS_LECTORES,pregunta_usu) 

    es_lector_contrasenia = busqueda_secuencial(CONTRASENIAS_LECTORES,pregunta_code)

    if es_admin_usuario == es_admin_contrasenia and es_admin_usuario != -1 and es_admin_contrasenia != -1:
            ADMIN = True
    elif es_lector_usuario == es_lector_contrasenia and es_lector_usuario != -1 and es_lector_contrasenia != -1:
            LECTOR = True
    return ADMIN , LECTOR

def obtener_caracter(texto):
    ask = normalizar_texto(input(texto)).upper()
    while len(ask) == 0:
        print("Debe ingresar un caracter")
        ask = normalizar_texto(input(texto)).upper()
    return ask

def buscar(lista,elemento):
    lista_origen = []
    lista_origen.extend(lista)
    contador = 0
    posiciones = []
    while elemento in lista_origen:
        posicion = lista_origen.index(elemento)
        posiciones.append(posicion)

        lista_origen[posicion] = 0
        contador +=1
        
            
    return contador,posiciones

        

def obtener_entero(texto, minimo, maximo):
    valor_invalido = True
    while valor_invalido == True:
        valor_str = input(texto)
        while len(valor_str) == 0:
            print("Valor invalido.")
            valor_str = input(texto)

        valor = int(valor_str)
        if not rango(minimo, maximo, valor):
            print("Valor no valido.")
        else:
            valor_invalido = False
    return valor


def busqueda_secuencial(lista, parametro):
    i = 0
    while i < len(lista) and lista[i] != parametro:
        i += 1
    if i < len(lista):
        return i
    else:
        return -1


def busqueda_por_codigo(lista, codigo):
    i = 0
    while i < len(lista) and lista[i][PRODUCTOS_CODIGO] != codigo:
        i += 1
    if i < len(lista):
        return i
    else:
        return -1


def ordenar_por_codigo():
    ordenados_codigo = sorted(productos_activos(), key=lambda fila: fila[PRODUCTOS_CODIGO])
    ancho = 96
    print("-" * ancho)
    for p in ordenados_codigo:
        mostrar_producto(p)
    print("-" * ancho)


def ordenar_alfabeticamente():
    ordenados_codigo = sorted(productos_activos(), key=lambda fila: fila[PRODUCTOS_NOMBRE])
    ancho = 96
    print("-" * ancho)
    for p in ordenados_codigo:
        mostrar_producto(p)
    print("-" * ancho)


def lista_cabeza_productos():
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
    ancho = 96
    print("-" * ancho)
    print(
        f"{list[0]:<15} | {list[1]:<15} | {list[2]:<15} | {list[3]:<15} | {list[4]:<15} | {list[5]:<15}"
    )
    
    print("-" * ancho)
