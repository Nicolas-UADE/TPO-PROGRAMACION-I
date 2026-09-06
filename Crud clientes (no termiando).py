clientes = [
    {
        "id": 1,
        "nombre": "Juan",
        "apellido": "Perez",
        "dni": "40123456",
        "telefono": "1123456789",
        "email": "juan@gmail.com"
    },
    {
        "id": 2,
        "nombre": "Maria",
        "apellido": "Gomez",
        "dni": "42345678",
        "telefono": "1145678910",
        "email": "maria@gmail.com"
    }
]


def agregar_cliente():
    print("\n--- AGREGAR CLIENTE ---")

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


def mostrar_clientes():
    print("\n--- LISTA DE CLIENTES ---")

    for cliente in clientes:
        print("ID:", cliente["id"])
        print("Nombre:", cliente["nombre"])
        print("Apellido:", cliente["apellido"])
        print("DNI:", cliente["dni"])
        print("Telefono:", cliente["telefono"])
        print("Email:", cliente["email"])
        print("------------------------")


def menu_clientes():
    opcion = 0

    while opcion != 3:
        print("\n===== MENU CLIENTES =====")
        print("1. Agregar cliente")
        print("2. Mostrar clientes")
        print("3. Salir")

        opcion = int(input("Ingrese una opcion: "))

        if opcion == 1:
            agregar_cliente()

        elif opcion == 2:
            mostrar_clientes()

        elif opcion == 3:
            print("Saliendo del menu...")

        else:
            print("Opcion invalida.")


menu_clientes()