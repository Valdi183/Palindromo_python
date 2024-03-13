"""
Este script, contiene un código para analizar cadenas de texto que introduce el usuario, de forma que si son un palíndromo
(se leen igual de dercha a izquierda que de izquierda a derecha), muestra True. Mostrará False en caso de que no lo sean
"""
# La clase Palindromo, es el algoritmo que analiza si una palabra lo es o no
class Palindromo:
    #Con el constructor se inicializa el atributo de la cadena (la cual almacena la cadena de carácteres)
    def __init__(self, cadena):
        self.cadena = cadena
    """
    En el método de esPalindromo, uno de los parametros que toma es el de cls además del de la cadena. Este parámetro hace referencia
    a la clase, (Palindromo en este caso) no a una instancia específica de esta (cuando esta instancia sea creada), es muy parecido al 
    uso de self. Esto permite que el método de clase pueda ser invocado sin tener que crear una instancia de la clase. El método puede 
    acceder a los atributos y métodos de la clase sin necesidad de una instancia específica
    """       
    @classmethod
    def esPalindromo(cls, cadena):
        # Convierte las letras a minúscula 
        cadena = cadena.lower()
        # Comprueba si la cadena es un palíndromo, si al poner los carácteres al reves, coincide con la cadena
        return cadena == cadena[::-1]

    # Este método, prueba si el atributo de la instancia (el atributo cadena, dependerá de lo que se ponga en la instancia al crearla) es un palíndromo
    def test(self):
        resultado = self.esPalindromo(self.cadena)
        print(self.cadena.upper())
        return resultado

"""
Estas son las instancias creadas, tanto a la clase, como del método test. Al crear una instancia de la clase, como ocurre con
p1 y p2. Lo que se muestra al ejecutar el código, es la palabra introducida como cadena en mayúsculas
"""
p1 = Palindromo("radar") # RADAR
print(p1.test())  # True


p2 = Palindromo("sonar") # SONAR
print(p2.test())  # False

print(Palindromo.esPalindromo('!@#$% %$#@!'))  # True

p3 = Palindromo("!##!")
print(p3.test())  # True