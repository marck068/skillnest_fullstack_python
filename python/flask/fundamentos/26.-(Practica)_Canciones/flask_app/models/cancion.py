from flask_app.config.mysqlconnection import connectToMySQL

DB = "esquema_canciones"


class Cancion:
    """Representa un registro de la tabla canciones."""

    def __init__(self, data):
        self.id = data["id"]
        self.titulo = data["titulo"]
        self.artista = data["artista"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.usuarios = []

    @classmethod
    def get_all(cls):
        """Obtiene todas las canciones."""
        query = "SELECT * FROM canciones ORDER BY id;"
        resultados = connectToMySQL(DB).query_db(query)

        return [cls(fila) for fila in resultados or []]

    @classmethod
    def get_by_id(cls, id):
        """Obtiene una canción por su ID (o None)."""
        query = "SELECT * FROM canciones WHERE id = %(id)s;"
        resultados = connectToMySQL(DB).query_db(query, {"id": id})

        return cls(resultados[0]) if resultados else None

    @classmethod
    def save(cls, data):
        """Crea una nueva canción y devuelve su ID."""
        query = """
            INSERT INTO canciones (titulo, artista)
            VALUES (%(titulo)s, %(artista)s);
        """
        return connectToMySQL(DB).query_db(query, data)

    @classmethod
    def get_by_id_with_users(cls, data):
        """Obtiene una canción con los usuarios que la marcaron favorita."""
        query = """
            SELECT
                canciones.*,
                usuarios.id         AS usuario_id,
                usuarios.nombre     AS usuario_nombre,
                usuarios.email      AS usuario_email,
                usuarios.created_at AS usuario_created_at,
                usuarios.updated_at AS usuario_updated_at
            FROM canciones
            LEFT JOIN favoritos ON favoritos.cancion_id = canciones.id
            LEFT JOIN usuarios ON favoritos.usuario_id = usuarios.id
            WHERE canciones.id = %(id)s
            ORDER BY usuarios.nombre;
        """
        resultados = connectToMySQL(DB).query_db(query, data)

        if not resultados:
            return None

        cancion = cls({
            "id": resultados[0]["id"],
            "titulo": resultados[0]["titulo"],
            "artista": resultados[0]["artista"],
            "created_at": resultados[0]["created_at"],
            "updated_at": resultados[0]["updated_at"],
        })

        for fila in resultados:
            if fila["usuario_id"] is not None:
                cancion.usuarios.append({
                    "id": fila["usuario_id"],
                    "nombre": fila["usuario_nombre"],
                    "email": fila["usuario_email"],
                    "created_at": fila["usuario_created_at"],
                    "updated_at": fila["usuario_updated_at"],
                })

        return cancion

    @classmethod
    def get_users_not_favorited(cls, data):
        """BONUS: usuarios que todavía NO tienen esta canción como favorita."""
        query = """
            SELECT usuarios.id, usuarios.nombre, usuarios.email
            FROM usuarios
            LEFT JOIN favoritos
                ON favoritos.usuario_id = usuarios.id
               AND favoritos.cancion_id = %(cancion_id)s
            WHERE favoritos.usuario_id IS NULL
            ORDER BY usuarios.nombre;
        """
        return connectToMySQL(DB).query_db(query, data) or []
