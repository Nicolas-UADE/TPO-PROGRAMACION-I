"""
Funciones estadísticas para las ventas.

Se espera que cada fila tenga el importe en la columna 3.
"""


def promedio_ventas(VENTAS):
	"""Devuelve el importe promedio de las ventas, o 0 si no hay ventas."""
	suma = 0

	for fila in VENTAS:
		suma += fila[3]

	if len(VENTAS) > 0:
		return suma / len(VENTAS)

	return 0
