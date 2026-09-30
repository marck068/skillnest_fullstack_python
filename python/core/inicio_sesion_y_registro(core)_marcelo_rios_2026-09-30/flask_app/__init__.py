import os
from flask import Flask

# Se crea la aplicación una sola vez y se importa desde controllers
app = Flask(__name__)

# En un proyecto real usa una variable de entorno (ver README)
app.secret_key = os.environ.get("SECRET_KEY", "clave-secreta-de-desarrollo")
