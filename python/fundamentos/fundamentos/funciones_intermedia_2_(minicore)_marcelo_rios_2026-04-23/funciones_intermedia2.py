datos = [
   {"nombre": "Carlos", "puntaje": 80},
   {"nombre": "María", "puntaje": 95},
   {"nombre": "Pedro", "puntaje": 70}
]

# 1. Cambiar el puntaje de Pedro a 75
datos[2]["puntaje"] = 75
print(datos)
# 2. Crear función que imprima:
#    "Carlos obtuvo 80 puntos"
def carlo(lista):
    for i in lista:
        print(f"{i['nombre']} obtuvo {i['puntaje']}")
# 3. Crear función que reciba "nombre" o "puntaje" e imprima solo esos valores

