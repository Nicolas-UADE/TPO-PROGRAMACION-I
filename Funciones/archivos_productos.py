import os

ARCHIVO_PRODUCTOS = "archivos/productos.txt"
ARCHIVO_AUXILIAR = "archivos/productos_auxiliar.txt"


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
    except (OSError, ValueError, IndexError):
        print("No se pudieron leer los productos.")
        return []
    return productos


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
    except (OSError, ValueError, IndexError):
        print("No se pudieron leer los productos.")


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
    except (OSError, ValueError, IndexError):
        print("No se pudieron leer los productos.")
    return None


def agregar_producto_archivo(producto):
    try:
        with open(ARCHIVO_PRODUCTOS, "a", encoding="utf-8") as archivo:
            archivo.write(preparar_linea_producto(producto))
        return True
    except OSError:
        print("No se pudo guardar el producto.")
        return False


def reemplazar_producto_archivo(codigo, producto_nuevo):
    encontrado = False
    try:
        with open(ARCHIVO_PRODUCTOS, "r", encoding="utf-8") as archivo:
            with open(ARCHIVO_AUXILIAR, "w", encoding="utf-8") as auxiliar:
                for linea in archivo:
                    producto = convertir_producto(linea)
                    if producto[0] == codigo:
                        auxiliar.write(preparar_linea_producto(producto_nuevo))
                        encontrado = True
                    else:
                        auxiliar.write(linea)

        if encontrado:
            os.replace(ARCHIVO_AUXILIAR, ARCHIVO_PRODUCTOS)
            return True

        os.remove(ARCHIVO_AUXILIAR)
        return False
    except (OSError, ValueError, IndexError):
        print("No se pudo modificar el archivo de productos.")
        if os.path.exists(ARCHIVO_AUXILIAR):
            os.remove(ARCHIVO_AUXILIAR)
        return False
