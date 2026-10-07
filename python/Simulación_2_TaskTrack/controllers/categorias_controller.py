"""Controlador de categorías personales."""
import pymysql
from flask import Blueprint, abort, flash, redirect, render_template, request, session, url_for

from models import categoria as Categoria
from utils.auth import login_required

bp = Blueprint("categorias", __name__)


@bp.route("/categorias")
@login_required
def listar():
    return render_template("categorias/listar.html", categorias=Categoria.listar(session["usuario_id"]))


@bp.route("/categorias/nueva", methods=["GET", "POST"])
@login_required
def nueva():
    nombre = ""
    if request.method == "POST":
        nombre = request.form.get("nombre", "").strip()
        error = _validar_nombre(nombre)
        if error:
            flash(error, "danger")
        else:
            try:
                Categoria.crear(session["usuario_id"], nombre)
                flash("Categoría creada correctamente.", "success")
                return redirect(url_for("categorias.listar"))
            except pymysql.MySQLError:
                flash("No se pudo crear la categoría. Puede que ya exista.", "danger")
    return render_template("categorias/nueva.html", nombre=nombre)


@bp.route("/categorias/editar/<int:categoria_id>", methods=["GET", "POST"])
@login_required
def editar(categoria_id):
    cat = Categoria.obtener(categoria_id, session["usuario_id"])
    if not cat:
        abort(404)

    nombre = cat["nombre"]
    if request.method == "POST":
        nombre = request.form.get("nombre", "").strip()
        error = _validar_nombre(nombre, categoria_id)
        if error:
            flash(error, "danger")
        else:
            Categoria.actualizar(categoria_id, session["usuario_id"], nombre)
            flash("Categoría actualizada.", "success")
            return redirect(url_for("categorias.listar"))
    return render_template("categorias/editar.html", categoria=cat, nombre=nombre)


@bp.route("/categorias/eliminar/<int:categoria_id>", methods=["POST"])
@login_required
def eliminar(categoria_id):
    cat = Categoria.obtener(categoria_id, session["usuario_id"])
    if not cat:
        abort(404)
    try:
        Categoria.eliminar(categoria_id, session["usuario_id"])
        flash("Categoría eliminada.", "success")
    except pymysql.MySQLError:
        flash("No puedes eliminar una categoría que tenga tareas asociadas.", "danger")
    return redirect(url_for("categorias.listar"))


def _validar_nombre(nombre, categoria_id=None):
    if not nombre:
        return "El campo es obligatorio."
    if len(nombre) < 3:
        return "El nombre debe tener al menos 3 caracteres."
    if len(nombre) > 50:
        return "El nombre no puede superar 50 caracteres."
    if Categoria.existe_nombre(nombre, session["usuario_id"], categoria_id):
        return "Ya tienes una categoría con ese nombre."
    return None
