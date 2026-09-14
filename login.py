from Funciones.funciones import obtener_caracter, obtener_entero, coincidencia


def login():
    print("==========\nBIENVENIDO\n==========")
    intentos_restantes = 4

    while intentos_restantes > 0:
        usuario = obtener_caracter("Ingrese usuario\n.")
        contrasenia = obtener_entero("Ingrese contrasenia (Numerica)\n.", 0, 1000)

        admin, lector = coincidencia(usuario, contrasenia)

        if admin == True or lector == True:
            print("\n\033[1;34mBienvenido al sistema\033[0m")
            return admin, lector, True

        intentos_restantes -= 1

        if intentos_restantes > 0:
            print(
                "Usuario o contrasenia incorrectas.",
                intentos_restantes,
                "intentos restantes.",
            )

    print("Maximo de intentos excedido.\nAcceso denegado...")
    return False, False, False
