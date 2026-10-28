from Funciones.funciones_uni import inicio, obtener_entero, obtener_caracter
from modulos import listas
from Funciones.consultas_productos import (
    categorias_distintas,
    codigos_activos,
    nombres_activos,
    nombres_por_categoria,
)
from Funciones.funciones_productos import (
    listar_productos,
    baja_producto,
    alta_producto,
    modificar_producto,
)


def consultas_rapidas():
    print("\nCONSULTAS DE PRODUCTOS")
    opcion = obtener_entero(
        "[0] Volver\n[1] Categorias\n[2] Nombres por categoria\n"
        "[3] Codigos activos\n[4] Nombres activos\n.", 0, 4
    )

    if opcion == 1:
        for categoria in sorted(categorias_distintas()):
            print(categoria)
    elif opcion == 2:
        categoria = obtener_caracter("Ingrese categoria\n.").upper()
        nombres = nombres_por_categoria(categoria)
        if len(nombres) == 0:
            print("No hay productos en esa categoria.")
        else:
            for nombre in nombres:
                print(nombre)
    elif opcion == 3:
        for codigo in sorted(codigos_activos()):
            print(codigo)
    elif opcion == 4:
        for nombre in nombres_activos():
            print(nombre)


def productos():
    """Muestra el menu del modulo productos y sus opciones segun el tipo de usuario."""
    seguir = True

    while seguir == True:
        texto = "PRODUCTOS"
        inicio(texto)

        if listas.ADMIN == True:
            ask = obtener_entero(
                "[0] ◀️  Retroceder\n[1] 📝 Listado de producto\n[2] 🚫 Baja de producto\n[3] ✅ Alta de producto\n[4] ✏️  Modificar producto\n[5] Consultas rapidas\n.",
                0,
                5,
            )
            match ask:
                case 0:
                    seguir = False
                case 1:
                    listar_productos()
                case 2:
                    baja_producto()
                case 3:
                    alta_producto()
                case 4:
                    modificar_producto()
                case 5:
                    consultas_rapidas()
        else:
            ask = obtener_entero(
                "[0] ◀️  Retroceder\n[1] 📝 Listado de producto\n[2] Consultas rapidas\n.", 0, 2
            )
            match ask:
                case 0:
                    seguir = False
                case 1:
                    listar_productos()
                case 2:
                    consultas_rapidas()
