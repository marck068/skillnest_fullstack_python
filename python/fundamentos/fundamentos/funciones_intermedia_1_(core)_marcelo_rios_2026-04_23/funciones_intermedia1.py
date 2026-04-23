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

def iterar_diccionario(lista):
   nombres = {"nombre": "GameNinjaPro", "nombre": "PixelWarrior"}
   seguidores ={"seguidores": 250000, "seguidores": 180000}


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
