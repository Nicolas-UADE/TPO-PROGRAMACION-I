# [ID_VENTA, ID_PRODUCTO, CATEGORIA, CANTIDAD, IMPORTE]

# CATEGORIA:( PARA ACORDARSE)
# 1 = Alimentos
# 2 = Limpieza
# 3 = Bebidas
# 4 = Otros



def resumen_estadistico(VENTAS):

    total_ventas = contar_ventas(VENTAS)
    promedio = promedio_ventas(VENTAS)
    mayor, menor = mayor_menor_venta(VENTAS)

    cant_alimentos = contar_ventas_categoria(VENTAS, 1)
    cant_limpieza = contar_ventas_categoria(VENTAS, 2)
    cant_bebidas = contar_ventas_categoria(VENTAS, 3)
    cant_otros = contar_ventas_categoria(VENTAS, 4)

    pct_alimentos = porcentaje_ventas_categoria(VENTAS, 1)
    pct_limpieza = porcentaje_ventas_categoria(VENTAS, 2)
    pct_bebidas = porcentaje_ventas_categoria(VENTAS, 3)
    pct_otros = porcentaje_ventas_categoria(VENTAS, 4)

    print(f"""========== ESTADISTICAS ==========
Cantidad total de ventas: {total_ventas}
Promedio general de ventas: {promedio}
Mayor venta: {mayor}
Menor venta: {menor}

Cantidad de ventas de ALIMENTOS: {cant_alimentos}
Cantidad de ventas de LIMPIEZA: {cant_limpieza}
Cantidad de ventas de BEBIDAS: {cant_bebidas}
Cantidad de ventas de OTROS: {cant_otros}

Porcentaje de ventas de ALIMENTOS: {pct_alimentos}%
Porcentaje de ventas de LIMPIEZA: {pct_limpieza}%
Porcentaje de ventas de BEBIDAS: {pct_bebidas}%
Porcentaje de ventas de OTROS: {pct_otros}%
==================================""")