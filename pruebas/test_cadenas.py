from Funciones.funciones_uni import recortar_texto


def test_recortar_texto_corto():
    assert recortar_texto("PAN", 8) == "PAN"


def test_recortar_texto_largo():
    assert recortar_texto("GALLETITAS", 8) == "GALLE..."


def test_recortar_texto_con_espacios():
    assert recortar_texto("  LECHE  ", 8) == "LECHE"
