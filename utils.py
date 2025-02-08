import re

def validar_expresion_matematica(expresion):
    """
    Valida que la expresión solo contenga dígitos, operadores básicos, paréntesis, puntos y espacios.
    """
    patron = r'^[\d+\-*/().\s]+$'
    return re.match(patron, expresion) is not None

def validar_texto(texto):
    """
    Valida que el texto no esté vacío (después de eliminar espacios).
    """
    return len(texto.strip()) > 0