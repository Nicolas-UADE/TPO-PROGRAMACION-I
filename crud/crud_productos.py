from Funciones.funciones_uni import inicio,obtener_entero
import listas
from Funciones.funciones_productos import listar_productos,baja_producto,alta_producto,modificar_producto

def productos():
    """Muestra el menu del modulo productos y sus opciones segun el tipo de usuario."""
    seguir = True

    while seguir == True:
        texto = "PRODUCTOS"
        inicio(texto)

        if listas.ADMIN == True:
            ask = obtener_entero(
                "[0] ◀️  Retroceder\n[1] 📝 Listado de producto\n[2] 🚫 Baja de producto\n[3] ✅ Alta de producto\n[4] ✏️  Modificar producto\n.",
                0,
                4,
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
        else:
            ask = obtener_entero("[0] ◀️  Retroceder\n[1] 📝 Listado de producto\n.", 0, 1)
            match ask:
                case 0:
                    seguir = False
                case 1:
                    listar_productos()


