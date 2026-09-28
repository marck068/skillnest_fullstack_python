from flask import Flask

app = Flask(__name__)
app.secret_key = "cambia-esta-clave-secreta"  # necesaria para session y flash
