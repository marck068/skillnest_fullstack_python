"""Controlador de registro, inicio y cierre de sesión."""
import bcrypt
import pymysql
from flask import Blueprint, flash, redirect, render_template, request, session, url_for

from models.usuario import crear, obtener_por_email
from utils.validaciones import validar_registro

bp = Blueprint("auth", __name__)


@bp.route("/")
def index():
    if session.get("usuario_id"):
        return redirect(url_for("tareas.dashboard"))
    return render_template("auth/acceso.html", registro={}, login_email="")


@bp.route("/login", methods=["GET", "POST"])
def login():
    if session.get("usuario_id"):
        return redirect(url_for("tareas.dashboard"))

    email = ""
    if request.method == "POST":
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")
        usuario = obtener_por_email(email) if email and password else None

        if usuario and bcrypt.checkpw(password.encode(), usuario["password"].encode()):
            session.clear()
            session["usuario_id"] = usuario["id"]
            session["usuario_nombre"] = usuario["nombre"]
            flash("Inicio de sesión correcto.", "success")
            return redirect(url_for("tareas.dashboard"))

        flash("El e-mail o la contraseña son incorrectos.", "danger")

    return render_template("auth/login.html", login_email=email, registro={})


@bp.route("/registro", methods=["GET", "POST"])
def registro():
    if session.get("usuario_id"):
        return redirect(url_for("tareas.dashboard"))

    datos = {}
    if request.method == "POST":
        datos = {c: request.form.get(c, "").strip() for c in ("nombre", "apellido", "email")}
        datos["email"] = datos["email"].lower()
        password = request.form.get("password", "")
        confirmar = request.form.get("confirmar", "")

        errores = validar_registro(datos["nombre"], datos["apellido"], datos["email"], password, confirmar)
        if errores:
            for error in errores:
                flash(error, "danger")
        else:
            try:
                if obtener_por_email(datos["email"]):
                    flash("Este e-mail ya está registrado.", "danger")
                else:
                    hash_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
                    crear(datos["nombre"], datos["apellido"], datos["email"], hash_pw)
                    flash("Cuenta creada correctamente. Ahora puedes iniciar sesión.", "success")
                    return redirect(url_for("auth.login"))
            except pymysql.MySQLError:
                flash("No fue posible crear la cuenta.", "danger")

    return render_template("auth/registro.html", registro=datos, login_email="")


@bp.route("/logout")
def logout():
    session.clear()
    flash("Sesión cerrada correctamente.", "success")
    return redirect(url_for("auth.login"))
