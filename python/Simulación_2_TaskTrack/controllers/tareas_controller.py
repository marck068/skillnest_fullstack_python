"""Controlador principal de tareas: dashboard, CRUD, filtros, estado y comentarios."""
import pymysql
from flask import Blueprint, abort, flash, redirect, render_template, request, session, url_for

from models import tarea as Tarea
from models import categoria as Categoria
from models import comentario as Comentario
from utils.auth import login_required
from utils.validaciones import PRIORIDADES, ESTADOS, validar_tarea

bp = Blueprint("tareas", __name__)


def _datos_form():
    return {
        "titulo": request.form.get("titulo", "").strip(),
        "categoria_id": request.form.get("categoria_id", "").strip(),
        "prioridad": request.form.get("prioridad", "").strip(),
        "fecha_limite": request.form.get("fecha_limite", "").strip(),
        "descripcion": request.form.get("descripcion", "").strip(),
    }


def _tarea_propia(tarea_id):
    tarea = Tarea.obtener_por_id(tarea_id, session["usuario_id"])
    if not tarea:
        abort(404)
    return tarea


@bp.route("/tareas")
@login_required
def dashboard():
    uid = session["usuario_id"]
    filtros = {
        "q": request.args.get("q", "").strip(),
        "categoria": request.args.get("categoria", "").strip(),
        "estado": request.args.get("estado", "").strip(),
        "prioridad": request.args.get("prioridad", "").strip(),
    }
    tareas = Tarea.listar(uid, filtros)
    proximas = Tarea.proximas(uid)
    resumen = Tarea.resumen(uid)
    categorias = Categoria.listar(uid)
    return render_template(
        "tareas/dashboard.html",
        tareas=tareas,
        proximas=proximas,
        resumen=resumen,
        categorias=categorias,
        filtros=filtros,
        prioridades=PRIORIDADES,
        estados=ESTADOS,
    )


@bp.route("/tareas/nueva", methods=["GET", "POST"])
@login_required
def nueva():
    uid = session["usuario_id"]
    datos = {}
    if request.method == "POST":
        datos = _datos_form()
        errores = validar_tarea(datos, uid)
        if errores:
            for error in errores:
                flash(error, "danger")
        else:
            try:
                Tarea.crear(uid, datos)
                flash("Tarea creada correctamente.", "success")
                return redirect(url_for("tareas.dashboard"))
            except pymysql.MySQLError:
                flash("No se pudo guardar la tarea.", "danger")
    return render_template(
        "tareas/nueva.html",
        tarea=datos,
        categorias=Categoria.listar(uid),
        prioridades=PRIORIDADES,
    )


@bp.route("/tareas/<int:tarea_id>")
@login_required
def detalle(tarea_id):
    tarea = _tarea_propia(tarea_id)
    comentarios = Comentario.listar_por_tarea(tarea_id, session["usuario_id"])
    return render_template("tareas/detalle.html", tarea=tarea, comentarios=comentarios)


@bp.route("/tareas/editar/<int:tarea_id>", methods=["GET", "POST"])
@login_required
def editar(tarea_id):
    uid = session["usuario_id"]
    tarea = _tarea_propia(tarea_id)

    if request.method == "POST":
        datos = _datos_form()
        errores = validar_tarea(datos, uid)
        if errores:
            for error in errores:
                flash(error, "danger")
            tarea = {**tarea, **datos}
        else:
            try:
                Tarea.actualizar(tarea_id, uid, datos)
                flash("Tarea actualizada correctamente.", "success")
                return redirect(url_for("tareas.detalle", tarea_id=tarea_id))
            except pymysql.MySQLError:
                flash("No se pudo actualizar la tarea.", "danger")

    return render_template(
        "tareas/editar.html",
        tarea=tarea,
        categorias=Categoria.listar(uid),
        prioridades=PRIORIDADES,
    )


@bp.route("/tareas/eliminar/<int:tarea_id>", methods=["POST"])
@login_required
def eliminar(tarea_id):
    _tarea_propia(tarea_id)
    try:
        Tarea.eliminar(tarea_id, session["usuario_id"])
        flash("Tarea eliminada correctamente.", "success")
    except pymysql.MySQLError:
        flash("No se pudo eliminar la tarea.", "danger")
    return redirect(url_for("tareas.dashboard"))


@bp.route("/tareas/completar/<int:tarea_id>", methods=["POST"])
@login_required
def completar(tarea_id):
    _tarea_propia(tarea_id)
    try:
        Tarea.marcar_completada(tarea_id, session["usuario_id"])
        flash("La tarea fue marcada como completada.", "success")
    except pymysql.MySQLError:
        flash("No se pudo cambiar el estado de la tarea.", "danger")
    return redirect(request.referrer or url_for("tareas.dashboard"))


@bp.route("/tareas/<int:tarea_id>/comentarios", methods=["POST"])
@login_required
def comentario(tarea_id):
    tarea = _tarea_propia(tarea_id)
    texto = request.form.get("comentario", "").strip()
    if len(texto) < 2:
        flash("El comentario debe tener al menos 2 caracteres.", "danger")
    elif len(texto) > 500:
        flash("El comentario no puede superar 500 caracteres.", "danger")
    else:
        Comentario.crear(tarea_id, session["usuario_id"], texto)
        flash("Comentario agregado.", "success")
    return redirect(url_for("tareas.detalle", tarea_id=tarea["id"]))
