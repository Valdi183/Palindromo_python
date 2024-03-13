"""
La clase logger, tiene como objetivo escribir un mensaje dado como parámetro en un archivo cada vez que se llame al método log(mensaje).
"""

class Logger:
    """
    Aquí en el constrctor, aparecen todos los atributos inicializados necesarios para llevar acabo este proceso de log
    """
    def __init__(self, filename):
        self.filename = filename # Este es el nombre del archivo del registro
        self.log_count = 0 # Se inicilaiza el contador de registros
        self.file = open(self.filename, 'w') # Con esto, se crea el archivo con el nombre asignado en modo escritura (de ahí la w)
        self.file.write("--Start log--\n") # Escribe "--Start log--" en el archivo añadiendo un salto de linea "/n" para el siguiente texto
        self.file.close() # Cierra el archivo
    
    # Este método, se encarga de añadir un nuevo registro al archivo creado
    """
    Es importante abrir el archivo en modo adjuntar, ya que si se abre en modo escritura, cada vez que se tenga que iterar posteriromente,
    sobreescribirá el texto de la segunda linea (lo hará en la segunda linea, porque en el constructor, se ha hecho ya el cambio de linea).
    Además, de añadir los cambios de linea respectivos cada vez que se itere al escrinbir en el archivo, de esa forma, nos aseguramos que
    todo el tex.
    """
    def log(self, message):
        self.log_count += 1 #Incrementa el contador de registros de uno en uno
        self.file = open(self.filename, 'a') # Se vuelve a abrir el archivo pero esta vez en modo adjuntar
        self.file.write(message + '\n')  # Se escribe el mensaje (el numero de llamada) y se realiza el respectivo cambio de linea
        self.file.close() # Se cierra el archivo
    """
    El método del, actua cuando se destruye la instancia de logger. En este caso cuando se dejen de contar llamadas, si necesitamos que se
    escriba un mensaje al final (en este caso el de end log), este método lo hará aunque el usuario no llame explícitamente al método del 
    cierre del registro.
    """
    def __del__(self):
        self.file = open(self.filename, 'a')
        self.file.write("--End log: {} log(s)--".format(self.log_count)) 
        self.file.close()
"""
La clase Test utiliza la clase Logger para probar su funcionalidad, de ahí su nombre.
"""
class Test:
    """
    Con el constructor de la clase test, se inicializa una instancia de la clase logger con un nombre de arhivo de registro
    (el creado en el constructor de la clase Logger). De esta forma, cada instancia que se cree de esta nueva clase Test, tendrá
    su propio Logger asociado, ya que el objeto creado de test, se crea a partir de otro objeto creado con Logger.
    """
    def __init__(self):
        self.logger = Logger("log.txt")
    
    # Este método, permite registrar mensajes a través de Logger, asociada a la instancia de test
    def llamada(self, message):
        self.logger.log(message)

test = Test() # Se crea una instancia de test
"""
Con este bucle for, se itera todas las veces que se quiera sobre el registro de llamadas (en este caso al ser en un rango de 1 a 6
se iteran 5 veces). De esta forma se van escribiendo en el archivo el número de llamadas registradas, hasta que se termina de iterar
que es cuando se "destruye" el objeto, y actúa el método del explicado anteriormente
"""
for i in range(1, 6):
    if i == 1:
        test.llamada("Primera llamada")
    else:
        test.llamada("{}ª llamada".format(i))

# Con esto nos aseguramos de que el archivo se cierre correctamente, a pesar de haber creado el método 'del'
del test

# Prueba de la salida en el archivo log.txt en modo lectura (la r hace referencia al modo rectua, de read en inglés)
with open("log.txt", 'r') as file:
    print(file.read())