"""Modelo Libro: acceso a la tabla `libros`."""
from config.database import execute, fetch_all, fetch_one

# Subconsulta reutilizable: cantidad de usuarios que marcaron el libro como favorito
_TOTAL_FAV = "(SELECT COUNT(*) FROM favoritos f WHERE f.libro_id = l.id)"


def crear(usuario_id, datos):
    return execute(
        """INSERT INTO libros (titulo, autor, genero, fecha_publicacion, descripcion, usuario_id)
           VALUES (%s, %s, %s, %s, %s, %s)""",
        (datos["titulo"], datos["autor"], datos["genero"],
         datos["fecha_publicacion"], datos["descripcion"], usuario_id),
        return_id=True,
    )


def actualizar(libro_id, usuario_id, datos):
    # El WHERE incluye usuario_id: defensa extra además de la verificación del controlador
    return execute(
        """UPDATE libros SET titulo=%s, autor=%s, genero=%s, fecha_publicacion=%s, descripcion=%s
           WHERE id=%s AND usuario_id=%s""",
        (datos["titulo"], datos["autor"], datos["genero"], datos["fecha_publicacion"],
         datos["descripcion"], libro_id, usuario_id),
    )


def eliminar(libro_id, usuario_id):
    return execute("DELETE FROM libros WHERE id=%s AND usuario_id=%s", (libro_id, usuario_id))


def obtener_por_id(libro_id):
    """Libro con el nombre de quien lo publicó y su total de favoritos."""
    return fetch_one(
        f"""SELECT l.*, u.nombre AS publicado_por, {_TOTAL_FAV} AS total_favoritos
            FROM libros l JOIN usuarios u ON u.id = l.usuario_id
            WHERE l.id = %s""",
        (libro_id,),
    )


def listar_por_usuario(usuario_id):
    return fetch_all(
        f"""SELECT l.*, {_TOTAL_FAV} AS total_favoritos
            FROM libros l WHERE l.usuario_id = %s ORDER BY l.created_at DESC""",
        (usuario_id,),
    )


def listar_comunidad():
    """Todos los libros de la plataforma (visibles para cualquier usuario registrado)."""
    return fetch_all(
        f"""SELECT l.*, u.nombre AS publicado_por, {_TOTAL_FAV} AS total_favoritos
            FROM libros l JOIN usuarios u ON u.id = l.usuario_id
            ORDER BY l.created_at DESC"""
    )
