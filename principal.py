from modulos.login import login
from modulos.menu import menu_principal

print("==========\nBIENVENIDO\n==========")
admin, lector = login()

menu_principal(admin, lector)
