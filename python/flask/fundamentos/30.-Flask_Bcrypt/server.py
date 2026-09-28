from flask_app import app
from flask_app.controllers import usuarios  # registra las rutas

if __name__ == "__main__":
    app.run(debug=True)
