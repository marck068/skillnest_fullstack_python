from flask import Flask, render_template, request

app = Flask(__name__)

# Base de datos ficticia de plataformas digitales
# "icono" es el nombre de la clase de Bootstrap Icons (https://icons.getbootstrap.com)
datos = [
    {"nombre": "Spotify",   "usuarios": "515M",  "fundado": 2006, "pais": "Suecia", "icono": "bi-spotify",      "color": "#1DB954"},
    {"nombre": "Netflix",   "usuarios": "247M",  "fundado": 1997, "pais": "EE.UU.", "icono": "bi-play-btn-fill", "color": "#E50914"},
    {"nombre": "YouTube",   "usuarios": "2.5B",  "fundado": 2005, "pais": "EE.UU.", "icono": "bi-youtube",      "color": "#FF0000"},
    {"nombre": "Twitch",    "usuarios": "140M",  "fundado": 2011, "pais": "EE.UU.", "icono": "bi-twitch",       "color": "#9146FF"},
    {"nombre": "TikTok",    "usuarios": "1.7B",  "fundado": 2016, "pais": "China",  "icono": "bi-tiktok",       "color": "#010101"},
    {"nombre": "Instagram", "usuarios": "2.35B", "fundado": 2010, "pais": "EE.UU.", "icono": "bi-instagram",    "color": "#E1306C"},
    {"nombre": "Discord",   "usuarios": "250M",  "fundado": 2015, "pais": "EE.UU.", "icono": "bi-discord",      "color": "#5865F2"},
]


# Ruta para mostrar la tabla con datos
@app.route("/tabla")
def tabla():

    # Parámetros que llegan desde el formulario (filtros y orden)
    pais_filtro = request.args.get("pais", "todos")
    orden = request.args.get("orden", "nombre")
    direccion = request.args.get("direccion", "asc")

    # Lista de países disponibles para el selector, sin repetir
    paises = []
    for fila in datos:
        if fila["pais"] not in paises:
            paises.append(fila["pais"])

    # Filtrado por país
    if pais_filtro != "todos":
        plataformas = []
        for fila in datos:
            if fila["pais"] == pais_filtro:
                plataformas.append(fila)
    else:
        plataformas = list(datos)

    # Ordenamiento según la columna elegida
    orden_invertido = (direccion == "desc")
    plataformas.sort(key=lambda fila: fila[orden], reverse=orden_invertido)

    return render_template(
        "tabla.html",
        plataformas=plataformas,
        paises=paises,
        pais_filtro=pais_filtro,
        orden=orden,
        direccion=direccion
    )


if __name__ == "__main__":
    app.run(debug=True)
