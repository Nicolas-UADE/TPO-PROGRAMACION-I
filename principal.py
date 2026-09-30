from modulos.login import login
from modulos.menu import menu_principal
from Funciones.funciones_uni import inicio

texto = "LOGIN"
inicio(texto)
admin, lector = login()

menu_principal(admin, lector)
