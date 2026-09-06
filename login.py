from Funciones.funciones import obtener_caracter,obtener_entero,coincidencia

def login():
    INGRESO = False
    ADMIN = False
    LECTOR = False  
    print("==========\nBIENVENIDO\n==========")
    maximo_intentos = 4
    ask_usuario = obtener_caracter("Ingrese usuario...")

    ask_code = obtener_entero("Ingrese contrasenia (Numerica)...",0,1000)

    ADMIN,LECTOR = coincidencia(ask_usuario,ask_code)

    while ADMIN == False and LECTOR == False and maximo_intentos > 0:
        print("Usuario o contrasenia incorrectas.", maximo_intentos, "cantidad de intentos restantes")     

        maximo_intentos -= 1

        ask_usuario = obtener_caracter("Ingrese usuario...") 

        ask_code = obtener_entero("Ingrese contrasenia (Numerica)...",0,1000)

        ADMIN,LECTOR = coincidencia(ask_usuario,ask_code)

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