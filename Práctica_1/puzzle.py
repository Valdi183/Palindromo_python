class A:
    def z(self):  # Método z de la clase A
        return self

    def y(self, t):  # Método y de la clase A que recibe un argumento t
        return len(t)  # Devuelve la longitud de t


a = A()  # Instanciamos un objeto de la clase A y lo asignamos a la variable 'a'
y = a.z  # Asignamos el método 'z' del objeto 'a' a la variable 'y'
print(y())  # Llamamos al método 'z' a través de 'y' y lo ejecutamos (debería imprimir el objeto 'a')

aa = A()  # Instanciamos otro objeto de la clase A y lo asignamos a la variable 'aa'
print(aa is A())  # Comprobamos si 'aa' es igual a un nuevo objeto de la clase A (debería imprimir False)

z = aa.y  # Asignamos el método 'y' del objeto 'aa' a la variable 'z'
print(z(()))  # Llamamos al método 'y' a través de 'z' con una tupla vacía como argumento (debería imprimir 0)

print(A.y(aa, (a,)))  # Llamamos al método 'y' de la clase A pasando 'aa' como primer argumento y una tupla que contiene 'a' como segundo argumento (debería imprimir 1)

print(aa.y((z, 1, 'z')))  # Llamamos al método 'y' del objeto 'aa' con una tupla que contiene 'z', 1 y 'z' como argumentos (debería imprimir 3)