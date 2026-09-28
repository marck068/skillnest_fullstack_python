import os

import pymysql.cursors


class MySQLConnection:
    """
    Administra la conexión entre Flask y MySQL.

    Los datos de conexión se leen de variables de entorno
    (DB_HOST, DB_USER, DB_PASSWORD, DB_PORT) y, si no existen,
    se usan valores por defecto para desarrollo local.
    """

    def __init__(self, db):
        self.connection = pymysql.connect(
            host=os.environ.get("DB_HOST", "localhost"),
            port=int(os.environ.get("DB_PORT", 3306)),
            user=os.environ.get("DB_USER", "root"),
            password=os.environ.get("DB_PASSWORD", ""),
            database=db,
            charset="utf8mb4",
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True,
        )

    def query_db(self, query, data=None):
        """
        Ejecuta una consulta SQL con sentencias preparadas
        (los valores viajan separados de la consulta).

        SELECT          -> lista de diccionarios.
        INSERT          -> ID generado o filas afectadas.
        UPDATE / DELETE -> filas afectadas.
        Error           -> False.
        """
        with self.connection.cursor() as cursor:
            try:
                cursor.execute(query, data)

                comando = query.strip().lower()

                if comando.startswith("select"):
                    return cursor.fetchall()

                if comando.startswith("insert"):
                    return cursor.lastrowid or cursor.rowcount

                return cursor.rowcount

            except Exception as e:
                print("Something went wrong:", e)
                return False

            finally:
                self.connection.close()


def connectToMySQL(db):
    """Recibe el nombre de la base de datos y devuelve una conexión."""
    return MySQLConnection(db)
