ARCHIVO_VENTAS = "archivos/ventas.txt"


def convertir_venta(linea):
    datos = linea.strip().split(";")
    return [
        int(datos[0]),
        int(datos[1]),
        int(datos[2]),
        datos[3],
        datos[4],
        int(datos[5]),
        int(datos[6]),
        int(datos[7]),
    ]


def mostrar_ventas_archivo():
    try:
        with open(ARCHIVO_VENTAS, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                venta = convertir_venta(linea)
                print(venta)
    except FileNotFoundError:
        print("No se encontro el archivo de ventas.")


def buscar_ventas_archivo(id_venta):
    ventas_encontradas = []
    try:
        with open(ARCHIVO_VENTAS, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                venta = convertir_venta(linea)
                if venta[0] == id_venta:
                    ventas_encontradas.append(venta)
    except FileNotFoundError:
        print("No se encontro el archivo de ventas.")
    return ventas_encontradas
