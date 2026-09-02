"""
El Juego del Destino
---------------------
Aplicación Flask que recibe datos de un formulario, los guarda en
la sesión del usuario y genera una predicción personalizada.
"""

import random
from flask import Flask, render_template, request, session, redirect

app = Flask(__name__)
app.secret_key = "clave_secreta"  # Necesaria para poder usar session

# Lista de predicciones posibles. Cada vez que el usuario consulte
# su destino, Flask elegirá una al azar.
PREDICCIONES = [
    "Encontrarás el verdadero amor en los próximos meses. Tu corazón se llenará de alegría.",
    "Nuevas oportunidades laborales tocarán tu puerta muy pronto.",
    "Un viaje inesperado cambiará tu forma de ver la vida.",
    "Reencontrarás a alguien importante de tu pasado.",
    "Tu esfuerzo será recompensado antes de lo que imaginas.",
    "Una decisión difícil te traerá paz y claridad mental.",
    "La fortuna estará de tu lado en asuntos económicos.",
    "Un proyecto personal comenzará a dar sus primeros frutos.",
]

# Descripciones asociadas a colores. Si el color no está en la lista,
# se usa una descripción genérica.
DESCRIPCIONES_COLOR = {
    "rojo": "revela pasión, energía y una fuerte determinación.",
    "azul": "refleja calma, sabiduría y una mente tranquila.",
    "verde": "revela tu afinidad con la misteriosa y el descubrimiento.",
    "morado": "simboliza intuición, misterio y espiritualidad.",
    "amarillo": "representa alegría, optimismo y buena energía.",
    "negro": "refleja elegancia, fuerza interior y misterio.",
    "blanco": "simboliza pureza, claridad y nuevos comienzos.",
    "naranja": "representa entusiasmo, creatividad y vitalidad.",
    "rosado": "refleja ternura, dulzura y armonía emocional.",
    "gris": "representa equilibrio, prudencia y estabilidad.",
}

# Descripciones asociadas a animales.
DESCRIPCIONES_ANIMAL = {
    "perro": "lealtad y compañía forman parte de tu esencia.",
    "gato": "simboliza tu naturaleza de independencia y misterio.",
    "aguila": "representa visión, libertad y ambición.",
    "águila": "representa visión, libertad y ambición.",
    "leon": "refleja coraje, liderazgo y una gran fuerza interior.",
    "león": "refleja coraje, liderazgo y una gran fuerza interior.",
    "delfin": "simboliza inteligencia, alegría y buena comunicación.",
    "delfín": "simboliza inteligencia, alegría y buena comunicación.",
    "lobo": "refleja instinto, lealtad y espíritu de equipo.",
    "tigre": "representa poder, valentía y determinación.",
}


def obtener_descripcion_color(color):
    """Devuelve una descripción para el color ingresado (o una genérica)."""
    return DESCRIPCIONES_COLOR.get(
        color.strip().lower(),
        "revela una personalidad única y llena de matices especiales.",
    )


def obtener_descripcion_animal(animal):
    """Devuelve una descripción para el animal ingresado (o una genérica)."""
    return DESCRIPCIONES_ANIMAL.get(
        animal.strip().lower(),
        "simboliza una conexión especial con la naturaleza y tu instinto.",
    )


def generar_prediccion_edad(edad):
    """Genera un pequeño mensaje relacionado con la edad del usuario."""
    if edad < 18:
        return "Tienes toda una vida llena de aventuras por delante."
    elif edad < 30:
        return f"A tus {edad} años, estás en un momento favorable para aprovechar nuevas oportunidades."
    elif edad < 50:
        return f"A tus {edad} años, la experiencia acumulada te ayudará a tomar grandes decisiones."
    else:
        return f"A tus {edad} años, la sabiduría te guía hacia un futuro tranquilo y pleno."


@app.route("/")
def index():
    """Muestra el formulario principal donde el usuario ingresa sus datos."""
    return render_template("index.html")


@app.route("/enviar", methods=["POST"])
def enviar():
    """
    Recibe los datos del formulario mediante request.form,
    valida que estén completos y los guarda en la sesión.
    Luego redirige al usuario hacia /futuro.
    """
    nombre = request.form.get("nombre", "").strip()
    edad = request.form.get("edad", "").strip()
    color = request.form.get("color", "").strip()
    animal = request.form.get("animal", "").strip()

    # Validaciones básicas
    if not nombre or not edad or not color or not animal:
        return redirect("/")

    if not edad.isdigit() or int(edad) <= 0 or int(edad) > 120:
        return redirect("/")

    # Guardamos los datos en la sesión del usuario
    session["nombre"] = nombre
    session["edad"] = int(edad)
    session["color"] = color
    session["animal"] = animal

    return redirect("/futuro")


@app.route("/futuro")
def futuro():
    """
    Recupera los datos guardados en la sesión y genera
    una predicción personalizada para mostrarla con Jinja2.
    """
    nombre = session.get("nombre")
    edad = session.get("edad")
    color = session.get("color")
    animal = session.get("animal")

    # Si no hay datos en la sesión, volvemos al formulario
    if not nombre:
        return redirect("/")

    prediccion = random.choice(PREDICCIONES)
    numero_suerte = random.randint(1, 99)
    descripcion_color = obtener_descripcion_color(color)
    descripcion_animal = obtener_descripcion_animal(animal)
    prediccion_edad = generar_prediccion_edad(edad)

    return render_template(
        "futuro.html",
        nombre=nombre,
        edad=edad,
        color=color,
        animal=animal,
        prediccion=prediccion,
        numero_suerte=numero_suerte,
        descripcion_color=descripcion_color,
        descripcion_animal=descripcion_animal,
        prediccion_edad=prediccion_edad,
    )


if __name__ == "__main__":
    app.run(debug=True)
