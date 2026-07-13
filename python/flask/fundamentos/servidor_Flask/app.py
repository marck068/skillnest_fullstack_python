from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("inicio.html")

@app.route("/explorar")
def explorar():
    return "<p>Usa / para poder explorar </p>"


@app.route("/bienvenida/<nombre>")
def saludo(nombre):
    return f"¡Bienvenido {nombre}!"

@app.route("/repetir/<apellido>/<int:veces>")
def repetir(apellido, veces):
    return f"¡Hola señor {apellido}!" * veces

@app.errorhandler(404)
def error(error):
    return "Ruta no existente por favor ponga una ruta que exista"



if __name__ == "__main__":
    app.run(debug=True)