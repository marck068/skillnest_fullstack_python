"""Modelo Favorito: acceso a la tabla `favoritos`."""
import pymysql

from config.database import execute, fetch_all, fetch_one


def existe(usuario_id, libro_id):
    fila = fetch_one(
        "SELECT id FROM favoritos WHERE usuario_id=%s AND libro_id=%s", (usuario_id, libro_id)
    )
    return fila is not None


def agregar(usuario_id, libro_id):
    """Devuelve True si se creó, False si ya existía (restricción UNIQUE)."""
    try:
        execute("INSERT INTO favoritos (usuario_id, libro_id) VALUES (%s, %s)",
                (usuario_id, libro_id))
        return True
    except pymysql.err.IntegrityError:
        return False


def usuarios_por_libro(libro_id):
    return fetch_all(
        """SELECT u.id, u.nombre, u.apellido FROM favoritos f
           JOIN usuarios u ON u.id = f.usuario_id
           WHERE f.libro_id = %s ORDER BY f.created_at""",
        (libro_id,),
    )


def libros_por_usuario(usuario_id):
    return fetch_all(
        """SELECT l.* FROM favoritos f JOIN libros l ON l.id = f.libro_id
           WHERE f.usuario_id = %s ORDER BY f.created_at DESC""",
        (usuario_id,),
    )
