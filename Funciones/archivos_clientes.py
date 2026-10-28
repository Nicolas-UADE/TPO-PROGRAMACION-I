ARCHIVO_CLIENTES = "archivos/clientes.txt"


def convertir_cliente(linea):
    datos = linea.strip().split(";")
    return {
        "id": int(datos[0]),
        "nombre": datos[1],
        "dni": datos[2],
        "telefono": datos[3],
        "email": datos[4],
    }


def mostrar_clientes_archivo():
    try:
        with open(ARCHIVO_CLIENTES, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                cliente = convertir_cliente(linea)
                print(cliente)
    except FileNotFoundError:
        print("No se encontro el archivo de clientes.")


def buscar_cliente_archivo(id_cliente):
    try:
        with open(ARCHIVO_CLIENTES, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                cliente = convertir_cliente(linea)
                if cliente["id"] == id_cliente:
                    return cliente
    except FileNotFoundError:
        print("No se encontro el archivo de clientes.")
    return None
