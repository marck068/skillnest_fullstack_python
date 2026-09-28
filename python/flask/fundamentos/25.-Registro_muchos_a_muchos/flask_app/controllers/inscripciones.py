from flask import flash, redirect, render_template, request, url_for

from flask_app import app
from flask_app.models.curso import Curso
from flask_app.models.estudiante import Estudiante
from flask_app.models.inscripcion import Inscripcion


def _volver():
    """Redirige siempre a la página principal (patrón PRG)."""
    return redirect(url_for("index"))


@app.route("/")
def index():
    """Muestra el formulario y las inscripciones registradas."""
    return render_template(
        "index.html",
        estudiantes=Estudiante.get_all(),
        cursos=Curso.get_all(),
        inscripciones=Inscripcion.get_all(),
    )


@app.route("/inscribir", methods=["POST"])
def inscribir():
    """
    Recibe estudiante_id y curso_id y crea la relación
    en la tabla inscripciones.
    """
    estudiante_id_texto = request.form.get("estudiante_id", "").strip()
    curso_id_texto = request.form.get("curso_id", "").strip()

    # 1. Ambos valores deben venir en el formulario.
    if not estudiante_id_texto or not curso_id_texto:
        flash("Debes seleccionar un estudiante y un curso.", "danger")
        return _volver()

    # 2. Deben ser enteros válidos.
    try:
        estudiante_id = int(estudiante_id_texto)
        curso_id = int(curso_id_texto)
    except ValueError:
        flash("Los identificadores no son válidos.", "danger")
        return _volver()

    # 3. El estudiante y el curso deben existir.
    estudiante = Estudiante.get_by_id(estudiante_id)

    if estudiante is None:
        flash("El estudiante seleccionado no existe.", "danger")
        return _volver()

    curso = Curso.get_by_id(curso_id)

    if curso is None:
        flash("El curso seleccionado no existe.", "danger")
        return _volver()

    data = {"estudiante_id": estudiante_id, "curso_id": curso_id}

    # 4. Evitar inscripciones duplicadas.
    if Inscripcion.existe(data):
        flash(
            f"{estudiante.nombre} ya está inscrito en {curso.nombre_curso}.",
            "warning",
        )
        return _volver()

    # 5. Insertar la relación.
    if Inscripcion.inscribir_estudiante_en_curso(data) is False:
        flash("No fue posible crear la inscripción.", "danger")
        return _volver()

    flash(
        f"Inscripción realizada correctamente: "
        f"{estudiante.nombre} → {curso.nombre_curso}.",
        "success",
    )
    return _volver()
