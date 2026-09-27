from login import login
from menu import menu_principal

print("==========\nBIENVENIDO\n==========")
admin, lector = login()

menu_principal(admin, lector)