from Funciones.funciones import inicio,obtener_caracter,obtener_entero,lista_cabeza_clientes,buscar_por_id
import listas
from listas import ELIMINADO
lista_clientes = [
    {"id": 1, "nombre": "JUAN PÉREZ", "dni": "30111222", "telefono": "1145678901", "email": "juan.perez@mail.com"},
    {"id": 2, "nombre": "ANA GÓMEZ", "dni": "28555666", "telefono": "1156789012", "email": "ana.gomez@mail.com"},
    {"id": 3, "nombre": "CARLOS FERNÁNDEZ", "dni": "32444555", "telefono": "1167890123", "email": "carlos.fernandez@mail.com"},
    {"id": 4, "nombre": "LUCÍA MARTÍNEZ", "dni": "35222333", "telefono": "1178901234", "email": "lucia.martinez@mail.com"},
    {"id": 5, "nombre": "DIEGO RODRÍGUEZ", "dni": "27888999", "telefono": "1189012345", "email": "diego.rodriguez@mail.com"},
    {"id": 6, "nombre": "SOFÍA LÓPEZ", "dni": "33666777", "telefono": "1190123456", "email": "sofia.lopez@mail.com"},
    {"id": 7, "nombre": "MARTÍN SÁNCHEZ", "dni": "29999000", "telefono": "1101234567", "email": "martin.sanchez@mail.com"},
    {"id": 8, "nombre": "VALENTINA TORRES", "dni": "31777888", "telefono": "1112345678", "email": "valentina.torres@mail.com"},
    {"id": 9, "nombre": "FEDERICO DÍAZ", "dni": "26333444", "telefono": "1123456789", "email": "federico.diaz@mail.com"},
    {"id": 10, "nombre": "CAMILA ROMERO", "dni": "34111222", "telefono": "1134567890", "email": "camila.romero@mail.com"},
]

def clientes():
    texto = "CLIENTES"
    inicio(texto)
    if listas.ADMIN == True:
        ask = obtener_entero(
            "0. Retroceder\n1. Listado de clientes\n2. Baja de clientes\n3.Alta de clientes\n4.Modificar clientes\n.",
            0,
            4,
        )
        match ask:
            case 0:
                return
            case 1:
                listado_clientes()
            case 2:
                baja_clientes()
            case 3:
                alta_clientes()
            case 4:
                modificar_clientes()
    else:
        ask = obtener_entero("0. Retroceder\n1. Listado de clientes\n", 0, 1)
        match ask:
            case 0:
                return
            case 1:
                listado_clientes()



def alta_clientes():
    texto = "ALTA DE CLIENTES"
    inicio(texto)
    

    nombre = obtener_caracter("Nombre y apellido:\n.").upper()
    dni = obtener_entero("DNI:\n.",1000000,99999999)
    telefono = obtener_entero("Telefono:\n.",1000000000,9999999999)
    email = obtener_caracter("Email:\n.").lower()

    el_dni = str(dni)
    el_telefono = str(telefono)

    nuevo_id = len(lista_clientes) + 1

    cliente = {
        "id": nuevo_id,
        "nombre": nombre,
        "dni": el_dni,
        "telefono": el_telefono,
        "email": email
    }
    lista_clientes.append(cliente)

    print("Cliente agregado correctamente.")
    texto = ""
    inicio(texto)
    


def listado_clientes():
    texto = "LISTADO CLIENTES"
    inicio(texto)
    lista_cabeza_clientes()

    for cliente in lista_clientes:
        if cliente != ELIMINADO:
            print(f'|{cliente['id']:<20} | {cliente['nombre']:<20} | {cliente['dni']:<20} | {cliente['telefono']:<20} | {cliente['email']:<20}')
        
    ancho = 120
    print("-" * ancho)



    

def baja_clientes():
    texto = "BAJA DE CLIENTES"
    inicio(texto)

    pregunta_codigo = obtener_entero(
        "\n\nIngrese código del cliente a eliminar. -1 Para salir\n.", -1, 1000000
    )

    while pregunta_codigo == 0:
        pregunta_codigo = obtener_entero(
            "\nIngrese código del cliente a eliminar. -1 Para salir\n.", -1, 1000000
        )

    if pregunta_codigo == -1:
        return

    esta = buscar_por_id(lista_clientes,pregunta_codigo)
    while esta == -2:
        print("Cliente inexistente.")
        pregunta_codigo = obtener_entero(
            "\nIngrese código del cliente a eliminar. -1 Para salir\n.", -1, 1000000
        )
        if pregunta_codigo == -1:
            return
        esta = buscar_por_id(lista_clientes,pregunta_codigo)
        


    pregunta_seguridad = obtener_caracter(
        f"\nEsta seguro de eliminar al cliente {pregunta_codigo}? Y/N\n."
    ).upper()

    if pregunta_seguridad == "Y":

        lista_clientes[esta] = ELIMINADO

        print("Cliente eliminado correctamente.")

    else:
        print("\nBaja de cliente cancelada.")
    texto = ""
    inicio(texto)


def modificar_clientes():
    texto = "MODIFICAR CLIENTES"
    inicio(texto)

