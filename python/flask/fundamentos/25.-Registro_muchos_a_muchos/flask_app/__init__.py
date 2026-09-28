import os

from flask import Flask

app = Flask(__name__)

# Necesaria para utilizar mensajes flash.
# En producción define la variable de entorno SECRET_KEY.
app.secret_key = os.environ.get("SECRET_KEY", "clave-secreta-desarrollo")
