# ==========================================================
# INICIALIZACIÓN DE FLASK
# ==========================================================

from flask import Flask


# ==========================================================
# CREAR APLICACIÓN
# ==========================================================

app = Flask(__name__)


# ==========================================================
# SECRET KEY
# ==========================================================
# Necesaria para usar flash() y session.
# En producción debe venir de una variable de entorno.

app.secret_key = "clave-secreta-desarrollo"
