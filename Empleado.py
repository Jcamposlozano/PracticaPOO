
class Empleado:

    def __init__(self):
        self.nombre = None #String o texto
        self.apellidos = None #String o texto
        self.sueldo = None #float o decimal


 # get que para mostrar la variable
 # Set que es para modificar la    

    def getNombre(self):
        return self.nombre

    def getApellidos(self):
        return self.apellidos

    def getSueldo(self):
        return self.sueldo

    def setNombre(self, nombre:str):
        self.nombre = nombre

    def setApellido(self, apellidos:str):
        self.apellidos = apellidos

    def setSueldo(self, sueldo:float):
        self.sueldo = sueldo








