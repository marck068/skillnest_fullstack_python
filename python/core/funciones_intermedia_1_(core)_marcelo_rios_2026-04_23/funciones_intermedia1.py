#Ejercicio 1: Ranking de puntajes de un torneo de eSports
puntajes = [ [1000, 1500, 2000], [300, 700, 1400] ]

puntajes[1][0] = 600
print(puntajes)

#Ejercicio 2: Lista de creadores de contenido en una plataforma de streaming
streamer = [
   {"nombre": "GameNinjaPro", "seguidores": 250000},
   {"nombre": "PixelWarrior", "seguidores": 180000}
]

streamer[0]["nombre"] = "EliteGamerX"
print(streamer)


#Ejercicio 3: Eventos en distintas ciudades del mundo
eventosP = {
   "Estados Unidos": ["Los Ángeles", "Nueva York", "Las Vegas"],
   "España": ["Madrid", "Barcelona", "Valencia"]
}

eventosP["Estados Unidos"][2] = "San Francisco"
print(eventosP)

#Ejercicio 4: Coordenadas de la sede de un torneo internacional
ubi = [
   {"latitud": 34.052235, "longitud": -118.243683}
]

ubi[0]["latitud"] = "40.712776"
print(ubi)

#Ejercicio 5:

def iterar_dicci(lista):
   for i in lista:
      print(f"nombre - {i['nombre']}, seguidores - {i['seguidores']}")

iterar_dicci(streamer)

obten_valor = {
      "nombre": [
         "EliteGamerX",
         "PixelWarrior",
      ],
      "seguidores": [
         "250000",
         "180000",
      ]
}
def iterar_dicci(valor):
   for llave, lista in valor.items():
      print(f"{len(lista)} {llave.upper()}")
      for element in lista:
         print(element)
      print()
iterar_dicci(obten_valor)


#Ejercicio 6:

categoria = {
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

def identar_diccio(diccionario):
   for llavesita, lista in diccionario.items():
      print(f"{len(lista)} {llavesita.upper()}")
      for element in lista:
         print(element)
      print()
identar_diccio(categoria)