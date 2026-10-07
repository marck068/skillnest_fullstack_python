"""Modelo Categoría."""
from config.database import execute, fetch_all, fetch_one


def listar(usuario_id):
    return fetch_all(
        """SELECT c.id, c.nombre, COUNT(t.id) AS total_tareas
           FROM categorias c
           LEFT JOIN tareas t ON t.categoria_id = c.id
           WHERE c.usuario_id = %s
           GROUP BY c.id, c.nombre
           ORDER BY c.nombre""",
        (usuario_id,),
    )


def obtener(categoria_id, usuario_id):
    return fetch_one(
        "SELECT * FROM categorias WHERE id=%s AND usuario_id=%s",
        (categoria_id, usuario_id),
    )


def crear(usuario_id, nombre):
    return execute(
        "INSERT INTO categorias (nombre, usuario_id) VALUES (%s, %s)",
        (nombre, usuario_id),
        return_id=True,
    )


def actualizar(categoria_id, usuario_id, nombre):
    return execute(
        "UPDATE categorias SET nombre=%s WHERE id=%s AND usuario_id=%s",
        (nombre, categoria_id, usuario_id),
    )


def eliminar(categoria_id, usuario_id):
    return execute(
        "DELETE FROM categorias WHERE id=%s AND usuario_id=%s",
        (categoria_id, usuario_id),
    )


def existe_nombre(nombre, usuario_id, excluir_id=None):
    if excluir_id:
        row = fetch_one(
            "SELECT id FROM categorias WHERE usuario_id=%s AND LOWER(nombre)=LOWER(%s) AND id<>%s",
            (usuario_id, nombre, excluir_id),
        )
    else:
        row = fetch_one(
            "SELECT id FROM categorias WHERE usuario_id=%s AND LOWER(nombre)=LOWER(%s)",
            (usuario_id, nombre),
        )
    return row is not None
