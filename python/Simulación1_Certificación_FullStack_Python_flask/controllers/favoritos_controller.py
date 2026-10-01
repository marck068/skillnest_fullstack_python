"""Controlador de favoritos."""
import pymysql
from flask import Blueprint, abort, flash, redirect, render_template, session, url_for

from models import favorito as Favorito
from models import libro as Libro
from utils.auth import login_required

bp = Blueprint("favoritos", __name__)


@bp.route("/libros/<int:libro_id>/favorito", methods=["POST"])
@login_required
def agregar(libro_id):
    if Libro.obtener_por_id(libro_id) is None:
        abort(404)
    try:
        if Favorito.agregar(session["usuario_id"], libro_id):
            flash("Libro agregado a favoritos.", "success")
        else:
            flash("Este libro ya está en tus favoritos.", "warning")
    except pymysql.MySQLError:
        flash("Error de base de datos al agregar el favorito.", "danger")
    return redirect(url_for("libros.detalle", libro_id=libro_id))


@bp.route("/favoritos")
@login_required
def mis_favoritos():
    return render_template("favoritos/favoritos.html",
                           libros=Favorito.libros_por_usuario(session["usuario_id"]))
