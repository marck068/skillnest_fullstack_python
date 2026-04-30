"""
Actividad: Desarrollo de funciones en Python con distintos tipos de datos
Objetivo de aprendizaje
Desarrollar programas en Python utilizando funciones, estructuras de control, listas, diccionarios
y distintos tipos de datos, aplicando lógica de programación para la resolución de problemas 
mediante el uso de menús interactivos y validación de información.

Instrucciones generales
Deberá desarrollar un programa en Python que contenga un menú interactivo utilizando la 
estructura while, permitiendo al usuario seleccionar distintas opciones para ejecutar funciones previamente definidas.
Cada opción del menú deberá llamar a una función diferente, la cual resolverá una situación
específica utilizando distintos tipos de datos como enteros, decimales, cadenas de texto, listas y diccionarios.
En aquellos casos donde sea necesario, deberá solicitar información al usuario mediante input().
Además, se deberá trabajar con arreglos (listas) para recorrer información utilizando ciclos for,
junto con estructuras condicionales como if, elif y else.
El programa deberá incluir una opción para salir correctamente del sistema.
"""

#Ejercicios a desarrollar
#Su programa deberá considerar las siguientes funciones:

# 1.-Crear una función que reciba una lista de números enteros y muestre cuál es el número mayor y cuál es el menor.
def numeroMayorMenor(lista):
    menor = min(lista)
    mayor = max(lista)
    print(f"El número mayor es {mayor}nEl número menor es: {menor}")
def ejercicio1():
    limit = int(input("Ingresa un límite de valores: "))
    listaNum = []
    i = i
    while i <= limit:
        num = input("Ingresa un numero entero o decimal (con punto): ")
        listaNum.append(num)
        i+=1
    numeroMayorMenor(listaNum)

# 2.-Crear una función que reciba una cadena de texto y cuente cuántas vocales contiene.
def es_vocal(letra):
    vocales = "aeiouAEIOU"
    return letra in vocales


def contar_vocales(texto):
    contador = 0

    for letra in texto:
        if es_vocal(letra):
            contador += 1

    print(f"La cadena contiene {contador} vocales.")


def ejercicio_contar_vocales():
    texto = input("Ingrese una cadena de texto: ")
    contar_vocales(texto)

# 3.-Crear una función que reciba una lista de nombres y muestre únicamente aquellos que tengan más de 5 letras.
def filtrar(lista):
    resultado = []
    for nombre in lista:
        if len(nombre) > 5:
            resultado.append(nombre)
    return resultado

def mostrar():
    nombres = []
    cantidad = int(input("¿Cuántos nombres quieres ingresar? "))
    for i in range(cantidad):
        nombre = input("Ingresa un nombre: ")
        print(f"{nombre} agregado con exito a la lista.")
        nombres.append(nombre)
    for nombre in filtrar(nombres):
        print("Los nombres con más de 5 letras son: ")
        print(nombre)
mostrar()

# 4.-Crear una función que reciba una lista de notas (números decimales), calcule el promedio e indique si el
#estudiante aprueba (promedio mayor o igual a 4.0).



# 5.-Crear una función que reciba una lista de precios de productos y aplique un descuento del 10%, mostrando el
#valor original y el nuevo valor.



# 6.-Crear una función que reciba un número entero y determine si es par o impar.



# 7.-Crear una función que reciba una lista de edades y muestre cuántas personas son mayores de edad
#(18 años o más).



# 8.-Crear una función que reciba una lista de palabras y permita buscar cuántas veces aparece una palabra
#específica ingresada por el usuario.



# 9.-Crear una función que reciba una lista de números y genere una nueva lista que contenga únicamente los
#números positivos.



# 10.-Crear una función que reciba una lista de productos (utilizando diccionarios con nombre y stock)
#y muestre cuáles tienen un stock menor a 5 unidades.



"""
Requisitos obligatorios
Su trabajo debe cumplir con lo siguiente:
Uso de funciones con parámetros
Uso de menú con ciclo while
Uso de input() para solicitar datos
Uso de listas (arreglos)
Uso de diccionarios
Uso de ciclos for
Uso de estructuras condicionales (if, elif, else)
Código ordenado, comentado y correctamente indentado
Opción de salida del programa (0. Salir)
"""

#Forma de entrega
#Debe subir un único archivo .py correctamente identificado con su nombre y apellido.
#Ejemplo:
#apellido_nombre_funciones.py

#Criterios de evaluación
#Se evaluará:
#Correcto funcionamiento de las funciones
#Aplicación adecuada de estructuras de control
#Uso correcto de listas y diccionarios
#Lógica de programación
#Orden, claridad e indentación del código
#Cumplimiento de todos los requerimientos solicitados