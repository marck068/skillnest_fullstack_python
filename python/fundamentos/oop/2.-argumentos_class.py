#➡️ Pasar argumentos 
#Para poder personalizar nuestras instancia vamos a pasar algunos 
#argumentos al método __init__ y que de esta manera podamos asignarle
#a los atributos los valores correspondientes.

class Usuario:
   def __init__(self, nombre, apellido, email, limite_credito, saldo_pagar):
       self.nombre = nombre
       self.apellido = apellido
       self.email = email
       self.limite_credito = limite_credito
       self.saldo_pagar = saldo_pagar

#Creación de instancias
miyagi = Usuario("Nariyoshi", "Miyagi", "miyagi@codingdojo.la", 30000, 0)
daniel = Usuario("Daniel", "Larusso", "daniel@codingdojo.la", 4000, 30)
marcelo = Usuario("Marcelo", "Ríos", "marcelo@gmail.com", 3000, 200)

#Imprimimos valores
print(miyagi.nombre) #Imprime: Nariyoshi
print(daniel.nombre) #Imprime: Daniel


#-----------------
#--- Tarea ráipda
'''
Crear una clase Estudiante, y asignarle los siguientes atributos:
(rut, nombre, apellido, especialidad, fecha_nac)
- Crear 3 instancias para la clase con distintos estudiantes.
- Imprimir el nombre y apellido concatenado + especialidad.
'''

class Estudiante:
   def __init__(self, rut, nombre, apellido, especialidad, fecha_nac):
       self.rut = rut
       self.nombre = nombre
       self.apellido = apellido
       self.especialidad = especialidad
       self.fecha_nac = fecha_nac
       

marcelo = Estudiante("23.009.064-5", "Marcelo", "Ríos", "Programación", 2/5/2009)
yoycer = Estudiante("28.981.636-4", "Yoycer", "Garcia", "Programación", 11/10/2007)
daniel = Estudiante("28.493.693-0", "Daniel", "Jimenez", "Programación", 16/1/2009)

print(marcelo.nombre + " " + marcelo.apellido + " Especialidad: " + marcelo.especialidad)
print(yoycer.nombre + " " + yoycer.apellido + " Especialidad: " + yoycer.especialidad)
print(daniel.nombre + " " + daniel.apellido + " Especialidad: " + daniel.especialidad)
