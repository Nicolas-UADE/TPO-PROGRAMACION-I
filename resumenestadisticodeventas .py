def resumen_estadistico(VENTAS):
    total_ventas = contar_ventas(VENTAS)
    promedio = promedio_ventas(VENTAS)
    mayor, menor = mayor_menor_venta(VENTAS)

    print("========== ESTADISTICAS ==========")
    print("Cantidad total de ventas:", total_ventas)
    print("Promedio general de ventas:", promedio)
    print("Mayor venta:", mayor)
    print("Menor venta:", menor)

    print("Cantidad de ventas de ALIMENTOS:",
          contar_ventas_categoria(VENTAS, "ALIMENTOS"))

    print("Cantidad de ventas de LIMPIEZA:",
          contar_ventas_categoria(VENTAS, "LIMPIEZA"))

    print("Cantidad de ventas de BEBIDAS:",
          contar_ventas_categoria(VENTAS, "BEBIDAS"))

    print("Cantidad de ventas de OTROS:",
          contar_ventas_categoria(VENTAS, "OTROS"))

    print("Porcentaje de ventas de ALIMENTOS:",
          porcentaje_ventas_categoria(VENTAS, "ALIMENTOS"))

    print("Porcentaje de ventas de LIMPIEZA:",
          porcentaje_ventas_categoria(VENTAS, "LIMPIEZA"))

    print("Porcentaje de ventas de BEBIDAS:",
          porcentaje_ventas_categoria(VENTAS, "BEBIDAS"))

    print("Porcentaje de ventas de OTROS:",
          porcentaje_ventas_categoria(VENTAS, "OTROS"))