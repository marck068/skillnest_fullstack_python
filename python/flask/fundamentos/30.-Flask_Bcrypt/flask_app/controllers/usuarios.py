from flask import render_template, redirect, request, session, flash
from flask_bcrypt import Bcrypt

from flask_app import app
from flask_app.models.usuario import Usuario

bcrypt = Bcrypt(app)  # objeto bcrypt


@app.route("/")
def index():
    if "usuario_id" in session:
        return redirect("/dashboard")
    return render_template("index.html")


@app.route("/registrar", methods=["POST"])
def registrar():
    # Validamos el formulario
    if not Usuario.validar_registro(request.form):
        return redirect("/")

    # Hasheamos la contraseña (decode para guardarla como texto)
    pass_hasheado = bcrypt.generate_password_hash(request.form["password"]).decode("utf-8")

    formulario = {
        "nombre": request.form["nombre"].strip(),
        "apellido": request.form["apellido"].strip(),
        "email": request.form["email"],
        "password": pass_hasheado,
    }

    nuevo_id = Usuario.guardar(formulario)
    if not nuevo_id:
        flash("No se pudo registrar el usuario", "registro")
        return redirect("/")

    session["usuario_id"] = nuevo_id
    return redirect("/dashboard")


@app.route("/login", methods=["POST"])
def login():
    usuario = Usuario.buscar_por_email(request.form)
    if not usuario:
        flash("E-mail no registrado", "login")
        return redirect("/")

    if not bcrypt.check_password_hash(usuario.password, request.form["password"]):
        flash("Password incorrecto", "login")
        return redirect("/")

    session["usuario_id"] = usuario.id
    return redirect("/dashboard")


@app.route("/dashboard")
def dashboard():
    if "usuario_id" not in session:
        flash("Debes iniciar sesión", "login")
        return redirect("/")
    usuario = Usuario.buscar_por_id({"id": session["usuario_id"]})
    if not usuario:
        session.clear()
        return redirect("/")
    return render_template("dashboard.html", usuario=usuario)


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")
