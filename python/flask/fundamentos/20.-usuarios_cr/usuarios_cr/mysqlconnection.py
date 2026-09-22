import pymysql.cursors


class MySQLConnection:
    """Administra la conexión entre Python y MySQL."""

    def __init__(self, db):
        self.connection = pymysql.connect(
            host="localhost",
            user="root",
            password="1234",  
            database=db,
            charset="utf8mb4",
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True,
        )

    def query_db(self, query, data=None):
        """SELECT -> lista de dicts | INSERT -> id generado | error -> False"""
        with self.connection.cursor() as cursor:
            try:
                cursor.execute(query, data)
                q = query.strip().lower()
                if q.startswith("select"):
                    return cursor.fetchall()
                elif q.startswith("insert"):
                    return cursor.lastrowid
                return None
            except Exception as e:
                print("Something went wrong:", e)
                return False
            finally:
                self.connection.close()


def connectToMySQL(db):
    return MySQLConnection(db)