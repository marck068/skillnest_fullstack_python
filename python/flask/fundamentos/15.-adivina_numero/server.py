# ==========================================================
# IMPORTACIONES
# ==========================================================
from flask import Flask, render_template, request, redirect, url_for, session
import random

# ==========================================================
# CREACIÓN DE LA APLICACIÓN FLASK
# ==========================================================
app = Flask(__name__)

# ==========================================================
# CONFIGURACIÓN DE LA CLAVE SECRETA
# Esta clave es necesaria para que Flask pueda firmar
# y proteger los datos guardados en la sesión del usuario.
# ==========================================================
app.secret_key = "clave-secreta-adivina-numero"


# ==========================================================
# RUTA PRINCIPAL ( GET )
# ==========================================================
@app.route("/")
def index():
    """
    Muestra la pantalla principal del juego.
    Si todavía no existe una partida en curso (no hay numero_secreto
    en la sesión), se crea una nueva: se genera el número aleatorio
    y se inicializan los intentos y los mensajes.
    """

    # --------------------------------------------------------
    # INICIALIZAR LA SESIÓN (solo si es una partida nueva)
    # --------------------------------------------------------
    if "numero_secreto" not in session:
        # Generamos un número aleatorio entre 1 y 10
        session["numero_secreto"] = random.randint(1, 10)
        session["intentos"] = 0
        session["mensaje"] = "Adivina un número entre 1 y 10."
        session["resultado"] = ""

    # --------------------------------------------------------
    # RECUPERAMOS LOS DATOS GUARDADOS EN LA SESIÓN
    # --------------------------------------------------------
    mensaje = session.get("mensaje", "Adivina un número entre 1 y 10.")
    intentos = session.get("intentos", 0)
    resultado = session.get("resultado", "")

    # --------------------------------------------------------
    # ENVIAMOS LOS DATOS A LA PLANTILLA HTML
    # --------------------------------------------------------
    return render_template(
        "index.html",
        mensaje=mensaje,
        intentos=intentos,
        resultado=resultado
    )


# ==========================================================
# RUTA PARA PROCESAR EL INTENTO DEL USUARIO ( POST )
# ==========================================================
@app.route("/adivinar", methods=["POST"])
def adivinar():
    """
    Procesa el número enviado por el usuario mediante el formulario,
    lo compara con el número secreto guardado en la sesión y
    actualiza el mensaje, el resultado y el contador de intentos.
    """

    # --------------------------------------------------------
    # VALIDACIÓN BÁSICA DEL DATO RECIBIDO
    # Evitamos que la aplicación se caiga si el valor no es válido.
    # --------------------------------------------------------
    valor_formulario = request.form.get("numero", "")

    try:
        numero_usuario = int(valor_formulario)
    except (ValueError, TypeError):
        # Si el valor no se puede convertir a entero, avisamos
        # al usuario sin romper la aplicación ni perder la partida.
        session["mensaje"] = "⚠️ Por favor ingresa un número válido entre 1 y 10."
        session["resultado"] = ""
        return redirect(url_for("index"))

    # Validamos que el número esté dentro del rango permitido
    if numero_usuario < 1 or numero_usuario > 10:
        session["mensaje"] = "⚠️ El número debe estar entre 1 y 10."
        session["resultado"] = ""
        return redirect(url_for("index"))

    # --------------------------------------------------------
    # OBTENEMOS EL NÚMERO SECRETO GUARDADO EN LA SESIÓN
    # --------------------------------------------------------
    # Si por alguna razón no existe (sesión perdida), generamos uno nuevo
    numero_secreto = session.get("numero_secreto")
    if numero_secreto is None:
        numero_secreto = random.randint(1, 10)
        session["numero_secreto"] = numero_secreto
        session["intentos"] = 0

    # --------------------------------------------------------
    # AUMENTAMOS EL CONTADOR DE INTENTOS
    # --------------------------------------------------------
    session["intentos"] = session.get("intentos", 0) + 1

    # --------------------------------------------------------
    # COMPARAMOS EL NÚMERO INGRESADO CON EL NÚMERO SECRETO
    # --------------------------------------------------------
    if numero_usuario < numero_secreto:
        session["resultado"] = "mayor"
        session["mensaje"] = "⬆️ El número secreto es MAYOR que tu elección."
    elif numero_usuario > numero_secreto:
        session["resultado"] = "menor"
        session["mensaje"] = "⬇️ El número secreto es MENOR que tu elección."
    else:
        session["resultado"] = "correcto"
        session["mensaje"] = f"🎉 ¡Correcto! El número era {numero_secreto}."

    # --------------------------------------------------------
    # PATRÓN POST -> PROCESAR -> REDIRECT -> GET
    # --------------------------------------------------------
    return redirect(url_for("index"))


# ==========================================================
# RUTA PARA REINICIAR EL JUEGO
# ==========================================================
@app.route("/reiniciar")
def reiniciar():
    """
    Elimina toda la información guardada en la sesión
    (número secreto, intentos, mensaje y resultado),
    permitiendo comenzar una partida completamente nueva.
    """

    # --------------------------------------------------------
    # LIMPIAMOS LA SESIÓN POR COMPLETO
    # --------------------------------------------------------
    session.clear()

    return redirect(url_for("index"))


# ==========================================================
# EJECUCIÓN DEL SERVIDOR
# ==========================================================
if __name__ == "__main__":
    app.run(debug=True)
