from Funciones.funciones import inicio,obtener_caracter,obtener_entero
import listas

clientes = [
    {"id": 1, "nombre": "Juan Pérez", "dni": "30111222", "telefono": "1145678901"},
    {"id": 2, "nombre": "Ana Gómez", "dni": "28555666", "telefono": "1156789012"},
    {"id": 3, "nombre": "Carlos Fernández", "dni": "32444555", "telefono": "1167890123"},
    {"id": 4, "nombre": "Lucía Martínez", "dni": "35222333", "telefono": "1178901234"},
    {"id": 5, "nombre": "Diego Rodríguez", "dni": "27888999", "telefono": "1189012345"},
    {"id": 6, "nombre": "Sofía López", "dni": "33666777", "telefono": "1190123456"},
    {"id": 7, "nombre": "Martín Sánchez", "dni": "29999000", "telefono": "1101234567"},
    {"id": 8, "nombre": "Valentina Torres", "dni": "31777888", "telefono": "1112345678"},
    {"id": 9, "nombre": "Federico Díaz", "dni": "26333444", "telefono": "1123456789"},
    {"id": 10, "nombre": "Camila Romero", "dni": "34111222", "telefono": "1134567890"},
]
    



def alta_clientes():
    texto = "ALTA DE CLIENTES"
    inicio(texto)
    

    nombre = input("Nombre: ").strip()
    apellido = input("Apellido: ").strip()
    dni = input("DNI: ").strip()
    telefono = input("Telefono: ").strip()
    email = input("Email: ").strip()

    nuevo_id = len(clientes) + 1

    cliente = {
        "id": nuevo_id,
        "nombre": nombre,
        "apellido": apellido,
        "dni": dni,
        "telefono": telefono,
        "email": email
    }

    clientes.append(cliente)

    print("Cliente agregado correctamente.")


def listado_clientes():
    texto = "LISTADO CLIENTES"
    inicio(texto)

    for cliente in clientes:
        print("ID:", cliente["id"])
        print("Nombre:", cliente["nombre"])
        print("Apellido:", cliente["apellido"])
        print("DNI:", cliente["dni"])
        print("Telefono:", cliente["telefono"])
        print("Email:", cliente["email"])
        print("------------------------")


def clientess():
    texto = "CLIENTES"
    inicio(texto)
    if listas.ADMIN == True:
        ask = obtener_entero(
            "0. Retroceder\n1. Listado de clientes\n2. Baja de clientes\n3.Alta de clientes\n4.Modificar clientes...",
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
    

def baja_clientes():
    pass
def modificar_clientes():
    pass
