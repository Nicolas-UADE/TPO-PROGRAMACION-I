
INGRESO = False
ADMIN = False
LECTOR = False
ELIMINADO = -1
USUARIOS_ADMIN = [
    "MARTIN",
    "LUCAS",
    "TOMAS",
    "FRANCO",
    "NICOLAS",
    "AGUSTIN",
    "JUAN",
    "MATEO",
    "SANTIAGO",
    "LEANDRO"
]
PRODUCTOS_CODIGO = 0
PRODUCTOS_NOMBRE = 1
PRODUCTOS_CATEGORIA = 2
PRODUCTOS_PRECIO = 3
PRODUCTOS_STOCK = 4
PRODUCTOS_DESCUENTO = 5

CONTRASENIAS_ADMIN = [
    1, 2, 3, 4, 5,
    6, 7, 8, 9, 10
]


          
USUARIOS_LECTORES = [
    "SOFIA",
    "VALENTINA",
    "JULIAN",
    "CAMILA",
    "FACUNDO",
    "MARTINA",
    "BENJAMIN",
    "LUCIA",
    "JOAQUIN",
    "PAULA"
]

CONTRASENIAS_LECTORES = [
    100, 101, 102, 103, 104,
    105, 106, 107, 108, 109
]

PRODUCTOS = [
    [482719,"Leche","Lacteos",1500,25,0],
    [935164,"Arroz","Alimento",1800,18,0],
    [271853,"Fideos","Alimento",1200,32,0],
    [604927,"Aceite","Alimento",3500,14,0],
    [158436,"Azucar","Alimento", 1300, 27,0],
    [793205,"Yerba","Alimento",4200,12,0],
    [326581,"Galletitas","Alimento",1600,20,0],
    [841672,"Cafe","Bebidas",5500,9,0],
    [519348,"Jabon","Limpieza",1400,35,0],
    [267914,"Gaseosa","Bebidas",2800,16,0]
]   

PRODUCTOS_LIMPIEZA = [
    "Lavandina",
    "Detergente",
    "Jabon",
    "Desinfectante",
    "Esponja",
    "Limpiavidrios",
    "Desengrasante",
    "Suavizante",
    "Escoba",
    "Trapo"
]

PRODUCTOS_COMIDA = [
    "Arroz",
    "Fideos",
    "Pan",
    "Galletitas",
    "Harina",
    "Atun",
    "Pure",
    "Aceite",
    "Azucar",
    "Sal"
]

PRODUCTOS_BEBIDA = [
    "Agua",
    "Coca Cola",
    "Sprite",
    "Fanta",
    "Jugo",
    "Soda",
    "Pepsi",
    "Gatorade",
    "Aquarius",
    "Paso de los Toros"
]
PRODUCTOS_OTROS = [
    "Pilas",
    "Servilletas",
    "Velas",
    "Fosforos",
    "Bolsas",
    "Papel aluminio",
    "Film",
    "Vasos",
    "Platos",
    "Encendedor"
]

def positivo(valor):
    return valor > 0


def rango(inicio,hasta,valor):
    return inicio <= valor and hasta >= valor

from funciones import generador_de_id

def genera_id():
    pass

def obtener_caracter(texto):
    ask = input(texto).upper()
    while len(ask) == 0:
        print("Debe ingresar un caracter")
        ask = input(texto).upper()
    return ask

def rectroceder():
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
    ordenados_codigo = sorted(PRODUCTOS,key=lambda fila: fila[PRODUCTOS_CODIGO])
    for p in ordenados_codigo:
        lista = print(f'{p[PRODUCTOS_CODIGO]:<15}{p[PRODUCTOS_NOMBRE]:15}{p[PRODUCTOS_CATEGORIA]:15}{p[PRODUCTOS_PRECIO]:<15}{p[PRODUCTOS_STOCK]:<15}{p[PRODUCTOS_DESCUENTO]:<15}')
    return lista

def ordenar_alfabeticamente():
    ordenados_codigo = sorted(PRODUCTOS,key=lambda fila: fila[PRODUCTOS_NOMBRE])
    for p in ordenados_codigo:
        lista = print(f'{p[PRODUCTOS_CODIGO]:<15}{p[PRODUCTOS_NOMBRE]:15}{p[PRODUCTOS_CATEGORIA]:15}{p[PRODUCTOS_PRECIO]:<15}{p[PRODUCTOS_STOCK]:<15}{p[PRODUCTOS_DESCUENTO]:<15}')
    return lista

