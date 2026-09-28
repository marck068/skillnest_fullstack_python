import os

from flask import Flask

app = Flask(__name__)

# Necesaria para los mensajes flash.
# En producción debe venir de una variable de entorno.
app.secret_key = os.environ.get("SECRET_KEY", "clave-secreta-desarrollo")
