# Variables globales de estado de sesion. Se van pisando desde el login.
ADMIN = False
LECTOR = False

# Valor que se usa como "marca" para indicar que un elemento fue dado de baja,
# en vez de borrarlo de la lista (asi no se rompen los indices de otras listas relacionadas).
ELIMINADO = -1

# Usuarios y contraseñas validos para el login. Las tuplas de usuario y contraseña
# se relacionan por posicion: USUARIOS_ADMIN[i] usa CONTRASENIAS_ADMIN[i].
USUARIOS_ADMIN = (
    "MARTIN",
    "LUCAS",
    "TOMAS",
    "FRANCO",
    "NICOLAS",
    "AGUSTIN",
    "JUAN",
    "MATEO",
    "SANTIAGO",
    "LEANDRO",
)

CONTRASENIAS_ADMIN = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

CONTRASENIAS_LECTORES = (100, 101, 102, 103, 104, 105, 106, 107, 108, 109)

USUARIOS_LECTORES = (
    "SOFIA",
    "VALENTINA",
    "JULIAN",
    "CAMILA",
    "FACUNDO",
    "MARTINA",
    "BENJAMIN",
    "LUCIA",
    "JOAQUIN",
    "PAULA",
)

# Constantes con la posicion de cada dato dentro de cada fila de PRODUCTOS.
# Se usan en vez de numeros sueltos para que el codigo sea mas facil de leer
# (ej: producto[PRODUCTOS_PRECIO] en vez de producto[3]).
PRODUCTOS_CODIGO = 0
PRODUCTOS_NOMBRE = 1
PRODUCTOS_CATEGORIA = 2
PRODUCTOS_PRECIO = 3
PRODUCTOS_STOCK = 4
PRODUCTOS_DESCUENTO = 5


# Los productos se cargan desde el archivo al iniciar el programa.
from Funciones.archivos_productos import cargar_productos_archivo
from Funciones.archivos_clientes import cargar_clientes_json

PRODUCTOS = cargar_productos_archivo()

#############################################
# CLIENTES#
# Lista de clientes. Se carga desde clientes.json al iniciar el programa.
lista_clientes = cargar_clientes_json()


# VENTAS

# Constantes con la posicion de cada dato dentro de cada fila de VENTAS.
VENTAS_ID = 0
VENTAS_CLIENTE = 1
VENTAS_PRODUCTO = 2
VENTAS_CATEGORIA = 3
VENTAS_FECHA = 4
VENTAS_CANTIDAD = 5
VENTAS_PRECIO_UNITARIO = 6
VENTAS_IMPORTE = 7


# Cada fila de ventas se lee del archivo de texto al iniciar.
from Funciones.archivos_ventas import cargar_ventas_archivo

VENTAS = cargar_ventas_archivo()