def lista_cabeza_productos():
    list = []
    codigo = "Codigo"
    nombre = "Nombre"
    tipo = "Categoria"
    precio = "Precio"
    stock = "Stock"
    descuento = "Descuento"
    list.append(codigo),list.append(nombre),list.append(tipo),list.append(precio),list.append(stock),list.append(descuento)
    lista = print(f'{list[0]:<15}{list[1]:15}{list[2]:15}{list[3]:15}{list[4]:15}{list[5]:15}')
    return lista
         
def productos_activos():
    activos = []
    for i in PRODUCTOS:
        if PRODUCTOS[i][PRODUCTOS_CODIGO] != ELIMINADO:
            activos.append([PRODUCTOS[i][PRODUCTOS_CODIGO], 
                            PRODUCTOS[i][PRODUCTOS_CATEGORIA],
                            PRODUCTOS[i][PRODUCTOS_PRECIO],
                            PRODUCTOS[i][PRODUCTOS_STOCK],
                            PRODUCTOS[i][PRODUCTOS_DESCUENTO]])
    return activos
    
def login():
    INGRESO = False
    ADMIN = False
    LECTOR = False  
    print("==========\nBIENVENIDO\n==========")
    maximo_intentos = 4
    ask_usuario = obtener_caracter("Ingrese usuario...")

    ask_code = obtener_entero("Ingrese contrasenia (Numerica)...",0,1000)

    es_admin_usuario = busqueda_secuencial(USUARIOS_ADMIN,ask_usuario) 

    es_admin_contrasenia = busqueda_secuencial(CONTRASENIAS_ADMIN,ask_code)

    es_lector_usuario = busqueda_secuencial(USUARIOS_LECTORES,ask_usuario) 

    es_lector_contrasenia = busqueda_secuencial(CONTRASENIAS_LECTORES,ask_code)


    if es_admin_usuario == es_admin_contrasenia and es_admin_usuario != -1 and es_admin_contrasenia != -1:
        ADMIN = True
    elif es_lector_usuario == es_lector_contrasenia and es_lector_usuario != -1 and es_lector_contrasenia != -1:
        LECTOR = True

    while ADMIN == False and LECTOR == False and maximo_intentos > 0:
        print("Usuario o contrasenia incorrectas.", maximo_intentos, "cantidad de intentos restantes")     

        maximo_intentos -= 1

        ask_usuario = obtener_caracter("Ingrese usuario...") 

        ask_code = obtener_entero("Ingrese contrasenia (Numerica)...",0,1000)

        es_admin_usuario = busqueda_secuencial(USUARIOS_ADMIN,ask_usuario) 

        es_admin_contrasenia = busqueda_secuencial(CONTRASENIAS_ADMIN,ask_code)

        es_lector_usuario = busqueda_secuencial(USUARIOS_LECTORES,ask_usuario) 

        es_lector_contrasenia = busqueda_secuencial(CONTRASENIAS_LECTORES,ask_code)

        if es_admin_usuario == es_admin_contrasenia and es_admin_usuario != -1 and es_admin_contrasenia != -1:
            ADMIN = True
        elif es_lector_usuario == es_lector_contrasenia and es_lector_usuario != -1 and es_lector_contrasenia != -1:
            LECTOR = True


    if maximo_intentos == 0:
        print("Maximo de intentos exedido\n Acceso denegado...")
        INGRESO = False
        return  ADMIN , LECTOR , INGRESO 
    else:
        INGRESO = True

        
    return ADMIN , LECTOR , INGRESO



def menu_principal():
    print("\n\n==========\nMENU PRINCIPAL\n==========")
    ask_menu = obtener_entero("0. Salir\n1. Productos\n2. Clientes\n3.Ventas...",0,3)

    if ask_menu == 0:
        print("Saliendo del programa...")
        return 0
   
    return ask_menu


def productos():
    print("\n\n==========\nPRODUCTOS\n==========")
    if ADMIN == True:
        ask = obtener_entero("0. Retroceder\n1. Listado de producto\n2. Baja de producto\n3.Alta de producto\n Modificar producto...",0,4)
        match ask:
            case 0:
                rectroceder()
            case 1:
                listar_productos()
            case 2:
                baja_producto()
            case 3:
                alta_producto()
            case 4:
                modificar_producto()
    else:
        ask = obtener_entero("0. Retroceder\n1. Listado de producto\n",0,1)
        match ask:
            case 0:
                rectroceder()
            case 1:
                listar_productos()

