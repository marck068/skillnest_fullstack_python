# ==========================================
# Importaciones
# ==========================================

from flask import Flask, render_template, request

# ==========================================
# Crear aplicación Flask
# ==========================================

app = Flask(__name__)

# ==========================================
# Base de datos ficticia
# ==========================================

frutas = [

    {
        "nombre": "Manzana",
        "precio": 2.5,
        "imagen": "manzana.png",
        "descripcion": "Fruta dulce y crujiente, rica en fibra y vitamina C."
    },

    {
        "nombre": "Plátano",
        "precio": 1.8,
        "imagen": "platano.png",
        "descripcion": "Fruta energética rica en potasio, perfecta para deportistas."
    },

    {
        "nombre": "Naranja",
        "precio": 3.0,
        "imagen": "naranja.png",
        "descripcion": "Cítrico jugoso con alto contenido de vitamina C y antioxidantes."
    },

    {
        "nombre": "Fresa",
        "precio": 4.5,
        "imagen": "fresa.png",
        "descripcion": "Baya dulce y aromática, rica en antioxidantes y vitamina C."
    },

    {
        "nombre": "Uva",
        "precio": 3.8,
        "imagen": "uva.png",
        "descripcion": "Fruta pequeña y dulce, ideal para snacks y postres."
    },

    {
        "nombre": "Piña",
        "precio": 5.0,
        "imagen": "pina.png",
        "descripcion": "Fruta tropical dulce y ácida, con propiedades antiinflamatorias."
    },

    {
        "nombre": "Sandía",
        "precio": 4.2,
        "imagen": "sandia.png",
        "descripcion": "Fruta refrescante, compuesta en un 90% de agua, ideal para el verano."
    },

    {
        "nombre": "Mango",
        "precio": 3.5,
        "imagen": "mango.png",
        "descripcion": "Fruta tropical dulce y aromática, rica en vitaminas A y C."
    }

]

# ==========================================
# Ruta principal
# ==========================================

@app.route("/")
def index():
    """
    Muestra la página principal del mercado.
    """

    return render_template(
        "index.html",
        frutas=frutas
    )


# ==========================================
# Catálogo de frutas
# ==========================================

@app.route("/frutas")
def catalogo():

    return render_template(
        "frutas.html",
        frutas=frutas
    )


# ==========================================
# Procesar compra
# ==========================================

@app.route("/checkout", methods=["POST"])
def checkout():

    # ----------------------------
    # Información del cliente
    # ----------------------------

    nombre = request.form["nombre"]

    email = request.form["email"]

    direccion = request.form["direccion"]


    # ----------------------------
    # Variables auxiliares
    # ----------------------------

    pedido = []

    total = 0

    total_frutas = 0


    # ----------------------------
    # Recorrer todas las frutas
    # ----------------------------

    for fruta in frutas:

        cantidad = int(request.form[fruta["nombre"]])

        if cantidad > 0:

            subtotal = cantidad * fruta["precio"]

            pedido.append({

                "nombre": fruta["nombre"],

                "precio": fruta["precio"],

                "cantidad": cantidad,

                "subtotal": subtotal,

                "imagen": fruta["imagen"]

            })

            total += subtotal

            total_frutas += cantidad


    # ----------------------------
    # Mostrar resumen
    # ----------------------------

    return render_template(

        "checkout.html",

        nombre=nombre,

        email=email,

        direccion=direccion,

        pedido=pedido,

        total=total,

        total_frutas=total_frutas

    )


# ==========================================
# Ejecutar servidor
# ==========================================

if __name__ == "__main__":

    app.run(debug=True)


from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

# Ruta principal (Formulario de compra)
@app.route('/')
def index():
    return render_template("index.html")

# Ruta para ver las frutas disponibles
@app.route('/frutas')
def frutas():
    return render_template("frutas.html")

# Ruta para procesar la orden de compra (POST)
@app.route('/checkout', methods=['POST'])
def checkout():
    # Muestra los datos recibidos en la consola para depuración
    print("Datos recibidos del formulario:", request.form)

    # Captura de cantidades de frutas (asegurando convertir a entero)
    fresa = int(request.form.get('strawberry', 0))
    frambuesa = int(request.form.get('raspberry', 0))
    manzana = int(request.form.get('apple', 0))
    platano = int(request.form.get('banana', 0))

    # Cálculo del total de frutas
    total_frutas = fresa + frambuesa + manzana + platano

    # Datos del cliente
    nombre = request.form.get('first_name', '')
    apellido = request.form.get('last_name', '')
    estudiante_id = request.form.get('student_id', '')

    # Mensaje de confirmación impreso en la consola del servidor
    print(f"Cobrando a {nombre} {apellido} por {total_frutas} frutas")

    # Fecha y hora actual formateada
    fecha_hora = datetime.now().strftime("%B %d, %Y %I:%M:%S %p")

    # Renderiza la plantilla checkout pasando todas las variables necesarias
    return render_template(
        "checkout.html",
        fresa=fresa,
        frambuesa=frambuesa,
        manzana=manzana,
        platano=platano,
        total_frutas=total_frutas,
        nombre=nombre,
        apellido=apellido,
        estudiante_id=estudiante_id,
        fecha_hora=fecha_hora
    )

if __name__ == "__main__":
    app.run(debug=True)