#Ejercicio 1: Ranking de puntajes de un torneo de eSports
puntajes = [ [1000, 1500, 2000], [300, 700, 1400] ]

puntajes[1][0] = 600
print(puntajes)

#Ejercicio 2: Lista de creadores de contenido en una plataforma de streaming
streamers = [
   {"nombre": "GameNinjaPro", "seguidores": 250000},
   {"nombre": "PixelWarrior", "seguidores": 180000}
]

streamers[0]["nombre"] = "EliteGamerX"
print(streamers)


#Ejercicio 3: Eventos en distintas ciudades del mundo
eventos = {
   "Estados Unidos": ["Los Ángeles", "Nueva York", "Las Vegas"],
   "España": ["Madrid", "Barcelona", "Valencia"]
}

eventos["Estados Unidos"][2] = "San Francisco"
print(eventos)

#Ejercicio 4: Coordenadas de la sede de un torneo internacional
ubicacion = [
   {"latitud": 34.052235, "longitud": -118.243683}
]

ubicacion[0]["latitud"] = "40.712776"
print(ubicacion)

#Ejercicio 5:

def iterar_diccionario(lista):
   for i in lista:
      print(f"nombre - {i['nombre']}, seguidores - {i['seguidores']}")

iterar_diccionario(streamers)

obtener_valores = {
      "nombre": [
         "EliteGamerX",
         "PixelWarrior",
      ],
      "seguidores": [
         "250000",
         "180000",
      ]
}
def iterar_diccionario(valores):
   for clave, lista in valores.items():
      print(f"{len(lista)} {clave.upper()}")
      for element in lista:
         print(element)
      print()
iterar_diccionario(obtener_valores)


#Ejercicio 6:

categorias = {
   "juegos_populares": [
      "Fortnite", 
      "Minecraft", 
      "Valorant", 
      "GTA V",
   ],
   "ciudades_eventos": [
      "Nueva York",
      "Madrid",
      "Tokio",
   ]
}

def identar_diccionario(diccionario):
   for clave, lista in diccionario.items():
      print(f"{len(lista)} {clave.upper()}")
      for element in lista:
         print(element)
      print()
identar_diccionario(categorias)