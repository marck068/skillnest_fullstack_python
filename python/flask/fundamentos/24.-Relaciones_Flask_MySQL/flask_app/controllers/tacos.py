# ==========================================================
# CONTROLADOR DE TACOS
# ==========================================================

from flask_app import app

from flask import (
    render_template,
    request,
    redirect,
    url_for,
    flash
)

from flask_app.models.taco import Taco

from flask_app.models.restaurante import Restaurante


# ==========================================================
# INICIO
# ==========================================================

@app.route("/")
def index():
    """
    Muestra el formulario para crear un taco.

    También recupera todos los restaurantes para que
    el usuario pueda seleccionar uno.
    """

    todos_restaurantes = Restaurante.get_all()


    return render_template(
        "index.html",
        todos_restaurantes=todos_restaurantes
    )


# ==========================================================
# CREATE
# ==========================================================

@app.route(
    "/crear",
    methods=["POST"]
)
def crear():
    """
    Recibe el formulario y crea un taco.
    """

    datos = {

        "tortilla": request.form.get(
            "tortilla", ""
        ).strip(),

        "guiso": request.form.get(
            "guiso", ""
        ).strip(),

        "salsa": request.form.get(
            "salsa", ""
        ).strip(),

        "restaurante_id": request.form.get(
            "restaurante_id", ""
        )

    }


    # ------------------------------------------------------
    # Validaciones (el HTML valida en el navegador, pero el
    # servidor nunca debe confiar solo en eso).
    # ------------------------------------------------------

    if not (
        datos["tortilla"]
        and datos["guiso"]
        and datos["salsa"]
    ):

        flash(
            "Tortilla, guiso y salsa son obligatorios.",
            "danger"
        )

        return redirect(
            url_for("index")
        )


    if not datos["restaurante_id"].isdigit():

        flash(
            "Debes seleccionar un restaurante.",
            "danger"
        )

        return redirect(
            url_for("index")
        )


    datos["restaurante_id"] = int(
        datos["restaurante_id"]
    )


    # ------------------------------------------------------
    # Guardar. Si el restaurante no existe, la FOREIGN KEY
    # hace fallar el INSERT y query_db devuelve False.
    # ------------------------------------------------------

    nuevo_id = Taco.save(
        datos
    )


    if not nuevo_id:

        flash(
            "No se pudo crear el taco. "
            "Verifica que el restaurante exista.",
            "danger"
        )

        return redirect(
            url_for("index")
        )


    flash(
        "Taco creado correctamente.",
        "success"
    )


    return redirect(
        url_for("tacos")
    )


# ==========================================================
# READ
# LISTADO DE TACOS
# ==========================================================

@app.route("/tacos")
def tacos():
    """
    Muestra el formulario y el listado de todos los tacos.
    """

    todos_los_tacos = Taco.get_all()

    todos_restaurantes = Restaurante.get_all()


    # Diccionario id -> nombre para mostrar a qué
    # restaurante pertenece cada taco.

    nombres_restaurantes = {
        r.id: r.nombre
        for r in todos_restaurantes
    }


    return render_template(
        "index.html",
        tacos=todos_los_tacos,
        todos_restaurantes=todos_restaurantes,
        nombres_restaurantes=nombres_restaurantes
    )


# ==========================================================
# READ
# RESTAURANTE + TACOS
# ==========================================================

@app.route(
    "/restaurantes/<int:id>"
)
def restaurante(id):
    """
    Muestra un restaurante junto con
    todos sus tacos relacionados.
    """

    datos = {
        "id": id
    }


    restaurante_con_tacos = Restaurante.get_restaurante_y_tacos(
        datos
    )


    if restaurante_con_tacos is None:

        return (
            "Restaurante no encontrado",
            404
        )


    return render_template(
        "restaurante.html",
        restaurante=restaurante_con_tacos
    )


# ==========================================================
# LISTADO DE RESTAURANTES
# ==========================================================

@app.route("/restaurantes")
def restaurantes():
    """
    Muestra todos los restaurantes.
    """

    todos_restaurantes = Restaurante.get_all()


    return render_template(
        "restaurantes.html",
        restaurantes=todos_restaurantes
    )
