"""
En este archivo pondrás en práctica el uso de bucles 'for' en Python,
usando ejemplos inspirados en videojuegos y situaciones atractivas.
"""

# 1. Generador de niveles
# Imprime todos los niveles del 0 al 100 (incluyendo el 100).
# (Tu código aquí)
for i in range(101):
    print(i)
    
print("\n")

# 2. Potenciadores de energía (Múltiplos de 2)
# Imprime los números múltiplos de 2 desde 2 hasta 500 (incluyendo el 500).
# (Tu código aquí)
for i in range(251):
    i *= 2
    print(i)
    
print("\n")

# 3. Trampa de emojis
# Recorre los puntos del 1 al 100.
# - Si el número es divisible por 5, imprime ""
# - Si es divisible por 10, imprime ""
# ¡Cuidado con la prioridad en tus condicionales!
# (Tu código aquí)
punt = 1
for punt in range(5, 100):
    if punt % 10 == 0:
        print(f"Puntaje: {str(punt)}")
    elif punt % 5 == 0:
        print(f"Puntaje: {str(punt)}")

print("\n")

# 4. Suma colosal
# Suma todos los números pares del 0 al 500,000 e imprime la suma total.
# (Tu código aquí)

sumaTotal = 0
for i in range(0, 500001, 2):
    sumaTotal += i
print(f"Suma total: {sumaTotal}")

print("\n")

# 5. Retroceso temporal
# Desde 2024, retrocede de 3 en 3 hasta 0 o menos.
# Imprime cada valor en la cuenta regresiva.
# (Tu código aquí)

for year in range(2024, -1, -3):
    print(year)
    
print("\n")

# 6. Contador dinámico
# Declara las variables inicio, fin, y salto (por ejemplo: inicio=3, fin=10, salto=2).
# Imprime los números en el rango que sean múltiplos de 'salto'.
# (Tu código aquí)

# Ejemplo: si inicio = 3, fin = 10, y salto = 2
# Se imprimiría: 4, 6, 8, 10

inicio = 3
fin = 10
salto = 2
for i in range(inicio, fin +1):
    if i % salto == 0:
        print(i)
