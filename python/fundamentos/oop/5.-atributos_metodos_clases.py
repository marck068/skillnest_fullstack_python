#Atributos, métodos de clase, métodos estáticos

#DEFINICION DE LA CLASE
class Estudiante:
    #Atributo de clase
    colegio = "Liceo Vate Vicente Huidobro"
    #Lista en donde esten todos los estudiantes
    estudiantes = []

    #Método CONSTRUCTOR
    def __init__(self, nombre, nota):
        #Atributos de instancias
        self.nombre = nombre
        self.nota = nota
        
        #Agregar elementos a la lista Estudiante
        Estudiante.estudiantes.append(self)
        
    #Método de instancia
    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Nota: {self.nota}")


## Función repaso.
## Crear una función que valide usuario y contraseña

def validador(user, password):
    if user == "matias123" and password == "matias321":
        print(f"Bienvenido, {user}!")
        return True
    else:
        print("Acceso Denegado")
        return False

def enviarDatos():
    username = input("Ingrese su nombre usuario: ")
    password = input("Ingrese su contraseña: ")
    validador(username, password)
    
enviarDatos()