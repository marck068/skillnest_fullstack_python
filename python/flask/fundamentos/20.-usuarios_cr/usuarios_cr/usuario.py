from mysqlconnection import connectToMySQL

DB = "esquema_usuarios"


class Usuario:
    """Representa un registro de la tabla usuarios."""

    def __init__(self, data):
        self.id = data["id"]
        self.nombre = data["nombre"]
        self.apellido = data["apellido"]
        self.email = data["email"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    # READ
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM usuarios ORDER BY id;"
        resultados = connectToMySQL(DB).query_db(query)
        return [cls(fila) for fila in (resultados or [])]

    # CREATE
    @classmethod
    def save(cls, data):
        query = """
            INSERT INTO usuarios (nombre, apellido, email, created_at, updated_at)
            VALUES (%(nombre)s, %(apellido)s, %(email)s, NOW(), NOW());
        """
        return connectToMySQL(DB).query_db(query, data)