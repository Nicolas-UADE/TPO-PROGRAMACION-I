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

PRODUCTOS = cargar_productos_archivo()

#############################################
# CLIENTES#
# Lista de clientes. A diferencia de productos, cada cliente es un diccionario
# (mas facil de leer que una lista de listas, porque se accede por nombre de clave).
lista_clientes = [
    {
        "id": 1,
        "nombre": "JUAN PEREZ",
        "dni": "30111222",
        "telefono": "1145678901",
        "email": "juan.perez@gmail.com",
    },
    {
        "id": 2,
        "nombre": "ANA GOMEZ",
        "dni": "28555666",
        "telefono": "1156789012",
        "email": "ana.gomez@gmail.com",
    },
    {
        "id": 3,
        "nombre": "CARLOS FERNANDEZ",
        "dni": "32444555",
        "telefono": "1167890123",
        "email": "carlos.fernandez@yahoo.com",
    },
    {
        "id": 4,
        "nombre": "LUCIA MARTINEZ",
        "dni": "35222333",
        "telefono": "1178901234",
        "email": "lucia.martinez@hotmail.com",
    },
    {
        "id": 5,
        "nombre": "DIEGO RODRIGUEZ",
        "dni": "27888999",
        "telefono": "1189012345",
        "email": "diego.rodriguez@yahoo.com",
    },
    {
        "id": 6,
        "nombre": "SOFIA LOPEZ",
        "dni": "33666777",
        "telefono": "1190123456",
        "email": "sofia.lopez@hotmail.com",
    },
    {
        "id": 7,
        "nombre": "MARTIN SANCHEZ",
        "dni": "29999000",
        "telefono": "1101234567",
        "email": "martin.sanchez@gmail.com",
    },
    {
        "id": 8,
        "nombre": "VALENTINA TORRES",
        "dni": "31777888",
        "telefono": "1112345678",
        "email": "valentina.torres@hotmail.com",
    },
    {
        "id": 9,
        "nombre": "FEDERICO DIAZ",
        "dni": "26333444",
        "telefono": "1123456789",
        "email": "federico.diaz@yahoo.com",
    },
    {
        "id": 10,
        "nombre": "CAMILA ROMERO",
        "dni": "34111222",
        "telefono": "1134567890",
        "email": "camila.romero@gmail.com",
    },
]


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
