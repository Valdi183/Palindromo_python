class Logger:
    def __init__(self, filename):
        self.filename = filename
        self.log_count = 0
        self.file = open(self.filename, 'w')
        self.file.write("--Start log--\n")
        self.file.close()
    
    def log(self, message):
        self.log_count += 1
        self.file = open(self.filename, 'a')
        self.file.write(message + '\n')
        self.file.close()
    
    def __del__(self):
        self.file = open(self.filename, 'a')
        self.file.write("--End log: {} log(s)--".format(self.log_count))
        self.file.close()

class Test:
    def __init__(self):
        self.logger = Logger("log.txt")
    
    def llamada(self, message):
        self.logger.log(message)

test = Test()
for i in range(1, 6):
    if i == 1:
        test.llamada("Primera llamada")
    else:
        test.llamada("{}ª llamada".format(i))

# Prueba de la salida en el archivo log.txt
with open("log.txt", 'r') as file:
    print(file.read())