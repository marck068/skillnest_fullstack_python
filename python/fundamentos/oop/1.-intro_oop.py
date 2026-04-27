#Creación de la clase usuario - Entidad
class Usuario:
    def __init__(self): #Constructor
        self.nombre = "Nariyoshi"
        self.apellido = "Miyagi"
        self.email = "miyagi@codingdojo.la"
        self.limite_credito = 30000
        self.saldo_pagar = 0

#Instancias de una clase
miyagi = Usuario()
daniel = Usuario()
marcelo = Usuario()

#Accedemos a los atributos de la instancia
print(miyagi.nombre)
print(miyagi.apellido)
print(miyagi.email)
print(miyagi.limite_credito)
print(miyagi.saldo_pagar)

#Nuevos valores asignados a atributos de la instancia
daniel.nombre = "Daniel"
daniel.apellido = "Larusso"
daniel.email = "daniel@gmail.com"
daniel.limite_credito = 100000
daniel.saldo_pagar = 300000

print(daniel.nombre)

#Valores a nueva instancia
marcelo.nombre = "Marcelo"
marcelo.apellido = "Ríos"
marcelo.email = "marcelo@gmail.com"
marcelo.limite_credito = 2000
marcelo.saldo_pagar = 1000

#Imprimir nombre de cada instancia
print(miyagi.nombre)
print(daniel.nombre)
print(marcelo.nombre)