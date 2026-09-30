from flask import render_template, request, redirect, session, flash, make_response
from werkzeug.security import generate_password_hash, check_password_hash
from mysql.connector.errors import IntegrityError

from flask_app import app
from flask_app.models.usuario import Usuario


# Página principal con los dos formularios
@app.route("/")
def index():
    if "usuario_id" in session:
        return redirect("/exito")
    return render_template("index.html")


# Registro
@app.route("/registrar", methods=["POST"])
def registrar():
    errores = Usuario.validar_registro(request.form)
    if errores:
        for e in errores:
            flash(e, "error")
        return redirect("/")

    datos = {
        "nombre": request.form["nombre"].strip(),
        "apellido": request.form["apellido"].strip(),
        "email": request.form["email"].strip().lower(),
        "password": generate_password_hash(request.form["password"]),  # nunca texto plano
        "fecha_nacimiento": request.form["fecha_nacimiento"],
    }
    try:
        id_usuario = Usuario.crear(datos)
    except IntegrityError:  # por si el UNIQUE de MySQL detecta un duplicado
        flash("Ese e-mail ya está registrado.", "error")
        return redirect("/")

    session["usuario_id"] = id_usuario
    return redirect("/exito")


# Inicio de sesión
@app.route("/login", methods=["POST"])
def login():
    email = request.form.get("email", "").strip().lower()
    password = request.form.get("password", "")

    usuario = Usuario.obtener_por_email(email)
    if not usuario:
        # En una app real conviene un mensaje genérico ("credenciales inválidas")
        flash("Correo no registrado.", "error")
        return redirect("/")
    if not check_password_hash(usuario["password"], password):
        flash("Contraseña incorrecta.", "error")
        return redirect("/")

    session["usuario_id"] = usuario["id"]  # solo el ID, nunca la contraseña
    return redirect("/exito")


# Página protegida
@app.route("/exito")
def exito():
    if "usuario_id" not in session:
        flash("Debes iniciar sesión para acceder.", "error")
        return redirect("/")

    usuario = Usuario.obtener_por_id(session["usuario_id"])
    if not usuario:  # el usuario ya no existe en la BD
        session.clear()
        flash("Debes iniciar sesión para acceder.", "error")
        return redirect("/")

    respuesta = make_response(render_template("exito.html", usuario=usuario))
    # Evita que el botón "atrás" muestre la página desde caché tras el logout
    respuesta.headers["Cache-Control"] = "no-store"
    return respuesta


# Cerrar sesión
@app.route("/logout")
def logout():
    session.clear()
    flash("Has cerrado sesión correctamente.", "success")
    return redirect("/")
