from flask_app.config.mysqlconnection import connectToMySQL

DB = "esquema_canciones"


class Favorito:
    """Relación entre un usuario y una canción (tabla favoritos)."""

    @classmethod
    def existe(cls, data):
        """Comprueba si la relación ya existe."""
        query = """
            SELECT usuario_id, cancion_id
            FROM favoritos
            WHERE usuario_id = %(usuario_id)s
              AND cancion_id = %(cancion_id)s;
        """
        return bool(connectToMySQL(DB).query_db(query, data))

    @classmethod
    def agregar(cls, data):
        """
        Agrega una canción a los favoritos de un usuario.
        Devuelve False si falla (la PK compuesta impide duplicados).
        """
        query = """
            INSERT INTO favoritos (usuario_id, cancion_id)
            VALUES (%(usuario_id)s, %(cancion_id)s);
        """
        return connectToMySQL(DB).query_db(query, data)
