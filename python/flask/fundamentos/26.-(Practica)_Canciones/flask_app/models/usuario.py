from flask_app.config.mysqlconnection import connectToMySQL

DB = "esquema_canciones"


class Usuario:
    """Representa un registro de la tabla usuarios."""

    def __init__(self, data):
        self.id = data["id"]
        self.nombre = data["nombre"]
        self.email = data["email"]
        self.contrasena = data["contrasena"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.favoritos = []

    @classmethod
    def get_all(cls):
        """Obtiene todos los usuarios."""
        query = "SELECT * FROM usuarios ORDER BY id;"
        resultados = connectToMySQL(DB).query_db(query)

        return [cls(fila) for fila in resultados or []]

    @classmethod
    def get_by_id(cls, id):
        """Obtiene un usuario por su ID (o None)."""
        query = "SELECT * FROM usuarios WHERE id = %(id)s;"
        resultados = connectToMySQL(DB).query_db(query, {"id": id})

        return cls(resultados[0]) if resultados else None

    @classmethod
    def save(cls, data):
        """Crea un nuevo usuario y devuelve su ID."""
        query = """
            INSERT INTO usuarios (nombre, email, contrasena)
            VALUES (%(nombre)s, %(email)s, %(contrasena)s);
        """
        return connectToMySQL(DB).query_db(query, data)

    @classmethod
    def get_by_id_with_favorites(cls, data):
        """Obtiene un usuario con todas sus canciones favoritas."""
        query = """
            SELECT
                usuarios.*,
                canciones.id         AS cancion_id,
                canciones.titulo     AS cancion_titulo,
                canciones.artista    AS cancion_artista,
                canciones.created_at AS cancion_created_at,
                canciones.updated_at AS cancion_updated_at
            FROM usuarios
            LEFT JOIN favoritos ON favoritos.usuario_id = usuarios.id
            LEFT JOIN canciones ON favoritos.cancion_id = canciones.id
            WHERE usuarios.id = %(id)s
            ORDER BY canciones.titulo;
        """
        resultados = connectToMySQL(DB).query_db(query, data)

        if not resultados:
            return None

        usuario = cls({
            "id": resultados[0]["id"],
            "nombre": resultados[0]["nombre"],
            "email": resultados[0]["email"],
            "contrasena": resultados[0]["contrasena"],
            "created_at": resultados[0]["created_at"],
            "updated_at": resultados[0]["updated_at"],
        })

        for fila in resultados:
            if fila["cancion_id"] is not None:
                usuario.favoritos.append({
                    "id": fila["cancion_id"],
                    "titulo": fila["cancion_titulo"],
                    "artista": fila["cancion_artista"],
                    "created_at": fila["cancion_created_at"],
                    "updated_at": fila["cancion_updated_at"],
                })

        return usuario
