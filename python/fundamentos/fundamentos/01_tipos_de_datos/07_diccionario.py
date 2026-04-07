#Direccioner en python
estudiante = {"nombre": "Gonzalo", "curso": "Python"} #Notación Literal
#Imprime el nombre del estudiante
print(estudiante["nombre"]) #Imprime: Gonzalo

#Diccionario de países
paises = {} #Diccionario vacío
paises["MEX"] = "México" #Agregando valores
paises["COL"] = "Colombia"
paises["CHL"] = "Chile"
paises["PER"] = "Perú"
paises["ARG"] = "Argentina"
print(paises) 

estudiante["nombre"] = "Yoycer"
print(estudiante["nombre"]) #Imprime: Vicente

#condicion para buscar elemento e insertar si no existe
if "CRI" in paises: #Preguntamos si existe la clave en el diccionario
   print("¿Deseas reemplazar el valor?")
else: #No existe esa clave
   paises["CRI"] = "Costa Rica"
   
#elimina valores de diccionario
print(paises)
valor_removido = paises.pop("MEX") #Elimina el elemento y devuelve su valor
print(f"Valor removido: {valor_removido}")
del paises["COL"] #Elimina el elemento
print(paises) #Imprime: {'CHL': 'Chile'}

#Diccionario Pintor
pintor = {
   "nombre": "Frida Kahlo",
   "pais": "México",
   "fecha_nacimiento": "6 de julio de 1907"
}

#diccionario anidado
escuela = {
   "nombre": "Coding Dojo LATAM",
   "profesores": [
       {"nombre": "Alfredo", "apellido": "Salazar", "cursos": ["Python", "Java"]},
       {"nombre": "Valeria", "apellido": "Romero", "cursos": ["Fundamentos", "Java"]},
       {"nombre": "Marcelo", "apellido": "Argotti", "cursos":["MERN", "Python"]}
   ]
}