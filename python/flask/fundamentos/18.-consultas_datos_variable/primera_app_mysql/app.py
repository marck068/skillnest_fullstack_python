# ==========================================================
# SERVIDOR FLASK
# ==========================================================

from flask import Flask, render_template

from mascota import Mascota


# ==========================================================
# CREAR APLICACIÓN
# ==========================================================

app = Flask(__name__)


# ==========================================================
# RUTA PRINCIPAL
# ==========================================================

@app.route("/")
def index():
    """
    Muestra todas las mascotas.
    """

    mascotas = Mascota.get_all()

    return render_template(
        "index.html",
        mascotas=mascotas
    )


# ==========================================================
# RUTA PARA BUSCAR MASCOTA POR ID
# ==========================================================

@app.route("/mascota/<int:id>")
def mostrar_mascota(id):
    """
    Recibe un ID desde la URL y busca
    la mascota correspondiente.
    """

    mascota = Mascota.get_by_id(id)

    if mascota is None:
        return "Mascota no encontrada", 404

    return render_template(
        "mascota.html",
        mascota=mascota
    )


# ==========================================================
# RUTA PARA BUSCAR MASCOTA POR NOMBRE
# ==========================================================

@app.route("/mascota/nombre/<string:nombre>")
def buscar_por_nombre(nombre):
    """
    Busca una mascota utilizando su nombre.
    """

    mascota = Mascota.get_by_name(nombre)

    if mascota is None:
        return "Mascota no encontrada", 404

    return render_template(
        "mascota.html",
        mascota=mascota
    )


# ==========================================================
# RUTA PARA BUSCAR MASCOTAS POR TIPO
# ==========================================================

@app.route("/mascotas/tipo/<string:tipo>")
def mascotas_por_tipo(tipo):
    """
    Busca todas las mascotas de un determinado tipo.

    Ejemplo:

        /mascotas/tipo/Perro
    """

    mascotas = Mascota.get_by_tipo(tipo)

    return render_template(
        "index.html",
        mascotas=mascotas,
        tipo=tipo
    )


# ==========================================================
# EJECUTAR SERVIDOR
# ==========================================================

if __name__ == "__main__":

    app.run(debug=True)