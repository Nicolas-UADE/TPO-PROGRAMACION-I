import random

IDS_PRODUCTOS = [
    482719,
    935164,
    271853,
    604927,
    158436,
    793205,
    326581,
    841672,
    519348,
    267914
]

def generar_lista_ids(): #Llamar a la funcion en AGREGAR PRODUCTOS

     nuevo_id=random.randint(100000,1000000)

     while nuevo_id in IDS_PRODUCTOS == True:
          nuevo_id=random.randint(100000,1000000)
     IDS_PRODUCTOS.append(nuevo_id)

     return IDS_PRODUCTOS
#Verificar que no este ya asociado ese ID, con un while y una busqueda secuencial. 
matriz_resumen = []

#for i in range(len(PRODUCTOS)):
#     matriz_resumen.append([lista_ids[i], PRODUCTOS[i], CATEGORIA[i], PRECIOS[i], DESCUENTO[i], STOCK[i]])

#print("ID       PRODUCTO       CATEGORIA      PRECIO     DESC (%)   STOCK")
#print("------------------------------------------------------------------")
#for i in range(len(matriz_resumen)):
#    print(f"ID: {matriz_resumen[i][0]} | Prod: {matriz_resumen[i][1]} | Cat: {matriz_resumen[i][2]} | Precio: ${matriz_resumen[i][3]} | Desc: {matriz_resumen[i][4]}% | Stock: {matriz_resumen[i][5]}")

print(generar_lista_ids())