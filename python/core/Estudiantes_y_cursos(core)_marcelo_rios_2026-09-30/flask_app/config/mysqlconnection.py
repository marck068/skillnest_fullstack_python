import os

import pymysql
import pymysql.cursors
from dotenv import load_dotenv

load_dotenv()


class MySQLConnection:
    """Gestiona la conexión entre Flask y MySQL."""

    def __init__(self, db):
        self.connection = pymysql.connect(
            host=os.getenv("DB_HOST", "localhost"),
            user=os.getenv("DB_USER", "root"),
            password=os.getenv("DB_PASSWORD", ""),
            database=db,
            charset="utf8mb4",
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True
        )

    def query_db(self, query, data=None):
        """Ejecuta la consulta SQL recibida."""

        with self.connection.cursor() as cursor:
            try:
                cursor.execute(query, data or {})
                tipo_consulta = query.strip().lower()

                if tipo_consulta.startswith("select"):
                    return cursor.fetchall()

                if tipo_consulta.startswith("insert"):
                    return cursor.lastrowid

                return cursor.rowcount

            except Exception as e:
                print("Error en MySQL:", e)
                return False

            finally:
                self.connection.close()


def connectToMySQL(db):
    """Crea una instancia de MySQLConnection."""
    return MySQLConnection(db)
