from flask import render_template, request, redirect, url_for, flash

from flask_app import app
from flask_app.models.usuario import Usuario
from flask_app.models.seguidor import Seguidor


def volver():
    return redirect(url_for("usuarios"))


@app.route("/")
def inicio():
    return volver()


@app.route("/usuarios")
def usuarios():
    return render_template(
        "usuarios.html",
        usuarios=Usuario.get_all(),
        relaciones=Seguidor.get_all(),
    )


@app.route("/usuarios/crear", methods=["POST"])
def crear_usuario():
    data = {
        "nombre": request.form.get("nombre", "").strip(),
        "apellido": request.form.get("apellido", "").strip(),
        "email": request.form.get("email", "").strip(),
    }

    if not all(data.values()):
        flash("Todos los campos son obligatorios.", "danger")
        return volver()

    if Usuario.save(data) is False:
        flash("No fue posible crear el usuario.", "danger")
        return volver()

    flash("Usuario creado correctamente.", "success")
    return volver()


@app.route("/seguir", methods=["POST"])
def seguir():
    """
    usuario_id  = usuario que es seguido
    seguidor_id = usuario que lo sigue
    """
    try:
        usuario_id = int(request.form.get("usuario_id", ""))
        seguidor_id = int(request.form.get("seguidor_id", ""))
    except ValueError:
        flash("Debes seleccionar un usuario y un seguidor.", "danger")
        return volver()

    if Usuario.get_by_id(usuario_id) is None:
        flash("El usuario seleccionado no existe.", "danger")
        return volver()

    if Usuario.get_by_id(seguidor_id) is None:
        flash("El seguidor seleccionado no existe.", "danger")
        return volver()

    if usuario_id == seguidor_id:
        flash("Un usuario no puede seguirse a sí mismo.", "warning")
        return volver()

    data = {"usuario_id": usuario_id, "seguidor_id": seguidor_id}

    # BONUS: no permitir la misma relación usuario:seguidor más de una vez
    if Seguidor.existe(data):
        flash("Esta relación ya existe.", "warning")
        return volver()

    if Seguidor.seguir(data) is False:
        flash("No fue posible registrar la relación.", "danger")
        return volver()

    flash("Relación registrada correctamente.", "success")
    return volver()
