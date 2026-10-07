"""Modelo de comentarios de tareas."""
from config.database import execute, fetch_all


def crear(tarea_id, usuario_id, texto):
    return execute(
        "INSERT INTO comentarios (tarea_id, usuario_id, texto) VALUES (%s,%s,%s)",
        (tarea_id, usuario_id, texto),
        return_id=True,
    )


def listar_por_tarea(tarea_id, usuario_id):
    return fetch_all(
        """SELECT c.*, u.nombre, u.apellido
           FROM comentarios c
           JOIN usuarios u ON u.id=c.usuario_id
           JOIN tareas t ON t.id=c.tarea_id
           WHERE c.tarea_id=%s AND t.usuario_id=%s
           ORDER BY c.created_at DESC""",
        (tarea_id, usuario_id),
    )
