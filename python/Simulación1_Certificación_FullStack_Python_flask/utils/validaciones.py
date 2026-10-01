"""Validaciones de backend (se repiten aquí aunque el HTML ya tenga required/minlength)."""
import re
from datetime import date, datetime

GENEROS = ["Ciencia Ficción", "Fantasía", "Romance", "Novela", "Misterio",
           "Terror", "Desarrollo Personal", "Fábula", "Otros"]

EMAIL_RE = re.compile(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+(\.[A-Za-z0-9-]+)+$")
PASSWORD_MIN = 8


def validar_registro(nombre, apellido, email, password, confirmar):
    errores = []
    if not all([nombre, apellido, email, password, confirmar]):
        errores.append("Todos los campos son obligatorios.")
        return errores
    if len(nombre) < 2 or len(apellido) < 2:
        errores.append("Nombre y apellido deben tener al menos 2 caracteres.")
    if len(nombre) > 50 or len(apellido) > 50:
        errores.append("Nombre y apellido no pueden superar 50 caracteres.")
    if not EMAIL_RE.match(email) or len(email) > 120:
        errores.append("El e-mail no tiene un formato válido.")
    if len(password) < PASSWORD_MIN:
        errores.append(f"La contraseña debe tener al menos {PASSWORD_MIN} caracteres.")
    if password != confirmar:
        errores.append("Las contraseñas no coinciden.")
    return errores


def validar_libro(datos):
    """Valida los datos de un libro. La fecha de publicación debe ser válida y no futura."""
    errores = []
    if not all(datos.get(c) for c in ("titulo", "autor", "genero", "fecha_publicacion", "descripcion")):
        errores.append("Todos los campos son obligatorios.")
        return errores
    if len(datos["titulo"]) < 2:
        errores.append("El título debe tener al menos 2 caracteres.")
    if len(datos["titulo"]) > 150 or len(datos["autor"]) > 100:
        errores.append("El título (máx. 150) o el autor (máx. 100) es demasiado largo.")
    if datos["genero"] not in GENEROS:
        errores.append("Selecciona un género válido.")
    if len(datos["descripcion"]) < 10:
        errores.append("La descripción debe tener al menos 10 caracteres.")
    try:
        fecha = datetime.strptime(datos["fecha_publicacion"], "%Y-%m-%d").date()
        if fecha > date.today():
            errores.append("La fecha de publicación no puede ser futura.")
    except ValueError:
        errores.append("La fecha de publicación no es válida.")
    return errores
