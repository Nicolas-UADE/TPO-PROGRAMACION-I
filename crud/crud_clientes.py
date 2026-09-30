from Funciones.funciones_uni import inicio, obtener_entero
from modulos import listas
from Funciones.funciones_clientes import (
    listado_clientes,
    baja_clientes,
    alta_clientes,
    modificar_clientes,
)


def clientes():
    """
    Menú principal del módulo de clientes.
    Muestra opciones según el rol: el admin tiene acceso completo y el usuario normal solo consulta.
    """
    seguir = True

    while seguir == True:
        texto = "CLIENTES"
        inicio(texto)

        # Si es Admin tiene permiso para altas, bajas, modificaciones y consultas
        if listas.ADMIN == True:
            ask = obtener_entero(
                "[0] ◀️  Retroceder\n[1] 📝 Listado de clientes\n[2] 🚫 Baja de clientes\n[3] ✅ Alta de clientes\n[4] ✏️  Modificar clientes\n.",
                0,
                4,
            )
            match ask:
                case 0:
                    seguir = False
                case 1:
                    listado_clientes()
                case 2:
                    baja_clientes()
                case 3:
                    alta_clientes()
                case 4:
                    modificar_clientes()
        else:
            # El usuario común solo puede consultar el listado
            ask = obtener_entero(
                "[0] ◀️  Retroceder\n[1] 📝 Listado de clientes\n.", 0, 1
            )
            match ask:
                case 0:
                    seguir = False
                case 1:
                    listado_clientes()
