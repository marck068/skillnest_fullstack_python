"""Validaciones de formularios."""
import re
from datetime import date, datetime
from models.categoria import obtener

PRIORIDADES = ["Alta", "Media", "Baja"]
ESTADOS = ["Pendiente", "En progreso", "Completada"]
EMAIL_RE = re.compile(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+(\.[A-Za-z0-9-]+)+$")


def validar_registro(nombre, apellido, email, password, confirmar):
    errores = []
    if not all([nombre, apellido, email, password, confirmar]):
        return ["Todos los campos son obligatorios."]
    if len(nombre) < 2 or len(apellido) < 2:
        errores.append("Nombre y apellido deben tener al menos 2 caracteres.")
    if len(nombre) > 50 or len(apellido) > 50:
        errores.append("Nombre y apellido no pueden superar 50 caracteres.")
    if not EMAIL_RE.match(email):
        errores.append("El e-mail no tiene un formato válido.")
    if len(password) < 8:
        errores.append("La contraseña debe tener al menos 8 caracteres.")
    if password != confirmar:
        errores.append("Las contraseñas no coinciden.")
    return errores


def validar_tarea(datos, usuario_id):
    errores = []
    if not datos["titulo"] or len(datos["titulo"]) < 3:
        errores.append("El título es obligatorio y debe tener al menos 3 caracteres.")
    if len(datos["titulo"]) > 120:
        errores.append("El título no puede superar 120 caracteres.")
    if not datos["categoria_id"]:
        errores.append("Selecciona una categoría.")
    else:
        try:
            if not obtener(int(datos["categoria_id"]), usuario_id):
                errores.append("La categoría seleccionada no pertenece a tu usuario.")
        except ValueError:
            errores.append("La categoría seleccionada no es válida.")
    if datos["prioridad"] not in PRIORIDADES:
        errores.append("Selecciona una prioridad válida.")
    if not datos["fecha_limite"]:
        errores.append("La fecha límite es obligatoria.")
    else:
        try:
            fecha = datetime.strptime(datos["fecha_limite"], "%Y-%m-%d").date()
            if fecha < date.today():
                errores.append("La fecha límite no puede estar en el pasado.")
        except ValueError:
            errores.append("La fecha límite no es válida.")
    if len(datos["descripcion"]) < 10:
        errores.append("La descripción debe tener al menos 10 caracteres.")
    if len(datos["descripcion"]) > 1000:
        errores.append("La descripción no puede superar 1000 caracteres.")
    return errores
