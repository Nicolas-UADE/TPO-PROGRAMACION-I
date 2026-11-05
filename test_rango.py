from Funciones.funciones_uni import rango


def test_rango_dentro():
    assert rango(1, 10, 5) == True


def test_rango_fuera():
    assert rango(1, 10, 15) == False


def test_rango_limites():
    assert rango(1, 10, 1) == True
    assert rango(1, 10, 10) == True
