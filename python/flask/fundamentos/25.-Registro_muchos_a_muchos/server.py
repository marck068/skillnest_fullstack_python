from flask_app import app

# Importar el controlador registra las rutas decoradas con @app.route.
from flask_app.controllers import inscripciones  # noqa: F401


if __name__ == "__main__":
    app.run(debug=True)
