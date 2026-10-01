"""BookHub - punto de entrada de la aplicación Flask."""
import secrets
from datetime import date

import pymysql
from flask import Flask, abort, render_template, request, session

from config.database import SECRET_KEY
from controllers.auth_controller import bp as auth_bp
from controllers.favoritos_controller import bp as favoritos_bp
from controllers.libros_controller import bp as libros_bp

app = Flask(__name__)
app.secret_key = SECRET_KEY

app.register_blueprint(auth_bp)
app.register_blueprint(libros_bp)
app.register_blueprint(favoritos_bp)


@app.before_request
def proteger_csrf():
    """Token CSRF simple: todo POST debe traer el token guardado en la sesión."""
    if "csrf_token" not in session:
        session["csrf_token"] = secrets.token_hex(16)
    if request.method == "POST":
        token = request.form.get("csrf_token", "")
        if not secrets.compare_digest(token.encode("utf-8"), session["csrf_token"].encode("utf-8")):
            abort(400)


@app.context_processor
def inyectar_globales():
    return {"csrf_token": lambda: session.get("csrf_token", ""),
            "hoy": date.today().isoformat()}


def _error(codigo, mensaje):
    return render_template("errors/error.html", codigo=codigo, mensaje=mensaje), codigo


@app.errorhandler(400)
def error_400(_):
    return _error(400, "La solicitud no es válida o el formulario expiró. Vuelve a intentarlo.")


@app.errorhandler(404)
def error_404(_):
    return _error(404, "La página o el libro que buscas no existe.")


@app.errorhandler(pymysql.MySQLError)
def error_bd(_):
    return _error(500, "No se pudo acceder a la base de datos. Revisa la configuración de MySQL.")


if __name__ == "__main__":
    app.run(debug=True, port=5000)
