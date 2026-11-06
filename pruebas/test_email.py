from Funciones.funciones_uni import validar_email


def test_validar_email_correcto():
    assert validar_email("juan@gmail.com") == True


def test_validar_email_sin_arroba():
    assert validar_email("juangmail.com") == False


def test_validar_email_con_espacios():
    assert validar_email("juan perez@gmail.com") == False
