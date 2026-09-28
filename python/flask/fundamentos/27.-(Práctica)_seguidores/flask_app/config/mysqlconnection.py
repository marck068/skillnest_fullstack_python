import pymysql.cursors


class MySQLConnection:
    """Administra la conexión entre Flask y MySQL."""

    def __init__(self, db):
        self.connection = pymysql.connect(
            host="localhost",
            user="root",
            password="1234",  # <-- cambia según tu instalación local
            database=db,
            charset="utf8mb4",
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True,
        )

    def query_db(self, query, data=None):
        """
        SELECT -> lista de diccionarios
        INSERT -> ID generado
        otros  -> filas afectadas
        Error  -> False
        """
        with self.connection.cursor() as cursor:
            try:
                cursor.execute(query, data)
                tipo = query.strip().lower()

                if tipo.startswith("select"):
                    return cursor.fetchall()
                if tipo.startswith("insert"):
                    return cursor.lastrowid
                return cursor.rowcount

            except Exception as e:
                print("Something went wrong:", e)
                return False

            finally:
                self.connection.close()


def connectToMySQL(db):
    return MySQLConnection(db)
