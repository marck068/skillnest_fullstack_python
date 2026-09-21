from flask import Flask, render_template, request, redirect, url_for
from mascota import Mascota

app = Flask(__name__)


# READ
@app.route("/")
def index():
    mascotas = Mascota.get_all()
    return render_template("index.html", mascotas=mascotas)


# CREATE
# La ruta coincide con el "action" del formulario
@app.route("/crear_mascota", methods=["POST"])
def crear_mascota():
    # IMPORTANTE: las claves deben coincidir con los placeholders del query
    datos = {
        "nombre": request.form["nombre"],
        "tipo": request.form["tipo"],
        "color": request.form["color"]
    }

    Mascota.save(datos)

    # POST -> Redirect -> GET
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)