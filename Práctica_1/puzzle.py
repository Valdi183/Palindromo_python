class A:
    def z(self):  # Este es un método de la clase A
        return self 

    def y(self, t):  # Método y de la clase A que recibe un argumento t
        return len(t)  # El método almacena la longitud de t 


a = A()  # Se crea una instancia de la clase A, por tanto ahora a es un objeto
y = a.z  # Asignamos el método z del objeto creado anteriormente (a) a la variable y
print(y())  # Llama al método z a través de y y lo ejecuta para que muestre el objeto a

aa = A()  # Creamos otro objeto de la clase A, esta vez llamado aa
print(aa is A())  # Esto muestra en pantalla false, ya que tantro aa como A(), son dos instancias diferentes 

z = aa.y  # Asignamos el método y del objeto aa a la variable z
print(z(()))  # Llama al método y a través de z cuyo argumento es una tupla. Al estar vacía, se mostrará en pantalla un 0
"""
En el siguiente print, se muestra un 1 en pantalla, ya que se está llamando a el método y de la clase A, que nos devuelve la longitud
del margumento t. En este caso, como argumento, se le está pasando una tupla que contiene el objeto a. Por tanto, al printear la llamada
del metodo, se nos mostrará la longitud del argumento, la tupla en este caso cuya longitud es 1
"""
print(A.y(aa, (a,)))

"""
En este caso, en ved de llamar al método desde la clase, se llama desde el objeto creado anteriormente 'aa', y se le pasa como argumento
una tupla, esta vez con tres elementos, por tantro en pantalla mostrará un 3
"""
print(aa.y((z, 1, 'z')))