from listas import PRODUCTOS_CODIGO,PRODUCTOS_NOMBRE,PRODUCTOS_CATEGORIA,PRODUCTOS_PRECIO,USUARIOS_ADMIN,USUARIOS_LECTORES
from listas import PRODUCTOS_STOCK,PRODUCTOS,PRODUCTOS_DESCUENTO,ELIMINADO,USUARIOS_ADMIN,CONTRASENIAS_ADMIN,CONTRASENIAS_LECTORES


def generador_de_id():
    pass

def positivo(valor):
    return valor > 0


def rango(inicio, hasta, valor):
    return inicio <= valor and hasta >= valor


#from funciones import generador_de_id


def genera_id():
    pass

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
    ask = input(texto).upper()
    while len(ask) == 0:
        print("Debe ingresar un caracter")
        ask = input(texto).upper()
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

def volver_al_menu():
        from menu import menu_principal
        print("Volviendo al menu principal...\n\n")
        menu_principal()
        

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
    ordenados_codigo = sorted(PRODUCTOS, key=lambda fila: fila[PRODUCTOS_CODIGO])
    for p in ordenados_codigo:
        lista = print(
            f"{p[PRODUCTOS_CODIGO]:<15}{p[PRODUCTOS_NOMBRE]:15}{p[PRODUCTOS_CATEGORIA]:15}{p[PRODUCTOS_PRECIO]:<15}{p[PRODUCTOS_STOCK]:<15}{p[PRODUCTOS_DESCUENTO]:<15}"
        )
    return lista


def ordenar_alfabeticamente():
    ordenados_codigo = sorted(PRODUCTOS, key=lambda fila: fila[PRODUCTOS_NOMBRE])
    for p in ordenados_codigo:
        lista = print(
            f"{p[PRODUCTOS_CODIGO]:<15}{p[PRODUCTOS_NOMBRE]:15}{p[PRODUCTOS_CATEGORIA]:15}{p[PRODUCTOS_PRECIO]:<15}{p[PRODUCTOS_STOCK]:<15}{p[PRODUCTOS_DESCUENTO]:<15}"
        )
    return lista


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
    lista = print(
        f"{list[0]:<15}{list[1]:15}{list[2]:15}{list[3]:15}{list[4]:15}{list[5]:15}"
    )
    return lista


def productos_activos():
    activos = []
    for i in PRODUCTOS:
        if PRODUCTOS[i][PRODUCTOS_CODIGO] != ELIMINADO:
            activos.append(
                [
                    PRODUCTOS[i][PRODUCTOS_CODIGO],
                    PRODUCTOS[i][PRODUCTOS_CATEGORIA],
                    PRODUCTOS[i][PRODUCTOS_PRECIO],
                    PRODUCTOS[i][PRODUCTOS_STOCK],
                    PRODUCTOS[i][PRODUCTOS_DESCUENTO],
                ]
            )
    return activos