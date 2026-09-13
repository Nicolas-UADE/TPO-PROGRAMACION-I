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