def alta_producto():
    print("\n\n==========ALTA DE PRODUCTOS==========")

    pregunta_codigo = obtener_entero("\nIngrese código del producto... -1 Para salir...",-1,1000000)

    while pregunta_codigo == 0:
            print("Codigo inexistente...")
            pregunta_codigo = obtener_entero("\nIngrese código del producto a eliminar. -1 Para salir...",-1,1000000)

    if pregunta_codigo == -1:
                menu_principal()
                print("Volviendo al menu principal...\n\n")

    pos = busqueda_secuencial()

    while pos != -1:
        print("Ya existe un producto con ese código.")

        pregunta_codigo = obtener_entero("\nIngrese código del producto... -1 Para salir...",-1,1000000)
        
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

        PRODUCTOS.append(pregunta_codigo,pregunta_nombre,categoria,precio,stock,descuento)
        print("\n\nProducto agregado correctamente.\n\n")
        print('===================')


def baja_producto():

    print("\n\n==========BAJA DE PRODUCTOS==========")

    pregunta_codigo = obtener_entero("\n\nIngrese código del producto a eliminar. -1 Para salir...",-1,1000000)

    

    while pregunta_codigo == 0:
        print("Codigo inexistente...")
        pregunta_codigo = obtener_entero("\nIngrese código del producto a eliminar. -1 Para salir...",-1,1000000)

    if pregunta_codigo == -1:
                    menu_principal()
                    print("Volviendo al menu principal...\n\n")

    pos = busqueda_secuencial(PRODUCTOS, pregunta_codigo)

    while pos == -1:
        print("Producto inexistente.")
        pregunta_codigo = obtener_entero("\nIngrese código del producto a eliminar. -1 Para salir...",-1,1000000)
        pos = busqueda_secuencial(PRODUCTOS,pregunta_codigo)


    pregunta_seguridad = obtener_caracter(f"\nEsta seguro de eliminar el producto {pregunta_codigo}? Y/N...").upper()

    if pregunta_seguridad == "Y":
        
        PRODUCTOS[PRODUCTOS_CODIGO][pos] = -1
        

        print("Producto eliminado correctamente.")
        print('===================')
    else:
        print("\nBaja de producto cancelada.")
        print('===================')
        


def modificar_producto():
    print("\n\n==========MODIFICACION DE PRODUCTOS==========")

    pregunta_codigo = obtener_entero("\nIngrese código del producto... -1 Para salir...",-1,1000000)

    while pregunta_codigo == 0:
            print("Codigo inexistente...")
            pregunta_codigo = obtener_entero("\nIngrese código del producto... -1 Para salir...",-1,1000000)

    if pregunta_codigo == -1:
                menu_principal()
                print("Volviendo al menu principal...\n\n")


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

        stock = obtener_entero("Ingrese nuevo stock: ",0,1000000)

        PRODUCTOS[PRODUCTOS_STOCK][pos] = stock

        descuento = float(input("Ingrese nuevo descuento: "))

        while descuento < 0 or descuento > 100:
            descuento = float(input("Descuento inválido. Reingrese: "))

        PRODUCTOS[PRODUCTOS_DESCUENTO][pos] = descuento

        print("Producto modificado correctamente.")
        print('===================')


def listar_productos():

    print("\n\n==========LISTA DE PRODUCTOS==========")
    pregunta_orden = obtener_entero("Elija metodo de ordenamiento. 1.ID  2.ALFABETICAMENTE ",1,2)
    if pregunta_orden == 1:
        lista_cabeza_productos()
        print()
        ordenar_por_codigo()
    else:
         lista_cabeza_productos()
         print()
         ordenar_alfabeticamente()

    print('===================')

def clientes():
    print("==========\nCLIENTES\n==========")

def ventas():
    print("==========\nVENTAS\n==========")

ADMIN , LECTOR , INGRESO = login()

print(ADMIN,LECTOR,INGRESO)
if INGRESO == True:
    print("Ingreso exitoso")

opcion = -1
while opcion != 0:
    opcion = menu_principal()
    match opcion:
        case 1:
            productos()
        case 2:
            clientes()
        case 3:
            ventas()


    
            


