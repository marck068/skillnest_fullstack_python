from flask_app import app

# Importar el controlador registra sus rutas en la app.
from flask_app.controllers import usuarios

if __name__ == "__main__":
    app.run(debug=True)
