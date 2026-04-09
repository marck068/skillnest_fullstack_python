#I. Interacción y Condicionales (Básico)

# 1. Números Pares Dinámicos
# Desarrolla un programa que solicite al usuario cuántos números pares desea ver ($n$). 
# El programa debe imprimir los primeros $n$ números pares positivos.
def numerosDinamicos():
    n = int(input("¿Cuantos números deseas ver?: "))
    pares = []
    for i in range (1, ( n * 2 ) + 1):
        if i % 2 == 0:
            pares.append(i)
    print(f"Mostrando pares: {pares}")
    
# 2. Verificador de Edad y Acceso
# Pide al usuario su año de nacimiento. Calcula su edad y muestra si es mayor de edad (18+). 
# Si tiene menos de 18, indica cuántos años le faltan para la mayoría de edad.
def verificador_edad():
    campo = input("Ingrese su año de nacimiento: ")
    edad = 2026 - int(campo)
    if campo == "":
        print("Error")
    elif edad >= 18:
        print(f"Tienes acceso ya que tu edad es: {edad}")
    elif edad > 0 and edad < 18:
        print(f"No tiene acceso: te faltan {18 - edad} años.")
    else:
        print("No tiene Acceso")
verificador_edad()

# 3. Calculadora de Descuentos
# Solicita el precio de un producto y la cantidad comprada.
# Si el total supera los $100, aplica un 15% de descuento. Muestra el subtotal, 
# el descuento aplicado y el total final.
def aplicarDescuento():
    precio = float(input("Ingrese el precio del producto: "))
    cantidad = int(input("Ingrese la cantidad comprada: "))
    producto = precio * cantidad
    if producto > 100:
        descuento = producto * 0.15
    else:
        descuento = 0
        total = producto
        print(f"Subtotal es: ${producto}. El descuento aplicado es: {descuento}. Y el total del producto es: {total}")

# 4. Clasificador de Números
# Pide un número al usuario e indica si es: Positivo-Par, Positivo-Impar, Negativo-Par,
# Negativo-Impar o Cero.
def clasificadorNum():
    num = int(input("Ingresar un número: "))
    if num > 0:
        if num % 2 == 0:
            print("Positivo-Par")
        elif num % 2 == 1:
            print("Positivo-Impar")
    elif num < 0:
        if num % 2 == 0:
            print("Negativo-Par")
        elif num % 2 == 1:
            print("Negativo-Impar")
    else:
        print("Es 0")


# II. Iteraciones y Bucles (Intermedio)

# 5. Tabla de Multiplicar Personalizada
# Solicita un número entero y muestra su tabla de multiplicar del 1 al 12, pero solo muestra 
# los resultados que sean múltiplos de 3.
def tablaMultiplicar():
    num = int(input("Ingresar número a trabajar: "))
    for i in range (1, 13):
        resultado = num + i
        if resultado % 3 == 0:
            print(f"Del {num} solo estos números son divisibles por 3: {resultado}")


# 6. Sumatoria con Centinela
# Crea un programa que pida números continuamente y los sume. 
# El ciclo debe terminar cuando el usuario ingrese un número negativo. Al final, muestra la suma total 
# (sin incluir el negativo).



# 7. Contador de Vocales
# Pide al usuario una frase o palabra.
# Utiliza un bucle para recorrer la cadena y contar cuántas vocales tiene en total.



# 8. Validación de Contraseña
# Define una contraseña en una variable. Pide al usuario que la intente adivinar.
# Tienes un máximo de 3 intentos; si falla los 3, bloquea el acceso.



# III. Manejo de Arreglos / Listas (Avanzado)

# 9. Registro de Nombres
# Crea un arreglo vacío. Pide al usuario que ingrese 5 nombres.
# Guárdalos en el arreglo y, al final, imprímelos en orden inverso al que fueron ingresados.



