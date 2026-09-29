from modulos import listas
from Funciones.funciones_uni import inicio,obtener_entero
from Funciones.funciones_ventas import listar_ventas,baja_venta,alta_venta,modificar_venta,menu_estadisticas_ventas


def ventas():
    """Menu principal del modulo ventas. Cambia segun si el usuario es admin o no."""
    seguir = True

    while seguir == True:
        texto = "VENTAS"
        inicio(texto)

        if listas.ADMIN == True:
            # Admin ve todas las opciones: listar, dar de baja, dar de alta, modificar y estadisticas.
            opcion = obtener_entero(
                "[0] ◀️  Retroceder\n[1] 📝 Listado de ventas\n[2] 🚫 Baja de venta\n[3] ✅ Alta de venta\n[4] ✏️  Modificar venta\n[5] 📈 Estadisticas\n.",
                0,
                5,
            )

            match opcion:
                case 0:
                    seguir = False
                case 1:
                    listar_ventas()
                case 2:
                    baja_venta()
                case 3:
                    alta_venta()
                case 4:
                    modificar_venta()
                case 5:
                    menu_estadisticas_ventas()
        else:
            # Usuario normal solo puede ver el listado y las estadisticas.
            opcion = obtener_entero(
                "[0] ◀️  Retroceder\n[1] 📝 Listado de ventas\n[2] 📈 Estadisticas\n.", 0, 2
            )

            match opcion:
                case 0:
                    seguir = False
                case 1:
                    listar_ventas()
                case 2:
                    menu_estadisticas_ventas()


