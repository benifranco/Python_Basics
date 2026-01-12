from python_basico.ejemplos import saludar, sumar


def test_saludar():
    assert saludar("Python") == "Hola, Python!"


def test_sumar():
    assert sumar(2, 3) == 5
