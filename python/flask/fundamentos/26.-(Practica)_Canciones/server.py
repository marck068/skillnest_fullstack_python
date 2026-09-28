from flask_app import app

# Importar el controlador registra todas las rutas en la app.
from flask_app.controllers import canciones  # noqa: F401


if __name__ == "__main__":
    app.run(debug=True)
