"""Controlador de autenticación: registro, login y logout."""
import bcrypt
import pymysql
from flask import Blueprint, flash, redirect, render_template, request, session, url_for

from models import usuario as Usuario
from utils.validaciones import validar_registro

bp = Blueprint("auth", __name__)


@bp.route("/")
def index():
    if session.get("usuario_id"):
        return redirect(url_for("libros.mis_libros"))
    return redirect(url_for("auth.login"))


@bp.route("/login", methods=["GET", "POST"])
def login():
    if session.get("usuario_id"):
        return redirect(url_for("libros.mis_libros"))
    email = ""
    if request.method == "POST":
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")
        usuario = Usuario.obtener_por_email(email) if email and password else None
        if usuario and bcrypt.checkpw(password.encode("utf-8"), usuario["password"].encode("utf-8")):
            session.clear()
            session["usuario_id"] = usuario["id"]
            session["usuario_nombre"] = usuario["nombre"]
            flash("Inicio de sesión correcto.", "success")
            return redirect(url_for("libros.mis_libros"))
        flash("Correo o contraseña incorrectos.", "danger")
    return render_template("auth/login.html", login_email=email, registro={})


@bp.route("/registro", methods=["GET", "POST"])
def registro():
    if session.get("usuario_id"):
        return redirect(url_for("libros.mis_libros"))
    datos = {}
    if request.method == "POST":
        datos = {c: request.form.get(c, "").strip() for c in ("nombre", "apellido", "email")}
        datos["email"] = datos["email"].lower()
        password = request.form.get("password", "")
        confirmar = request.form.get("confirmar", "")
        errores = validar_registro(datos["nombre"], datos["apellido"], datos["email"], password, confirmar)
        if errores:
            for e in errores:
                flash(e, "danger")
        else:
            try:
                if Usuario.obtener_por_email(datos["email"]):
                    flash("Este e-mail ya está registrado.", "danger")
                else:
                    hash_pw = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")
                    Usuario.crear(datos["nombre"], datos["apellido"], datos["email"], hash_pw)
                    flash("Registro exitoso. Ya puedes iniciar sesión.", "success")
                    return redirect(url_for("auth.login"))
            except pymysql.err.IntegrityError:  # email duplicado por concurrencia
                flash("Este e-mail ya está registrado.", "danger")
            except pymysql.MySQLError:
                flash("Error de base de datos. Inténtalo más tarde.", "danger")
    return render_template("auth/registro.html", registro=datos, login_email="")


@bp.route("/logout")
def logout():
    session.clear()
    flash("Sesión cerrada correctamente.", "success")
    return redirect(url_for("auth.login"))
