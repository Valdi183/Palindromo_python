"""
Este script, contiene un código para analizar palabras o frases que introduce el usuario, de forma que si son un palíndromo
(se leen igual de dercha a izquierda que de izquierda a derecha), muestra True. Mostrará False en caso de que no lo sean
"""
class Palindromo:
    def __init__(self, cadena):
        self.cadena = cadena

    @classmethod
    def esPalindromo(cls, cadena):
        # Eliminar caracteres no alfanuméricos y convertir a minúsculas
        cadena = ''.join(caracter.lower() for caracter in cadena if caracter.isalnum())
        # Comprobar si la cadena es un palíndromo
        return cadena == cadena[::-1]

    def test(self):
        return self.esPalindromo(self.cadena)

    def __del__(self):
        print(f"El atributo de la instancia en mayúsculas: {self.cadena.upper()}")

# Ejemplo de uso
cadena = input("Palabra a analizar:")
objeto_palindromo = Palindromo(cadena)
print("¿Es un palíndromo?", objeto_palindromo.test())
del objeto_palindromo