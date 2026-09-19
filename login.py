from Funciones.funciones import obtener_caracter, obtener_entero, coincidencia


def login():
    # Pantalla de acceso al sistema. Da 4 intentos para ingresar usuario y contraseña.
    print("==========\nBIENVENIDO\n==========")
    intentos_restantes = 4

    while intentos_restantes > 0:
        usuario = obtener_caracter("Ingrese usuario\n.")
        contrasenia = obtener_entero("Ingrese contrasenia (Numerica)\n.", 0, 1000)

        # Chequea si el usuario y contraseña coinciden con los de admin o lector.
        admin, lector = coincidencia(usuario, contrasenia)

        if admin == True or lector == True:
            print("\n\033[1;34mBienvenido al sistema\033[0m")
            return admin, lector, True

        # Si no coincide ninguno de los dos, se resta un intento.
        intentos_restantes -= 1

        if intentos_restantes > 0:
            print(
                "Usuario o contrasenia incorrectas.",
                intentos_restantes,
                "intentos restantes.",
            )

    # Se agotaron los intentos, no se deja entrar al sistema.
    print("Maximo de intentos excedido.\nAcceso denegado...")
    return False, False, False