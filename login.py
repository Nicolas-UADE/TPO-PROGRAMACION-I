from Funciones.funciones import obtener_caracter,obtener_entero,busqueda_secuencial
from listas import USUARIOS_ADMIN,USUARIOS_LECTORES,CONTRASENIAS_LECTORES,CONTRASENIAS_ADMIN

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

ADMIN, LECTOR, INGRESO = login()

print(ADMIN, LECTOR, INGRESO)
if INGRESO == True:
    print("Ingreso exitoso")