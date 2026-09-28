import os
import pymysql.cursors


class MySQLConnection:
    def __init__(self, db):
        self.connection = pymysql.connect(
            host=os.environ.get("DB_HOST", "localhost"),
            user=os.environ.get("DB_USER", "root"),
            password=os.environ.get("DB_PASSWORD", "1234"),
            db=db,
            charset="utf8mb4",
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True,
        )

    def query_db(self, query, data=None):
        with self.connection.cursor() as cursor:
            try:
                query = cursor.mogrify(query, data)
                print("Ejecutando:", query)
                cursor.execute(query)
                tipo = query.strip().lower().split()[0]
                if tipo == "insert":
                    self.connection.commit()
                    return cursor.lastrowid
                elif tipo == "select":
                    return cursor.fetchall()
                else:
                    self.connection.commit()
                    return True
            except Exception as e:
                print("Error en la consulta:", e)
                return False
            finally:
                self.connection.close()


def connectToMySQL(db):
    return MySQLConnection(db)
