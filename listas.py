INGRESO = False
ADMIN = False
LECTOR = False
ELIMINADO = -1
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

PRODUCTOS_CODIGO = 0
PRODUCTOS_NOMBRE = 1
PRODUCTOS_CATEGORIA = 2
PRODUCTOS_PRECIO = 3
PRODUCTOS_STOCK = 4
PRODUCTOS_DESCUENTO = 5


PRODUCTOS = [
    [482719, "PILAS", "OTROS", 1500, 25, 5],
    [935164, "ARROZ", "ALIMENTOS", 1800, 18, 0],
    [271853, "ATUN", "ALIMENTOS", 1200, 32, 10],
    [604927, "ACEITE", "ALIMENTOS", 3500, 14, 13],
    [158436, "AZUCAR", "ALIMENTOS", 1300, 27, 9],
    [793205, "YERBA", "ALIMENTOS", 4200, 12, 20],
    [326581, "GALLETITAS", "ALIMENTOS", 1600, 20, 0],
    [841672, "CAFE", "BEBIDAS", 5500, 9, 0],
    [519348, "JABON", "LIMPIEZA", 1400, 35, 5],
    [267914, "PEPSI", "BEBIDAS", 2800, 16, 15],
]
productos_nombre_individual = [
    "PILAS",
    "ARROZ",
    "ATUN",
    "ACEITE",
    "AZUCAR",
    "YERBA",
    "GALLETITAS",
    "CAFE",
    "JABON",
    "PEPSI",
]

productos_id_individual = [
    482719,
    935164,
    271853,
    604927,
    158436,
    793205,
    326581,
    841672,
    519348,
    267914,
]
descuentos_individual = [5, 0, 10, 13, 9, 20, 0, 0, 5, 15]


#############################################
# CLIENTES#
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





#VENTAS

VENTAS_ID = 0
VENTAS_CLIENTE = 1
VENTAS_PRODUCTO = 2
VENTAS_CATEGORIA = 3
VENTAS_FECHA = 4
VENTAS_CANTIDAD = 5
VENTAS_PRECIO_UNITARIO = 6
VENTAS_IMPORTE = 7


VENTAS = [
    [100001, 1, 935164, "ALIMENTOS", "01/09/2026", 2, 1800, 3600],
    [100001, 1, 267914, "BEBIDAS", "01/09/2026", 1, 2380, 2380],
    [100002, 2, 519348, "LIMPIEZA", "02/09/2026", 2, 1330, 2660],
    [100003, 3, 271853, "ALIMENTOS", "03/09/2026", 2, 1080, 2160],
    [100003, 3, 482719, "OTROS", "03/09/2026", 1, 1425, 1425],
    [100004, 4, 841672, "BEBIDAS", "04/09/2026", 1, 5500, 5500],
    [100005, 5, 604927, "ALIMENTOS", "05/09/2026", 1, 3045, 3045],
    [100005, 5, 158436, "ALIMENTOS", "05/09/2026", 2, 1183, 2366],
    [100006, 6, 793205, "ALIMENTOS", "06/09/2026", 1, 3360, 3360],
    [100007, 7, 326581, "ALIMENTOS", "07/09/2026", 3, 1600, 4800],
    [100008, 8, 267914, "BEBIDAS", "08/09/2026", 2, 2380, 4760],
    [100009, 9, 519348, "LIMPIEZA", "09/09/2026", 1, 1330, 1330],
    [100010, 10, 482719, "OTROS", "10/09/2026", 2, 1425, 2850]
]