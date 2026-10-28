ARCHIVO_PRODUCTOS = "archivos/productos.txt"


def convertir_producto(linea):
    datos = linea.strip().split(";")
    return [
        int(datos[0]),
        datos[1],
        datos[2],
        int(datos[3]),
        int(datos[4]),
        int(datos[5]),
    ]


def preparar_linea_producto(producto):
    return (
        f"{producto[0]};{producto[1]};{producto[2]};"
        f"{producto[3]};{producto[4]};{producto[5]}\n"
    )


def cargar_productos_archivo():
    productos = []
    try:
        with open(ARCHIVO_PRODUCTOS, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                if linea.strip() != "":
                    productos.append(convertir_producto(linea))
    except FileNotFoundError:
        print("No se encontro el archivo de productos.")
    return productos


def guardar_productos_archivo(productos):
    with open(ARCHIVO_PRODUCTOS, "w", encoding="utf-8") as archivo:
        for producto in productos:
            archivo.write(preparar_linea_producto(producto))


def mostrar_productos_archivo():
    try:
        with open(ARCHIVO_PRODUCTOS, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                if linea.strip() != "":
                    producto = convertir_producto(linea)
                    if producto[0] != -1:
                        print(producto)
    except FileNotFoundError:
        print("No se encontro el archivo de productos.")


def buscar_producto_archivo(codigo):
    try:
        with open(ARCHIVO_PRODUCTOS, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                if linea.strip() != "":
                    producto = convertir_producto(linea)
                    if producto[0] == codigo:
                        return producto
    except FileNotFoundError:
        print("No se encontro el archivo de productos.")
    return None
