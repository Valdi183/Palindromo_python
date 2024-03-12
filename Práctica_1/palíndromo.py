"""
Este script, contiene un código para analizar cadenas de texto que introduce el usuario, de forma que si son un palíndromo
(se leen igual de dercha a izquierda que de izquierda a derecha), muestra True. Mostrará False en caso de que no lo sean
"""
# La clase Palindromo, es el algoritmo que analiza si una palabra lo es o no
class Palindromo:
    #Con el constructor se inicializa el atributo de la cadena (la cual almacena la cadena de carácteres)
    def __init__(self, cadena):
        self.cadena = cadena
            
    def esPalindromo(cls,cadena):
        # Elimina caracteres no alfanuméricos y convierte las letras a minúsculas
        cadena = ''.join(c for c in cadena if c.isalnum()).lower()
        # Comprueba si la cadena es un palíndromo, si al poner los carácteres al reves, coincide con la cadena
        return cadena == cadena[::-1]

    # Este método facilita 
    def test(self):
        resultado = self.esPalindromo(self.cadena)
        print(self.cadena.upper())
        return resultado


p1 = Palindromo("radar")
print(p1.test())  # True


p2 = Palindromo("sonar")
print(p2.test())  # False

p3 = Palindromo("sonar")
print(p3.test())  # False
