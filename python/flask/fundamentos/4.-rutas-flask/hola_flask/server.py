from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return "¡Hola Mundo!"


@app.route("/exito")
def exito():
    return "¡Éxito!"


@app.route("/saludo/<nombre>")
def saludo(nombre):
    return f"¡Hola {nombre}!"


@app.route("/color/<nombre>/<color>")
def color_favorito(nombre, color):
    return f"Hola {nombre}, tu color favorito es el {color}"


@app.route("/saludo/<nombre>/<int:veces>")
def repetir(nombre, veces):
    return f"¡Hola {nombre}!" * veces


@app.route("/despedida/<nombre>")
def despedir(nombre, veces):
    return f"¡Hasta luego {nombre}! ¡Esperamos verte pronto!"


@app.route("/presentacion/<nombre>/<int:edad>")
def presentar(nombre, edad):
    return f"Hola {nombre}, tienes {edad} años"


if __name__ == "__main__":
    app.run(debug=True)