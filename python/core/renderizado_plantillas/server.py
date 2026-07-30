from flask import Flask, render_template
app = Flask(__name__)

@app.route("/listas")
def renderizar_listas():
    # Lista de números
    numeros = [7, 15, 22]

    # Lista de diccionarios
    listado_estudiantes = [
        {"nombre": "Florencia", "edad": 25},
        {"nombre": "Valentina", "edad": 30},
        {"nombre": "José", "edad": 27},
        {"nombre": "Patricio", "edad": 21}
    ]

    return render_template(
        "listas.html",
        numeros=numeros,
        estudiantes=listado_estudiantes
    )


@app.route("/videojuegos")
def renderizar_videojuegos():
    listado_videojuegos = [
        {"nombre": "Minecraft", "plataforma": "PC", "anio": 2011},
        {"nombre": "Call of Duty", "plataforma": "PC", "anio": 2003},
        {"nombre": "Far Cry", "plataforma": "PlayStation 4", "anio": 2014},
        {"nombre": "The Legend of Zelda", "plataforma": "Switch", "anio": 2017},
        {"nombre": "FIFA 23", "plataforma": "PlayStation 5", "anio": 2022},
        {"nombre": "God of War", "plataforma": "PlayStation 4", "anio": 2018},
    ]

    return render_template(
        "videojuegos.html",
        videojuegos=listado_videojuegos
    )


if __name__ == "__main__":
    app.run(debug=True)