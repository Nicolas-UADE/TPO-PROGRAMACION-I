from modulos import listas
from crud.crud_productos import productos
from crud.crud_clientes import clientes
from crud.crud_ventas import ventas
from Funciones.funciones_uni import obtener_entero, inicio

def mostrar_menu():
    """Muestra el menu principal y devuelve la opcion elegida."""
    texto = "MENU PRINCIPAL"
    inicio(texto)
    opcion = obtener_entero(
        "[0] 🚪 Salir\n[1] 📦 Productos\n[2] 👤 Clientes\n[3] 💰 Ventas\n.", 0, 3
    )
    return opcion


def menu_principal(admin, lector):
    """Loop principal del programa. Se llama UNA vez, después del login."""
    if admin == False and lector == False:
        print("\n\033[31mCredenciales incorrectas. Acceso denegado.\033[0m")
        return

    # Sincroniza con listas.py, que es de donde los CRUD leen el rol del usuario.
    listas.ADMIN = admin
    listas.LECTOR = lector

    while True:
        opcion = mostrar_menu()

        match opcion:
            case 0:
                print("Saliendo del programa...")
                return
            case 1:
                productos()
            case 2:
                clientes()
            case 3:
                ventas()