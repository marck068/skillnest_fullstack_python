import os
import mysql.connector


class MySQLConnection:
    """Maneja la conexión entre Flask y MySQL."""
    connection = None

    @classmethod
    def get_db(cls):
        # Reutiliza la conexión; si se cerró, crea una nueva
        if cls.connection is None or not cls.connection.is_connected():
            cls.connection = mysql.connector.connect(
                host=os.environ.get("DB_HOST", "localhost"),
                user=os.environ.get("DB_USER", "root"),
                password=os.environ.get("DB_PASSWORD", "1234"),  # cámbiala
                database="sistema_usuarios",
                autocommit=True,
            )
        return cls.connection

    @classmethod
    def query_db(cls, query, data=None):
        """Ejecuta una consulta parametrizada.
        SELECT -> lista de diccionarios | INSERT -> id insertado."""
        cursor = cls.get_db().cursor(dictionary=True)
        try:
            cursor.execute(query, data or ())
            if query.strip().lower().startswith("select"):
                return cursor.fetchall()
            return cursor.lastrowid
        finally:
            cursor.close()