# 10. Promedio de Notas
# Solicita al usuario cuántas notas desea ingresar. Almacena cada nota en un arreglo.
# Al finalizar, calcula y muestra el promedio, la nota más alta y la más baja.



# 11. Filtro de Arreglos
# Dado un arreglo de números generado por el usuario, crea un nuevo arreglo que contenga 
# solo los números que sean mayores a 50. Muestra ambos arreglos.



# 12. Buscador de Elementos
# Crea una lista de 10 ciudades. 
# Pide al usuario que ingrese el nombre de una ciudad y el programa debe decir si la ciudad se
# encuentra en la lista y en qué índice (posición) está.



# IV. Retos de Lógica Combinada

# 13. Simulación de Inventario
# Crea dos arreglos: uno para nombres_productos y otro para precios. 
# Permite al usuario ingresar 3 productos con sus precios. Luego,
# muestra una lista formateada: Producto: [Nombre] - Precio: $[Valor].



# 14. Generador de Lista de Compras
# Usa un bucle while para que el usuario agregue artículos a una lista de compras. El proceso termina 
# cuando el usuario escribe "terminar". Al final, muestra la lista ordenada alfabéticamente.



# 15. Análisis de Temperaturas
# Solicita las temperaturas de los 7 días de la semana y guárdalas en un arreglo. Muestra:
# El promedio semanal.
# Cuántos días la temperatura fue superior a 25 grados.
# El día con la temperatura más baja (asumiendo que el índice 0 es Lunes).


continuar = True
while continuar:
    print("\n --- ejercicio 1 Python---")
    print(" ---1 ejercicio 1 ---")
    print(" ---2 ejercicio 2 ---")    
    print(" ---3 ejercicio 3 ---")
    print(" ---4 ejercicio 4 ---")
    print(" ---5 ejercicio 5 ---")
    print(" ---6 ejercicio 6 ---")
    print(" ---7 ejercicio 7 ---")
    print(" ---8 ejercicio 8 ---")
    print(" ---9 ejercicio 9 ---")
    print(" ---10 ejercicio 10 ---")
    print(" ---11 ejercicio 11 ---")
    print(" ---12 ejercicio 12 ---")
    print(" ---13 ejercicio 13 ---")
    print(" ---14 ejercicio 14 ---")
    print(" ---15 ejercicio 15 ---")
    opcion = input("\n---- Elige una opción (1-15) o '(0 para salir)= ")
    if opcion == "1":
        print("\nEjecutando ejercicio 1: ")
        print(numerosDinamicos())
    elif opcion == "2":
        print("\nEjecutando ejercicio 2: ")
        print(verificador_edad())
    elif opcion == "3":
        print("\nEjecutando ejercicio 3: ")
        print(aplicarDescuento())
    elif opcion == "4":
        print("\nEjecutando ejercicio 4: ")
        print(clasificadorNum())
    elif opcion == "5":
        print("\nEjecutando ejercicio 5: ")
        print(tablaMultiplicar())
    elif opcion == "6":
        print("\nEjecutando ejercicio 6: ")
        print()
    elif opcion == "7":
        print("\nEjecutando ejercicio 7: ")
        print()
    elif opcion == "8":
        print("\nEjecutando ejercicio 8: ")
        print()
    elif opcion == "9":
        print("\nEjecutando ejercicio 9: ")
        print()
    elif opcion == "10":
        print("\nEjecutando ejercicio 10: ")
        print()
    elif opcion == "11":
        print("\nEjecutando ejercicio 11: ")
        print()
    elif opcion == "12":
        print("\nEjecutando ejercicio 12: ")
        print()
    elif opcion == "13":
        print("\nEjecutando ejercicio 13: ")
        print()
    elif opcion == "14":
        print("\nEjecutando ejercicio 14: ")
        print()
    elif opcion == "15":
        print("\nEjecutando ejercicio 15: ")
        print()

    elif opcion == "0":
        print("Saliendo...") 
        continuar = False
    else:
        print("Opción no válida, intenta otra vez")