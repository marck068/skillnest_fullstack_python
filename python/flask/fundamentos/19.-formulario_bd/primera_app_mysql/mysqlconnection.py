import pymysql.cursors


class MySQLConnection:
    """Administra la conexión entre Python y MySQL."""

    def __init__(self, db):
        self.connection = pymysql.connect(
            host="localhost",
            user="root",
            password="1234",   # <-- cambia por tu contraseña de MySQL
            database=db,
            charset="utf8mb4",
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True
        )

    def query_db(self, query, data=None):
        """
        SELECT -> lista de diccionarios
        INSERT -> ID generado
        UPDATE / DELETE -> None
        Error  -> False
        """
        with self.connection.cursor() as cursor:
            try:
                # Imprime la consulta real que se ejecutará
                print("Running Query:", cursor.mogrify(query, data))

                cursor.execute(query, data)

                if query.strip().lower().startswith("select"):
                    return cursor.fetchall()
                elif query.strip().lower().startswith("insert"):
                    return cursor.lastrowid
                else:
                    return None

            except Exception as e:
                print("Something went wrong:")
                print(e)
                return False

            finally:
                self.connection.close()


def connectToMySQL(db):
    return MySQLConnection(db)