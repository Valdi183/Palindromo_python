"""
Este script, contiene un código para analizar cadenas de texto que introduce el usuario, de forma que si son un palíndromo
(se leen igual de dercha a izquierda que de izquierda a derecha), muestra True. Mostrará False en caso de que no lo sean
"""
1
class Palindromo:
    def __init__(self, cadena):
        self.cadena = cadena
            
    def esPalindromo(cls, cadena):
        # Eliminar caracteres no alfanuméricos y convertir a minúsculas
        cadena = ''.join(caracter.lower() for caracter in cadena if caracter.isalnum())
        # Comprobar si la cadena es un palíndromo
        return cadena == cadena[::-1]

    def test(self):
        return self.esPalindromo(self.cadena)

    def __del__(self):
        print(self.cadena.upper())


p1 = Palindromo("radar")
print(p1.test())  # True


p2 = Palindromo("sonar")
print(p2.test())  # False

p3 = Palindromo("sonar")
print(p3.test())  # False