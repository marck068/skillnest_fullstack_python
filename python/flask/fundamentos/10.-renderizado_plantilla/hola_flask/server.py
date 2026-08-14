from flask import Flask, render_template

app = Flask(__name__)


@app.route("/listas")
def renderizar_listas():

    # Lista de números

    numeros = [7, 15, 22]

    # Lista de diccionarios

    listado_estudiantes = [

        {
            "nombre":"Florencia",
            "edad":25
        },

        {
            "nombre":"Valentina",
            "edad":30
        },

        {
            "nombre":"José",
            "edad":27
        },

        {
            "nombre":"Patricio",
            "edad":21
        }

    ]
    return render_template(
    
            "listas.html",
    
            numeros=numeros,
    
            estudiantes=listado_estudiantes
    
        )
@app.route("/videojuegos")
def renderizar_videojuegos():

    listado_videojuegos = [

        {
            "nombre": "Minecraft",
            "plataforma": "PC",
            "anio": 2011
        },

        {
            "nombre": "Grand Theft Auto V",
            "plataforma": "PC",
            "anio": 2013
        },

        {
            "nombre": "Valorant",
            "plataforma": "PC",
            "anio": 2020
        },

        {
            "nombre": "EA Sports FC 25",
            "plataforma": "PC / PS5",
            "anio": 2024
        },

        {
            "nombre": "God of War",
            "plataforma": "PC / PS5",
            "anio": 2018
        },

        {
            "nombre": "Minecraft Dungeons",
            "plataforma": "PC",
            "anio": 2020
        }

    ]

    return render_template(
        "videojuegos.html",
        videojuegos=listado_videojuegos
    )
   

if __name__ == "__main__":
    app.run(debug=True)