# ==========================================
# IMPORTACIONES
# ==========================================

from flask import Flask, render_template, request, redirect


# ==========================================
# CREACIÓN DE LA APLICACIÓN
# ==========================================

app = Flask(__name__)


# ==========================================
# RUTA PRINCIPAL
# ==========================================

@app.route("/")
def index():
    """
    Muestra el formulario de creación de usuario.
    """

    return render_template("index.html")


# ==========================================
# PROCESAR FORMULARIO
# ==========================================

@app.route("/crear_comprar", methods=["POST"])
def crear_comprar():
    """
    Recibe la información enviada mediante POST.

    Esta función se encarga de procesar los datos
    antes de realizar la redirección.
    """

    # ------------------------------------------
    # Obtener los datos enviados por el formulario
    # ------------------------------------------


    nombre = request.form["nombre"]
    
    email = request.form["email"]

    categoria = request.form["categoria"]
    # ------------------------------------------
    # Mostrar los datos en la terminal
    # ------------------------------------------

    print("===================================")

    print("Producto recibido")

    print(f"Nombre: {nombre}")

    print(f"Email: {email}")

    print(f"Categoría: {categoria}")

    print("===================================")


    # ------------------------------------------
    # Redireccionar al usuario
    # ------------------------------------------

    return redirect("/mostrar_compra")


# ==========================================
# MOSTRAR RESULTADO
# ==========================================

@app.route("/mostrar_compra")
def mostrar_compra():
    """
    Esta ruta recibe una solicitud GET después
    de la redirección.
    """

    print("Comprar redirigida")

    # ------------------------------------------
    # request.form estará vacío
    # ------------------------------------------

    print(request.form)


    # ------------------------------------------
    # Mostrar la plantilla
    # ------------------------------------------

    return render_template("resultado.html")


# ==========================================
# EJECUTAR SERVIDOR
# ==========================================

if __name__ == "__main__":

    app.run(debug=True)