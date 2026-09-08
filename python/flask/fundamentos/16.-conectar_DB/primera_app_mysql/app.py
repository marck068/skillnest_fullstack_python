# ==========================================================
# SERVIDOR FLASK + MYSQL
# ==========================================================


from flask import Flask, render_template

from mascota import Mascota
from usuario import Usuario


# ==========================================================
# CREAR APLICACIÓN
# ==========================================================

app = Flask(__name__)


# ==========================================================
# RUTA PRINCIPAL - LISTADO DE MASCOTAS
# ==========================================================

@app.route("/")
def index():
    """
    Consulta todas las mascotas de la base de datos
    y las envía hacia la plantilla HTML.
    """

    mascotas = Mascota.get_all()

    print(mascotas)

    return render_template(
        "index.html",
        mascotas=mascotas
    )


# ==========================================================
# RUTA DE DETALLE - UNA MASCOTA POR ID (usa el desafío)
# ==========================================================

@app.route("/mascotas/<int:id>")
def mostrar_mascota(id):
    """
    Busca una mascota específica utilizando
    Mascota.get_by_id() y muestra sus datos.
    """

    mascota = Mascota.get_by_id(id)

    return render_template(
        "mascota.html",
        mascota=mascota
    )


# ==========================================================
# RUTA - LISTADO DE USUARIOS (ejercicio de consolidación)
# ==========================================================

@app.route("/usuarios")
def usuarios():
    """
    Consulta todos los usuarios de la base de datos
    y los envía hacia la plantilla HTML.
    """

    usuarios = Usuario.get_all()

    return render_template(
        "usuarios.html",
        usuarios=usuarios
    )


# ==========================================================
# EJECUTAR SERVIDOR
# ==========================================================

if __name__ == "__main__":

    app.run(debug=True)
