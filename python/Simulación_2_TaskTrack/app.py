"""TaskTrack - aplicación Flask para organizar tareas y proyectos."""
import secrets
from datetime import date
import pymysql
from flask import Flask, abort, render_template, request, session

from config.database import SECRET_KEY
from controllers.auth_controller import bp as auth_bp
from controllers.tareas_controller import bp as tareas_bp
from controllers.categorias_controller import bp as categorias_bp

app = Flask(__name__)
app.secret_key = SECRET_KEY

app.register_blueprint(auth_bp)
app.register_blueprint(tareas_bp)
app.register_blueprint(categorias_bp)


@app.before_request
def proteger_csrf():
    """Genera y valida un token CSRF para todos los formularios POST."""
    if "csrf_token" not in session:
        session["csrf_token"] = secrets.token_hex(16)
    if request.method == "POST":
        token = request.form.get("csrf_token", "")
        if not secrets.compare_digest(token.encode(), session["csrf_token"].encode()):
            abort(400)


@app.context_processor
def inyectar_globales():
    return {
        "csrf_token": lambda: session.get("csrf_token", ""),
        "hoy": date.today().isoformat(),
    }


@app.errorhandler(400)
def error_400(_):
    return render_template(
        "errors/error.html",
        codigo=400,
        mensaje="La solicitud no es válida o el formulario expiró. Vuelve a intentarlo.",
    ), 400


@app.errorhandler(404)
def error_404(_):
    return render_template(
        "errors/error.html",
        codigo=404,
        mensaje="La tarea, categoría o página que buscas no existe.",
    ), 404


@app.errorhandler(pymysql.MySQLError)
def error_bd(_):
    return render_template(
        "errors/error.html",
        codigo=500,
        mensaje="No se pudo acceder a MySQL. Revisa tu archivo .env y que el servidor esté iniciado.",
    ), 500


if __name__ == "__main__":
    app.run(debug=True, port=5000)
