"""Controlador de libros: CRUD, detalle y exploración."""
import pymysql
from flask import Blueprint, abort, flash, redirect, render_template, request, session, url_for

from models import favorito as Favorito
from models import libro as Libro
from utils.auth import login_required
from utils.validaciones import GENEROS, validar_libro

bp = Blueprint("libros", __name__)
CAMPOS = ("titulo", "autor", "genero", "fecha_publicacion", "descripcion")


def _datos_form():
    return {c: request.form.get(c, "").strip() for c in CAMPOS}


def _libro_propio_o_none(libro_id):
    """Devuelve el libro si pertenece al usuario; si no, avisa y devuelve None.
    404 si el libro no existe."""
    libro = Libro.obtener_por_id(libro_id)
    if libro is None:
        abort(404)
    if libro["usuario_id"] != session["usuario_id"]:
        flash("No tienes permisos para realizar esta acción.", "danger")
        return None
    return libro


@bp.route("/libros")
@login_required
def mis_libros():
    uid = session["usuario_id"]
    return render_template("libros/mis_libros.html",
                           mis_libros=Libro.listar_por_usuario(uid),
                           comunidad=Libro.listar_comunidad())


@bp.route("/explorar")
@login_required
def explorar():
    return render_template("libros/explorar.html",
                           comunidad=Libro.listar_comunidad())


@bp.route("/libros/nuevo", methods=["GET", "POST"])
@login_required
def nuevo():
    datos = {}
    if request.method == "POST":
        datos = _datos_form()
        errores = validar_libro(datos)
        if errores:
            for e in errores:
                flash(e, "danger")
        else:
            try:
                # El dueño SIEMPRE es el usuario de la sesión, nunca un valor del formulario
                Libro.crear(session["usuario_id"], datos)
                flash("Libro creado correctamente.", "success")
                return redirect(url_for("libros.mis_libros"))
            except pymysql.MySQLError:
                flash("Error de base de datos al guardar el libro.", "danger")
    return render_template("libros/nuevo.html", libro=datos, generos=GENEROS)


@bp.route("/libros/editar/<int:libro_id>", methods=["GET", "POST"])
@login_required
def editar(libro_id):
    libro = _libro_propio_o_none(libro_id)
    if libro is None:
        return redirect(url_for("libros.mis_libros"))
    fecha_original = libro["fecha_publicacion"].isoformat()
    datos = {**libro, "fecha_publicacion": fecha_original}
    if request.method == "POST":
        datos = _datos_form()
        errores = validar_libro(datos)
        if errores:
            for e in errores:
                flash(e, "danger")
        else:
            try:
                Libro.actualizar(libro_id, session["usuario_id"], datos)
                flash("Libro actualizado correctamente.", "success")
                return redirect(url_for("libros.mis_libros"))
            except pymysql.MySQLError:
                flash("Error de base de datos al actualizar el libro.", "danger")
    return render_template("libros/editar.html", libro=datos, libro_id=libro_id, generos=GENEROS)


@bp.route("/libros/eliminar/<int:libro_id>", methods=["POST"])
@login_required
def eliminar(libro_id):
    if _libro_propio_o_none(libro_id) is not None:
        try:
            Libro.eliminar(libro_id, session["usuario_id"])
            flash("Libro eliminado correctamente.", "success")
        except pymysql.MySQLError:
            flash("Error de base de datos al eliminar el libro.", "danger")
    return redirect(url_for("libros.mis_libros"))


@bp.route("/libros/<int:libro_id>")
@login_required
def detalle(libro_id):
    libro = Libro.obtener_por_id(libro_id)
    if libro is None:
        abort(404)
    uid = session["usuario_id"]
    return render_template("libros/detalle.html", libro=libro,
                           usuarios_fav=Favorito.usuarios_por_libro(libro_id),
                           es_favorito=Favorito.existe(uid, libro_id),
                           es_propietario=libro["usuario_id"] == uid)
