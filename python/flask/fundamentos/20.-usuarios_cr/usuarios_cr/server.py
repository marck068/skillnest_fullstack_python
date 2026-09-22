from flask import Flask, render_template, request, redirect, url_for
from usuario import Usuario

app = Flask(__name__)


@app.route("/")
def inicio():
    return redirect(url_for("usuarios"))


# READ: listado
@app.route("/usuarios")
def usuarios():
    return render_template("usuarios.html", usuarios=Usuario.get_all())


# Formulario
@app.route("/usuarios/nuevo")
def nuevo_usuario():
    return render_template("usuario_nuevo.html")


# CREATE
@app.route("/usuarios/crear", methods=["POST"])
def crear_usuario():
    data = {
        "nombre": request.form["nombre"].strip(),
        "apellido": request.form["apellido"].strip(),
        "email": request.form["email"].strip(),
    }
    if not all(data.values()):
        return render_template("usuario_nuevo.html", error="Todos los campos son obligatorios.")
    if Usuario.save(data) is False:
        return render_template("usuario_nuevo.html", error="No fue posible crear el usuario.")
    return redirect(url_for("usuarios"))


if __name__ == "__main__":
    app.run(debug=True)