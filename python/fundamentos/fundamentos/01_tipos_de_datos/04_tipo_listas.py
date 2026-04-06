'''Actividad Gestor de inventario
1.- Creación: Crear una lista llamada inventario que contenga los siguientes
articulos: "laptop", "ratón", "monitor", "cable hdmi" '''

inventario = ["laptop", "teclado" ,"ratón", "monitor", "cable hdmi"]

''' 2.- Expansíon: Utiliza el método correspondiente para agregar "impresora"
y "teclado" al final de la lista '''

inventario.append("inpresora")

''' 3.- Conteo: Utiliza la funcion integrada para mostrar cuantos elementos
totales hay en la lista. '''

print(len(inventario))

''' 4.- Acceso y modificación: Modifica "teclado" po "teclado mecánico" '''

inventario[1] = "teclado mecanico"

''' 5.- slicing: Crea una nueva lista llamada "promoción" debe contener solo los 3 primeros elementos de la lista
"inventario", solo los primeros 3 elementos de la lista "inventario". '''

promocion = inventario[0:3]

''' 6.- Mostrar la lista de inventario ordenado alfabeticamente. '''

inventario.sort()
print(inventario)

''' 7.- Elimina el último elemento de la lista de inventario mostrando el elemento eliminado y la lista final. '''

elemento_eliminado = inventario.pop()
print("Elemento eliminado", elemento_eliminado)