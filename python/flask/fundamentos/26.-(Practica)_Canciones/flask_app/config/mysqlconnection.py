import os

import pymysql.cursors


class MySQLConnection:
    """
    Administra la conexión entre Flask y MySQL.

    Los datos de conexión pueden sobrescribirse con variables de entorno
    (DB_HOST, DB_USER, DB_PASSWORD); por defecto usa la configuración
    típica de una instalación local.
    """

    def __init__(self, db):
        self.connection = pymysql.connect(
            host=os.environ.get("DB_HOST", "localhost"),
            user=os.environ.get("DB_USER", "root"),
            password=os.environ.get("DB_PASSWORD", "1234"),
            database=db,
            charset="utf8mb4",
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True,
        )

    def query_db(self, query, data=None):
        """
        Ejecuta una consulta con sentencia preparada.

        SELECT  -> lista de diccionarios.
        INSERT  -> ID generado (0 si la tabla no tiene AUTO_INCREMENT).
        UPDATE / DELETE -> filas afectadas.
        Error   -> False.
        """
        with self.connection.cursor() as cursor:
            try:
                cursor.execute(query, data)

                instruccion = query.strip().lower()

                if instruccion.startswith("select"):
                    return cursor.fetchall()

                if instruccion.startswith("insert"):
                    return cursor.lastrowid

                return cursor.rowcount

            except Exception as e:
                print("Something went wrong:", e)
                return False

            finally:
                self.connection.close()


def connectToMySQL(db):
    """Devuelve una instancia de MySQLConnection."""
    return MySQLConnection(db)
