import json

ARCHIVO_CLIENTES = "archivos/clientes.txt"
ARCHIVO_CLIENTES_JSON = "archivos/clientes.json"


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


def cargar_clientes_json():
    """Lee los clientes desde clientes.json y devuelve una lista de diccionarios."""
    try:
        with open(ARCHIVO_CLIENTES_JSON, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        print("No se encontro el archivo de clientes.")
    except (OSError, ValueError):
        print("No se pudieron leer los clientes.")
    return []


def guardar_clientes_json(clientes):
    """Guarda la lista de clientes en clientes.json. Devuelve True si se pudo guardar."""
    try:
        with open(ARCHIVO_CLIENTES_JSON, "w", encoding="utf-8") as archivo:
            json.dump(clientes, archivo, indent=4, ensure_ascii=False)
        return True
    except OSError:
        print("No se pudieron guardar los clientes.")
        return False
