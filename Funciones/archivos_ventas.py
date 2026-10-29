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
        float(datos[6]),
        float(datos[7]),
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


def preparar_linea_venta(venta):
    return (
        f"{venta[0]};{venta[1]};{venta[2]};{venta[3]};"
        f"{venta[4]};{venta[5]};{venta[6]};{venta[7]}\n"
    )


def agregar_ventas_archivo(ventas_nuevas):
    if len(ventas_nuevas) == 0:
        return False

    try:
        with open(ARCHIVO_VENTAS, "a", encoding="utf-8") as archivo:
            for venta in ventas_nuevas:
                archivo.write(preparar_linea_venta(venta))
        return True
    except OSError:
        print("No se pudo guardar la venta.")
        return False
