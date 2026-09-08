# ==========================================================
# MODELO USUARIO
# ==========================================================
#
# Este archivo representa la tabla "usuarios"
# mediante una clase de Python.
#
# Sigue exactamente el mismo patrón que "mascota.py":
# cada registro de la tabla se convierte en un objeto
# de la clase Usuario.
#
# ==========================================================


from mysqlconnection import connectToMySQL


# ==========================================================
# CLASE USUARIO
# ==========================================================

class Usuario:
    """
    Representa un registro de la tabla usuarios.
    """

    def __init__(self, data):
        """
        Recibe un diccionario proveniente de MySQL
        y transforma sus datos en atributos del objeto.
        """

        self.id = data["id"]

        self.nombre = data["nombre"]

        self.email = data["email"]

        self.edad = data["edad"]

        self.created_at = data["created_at"]

        self.updated_at = data["updated_at"]


    # ======================================================
    # OBTENER TODOS LOS USUARIOS
    # ======================================================

    @classmethod
    def get_all(cls):
        """
        Consulta todos los usuarios almacenados
        en la base de datos.

        Retorna una lista de objetos Usuario.
        """

        query = """
            SELECT *
            FROM usuarios;
        """

        resultados = connectToMySQL(
            "primera_flask"
        ).query_db(query)

        usuarios = []

        for usuario in resultados:

            usuarios.append(
                cls(usuario)
            )

        return usuarios


    # ======================================================
    # OBTENER UN USUARIO POR ID
    # ======================================================
    # (siguiendo el mismo patrón aplicado en el desafío
    #  de Mascota.get_by_id)

    @classmethod
    def get_by_id(cls, id):
        """
        Busca un usuario específico según su id.
        """

        query = """
            SELECT *
            FROM usuarios
            WHERE id = %(id)s;
        """

        data = {
            "id": id
        }

        resultados = connectToMySQL(
            "primera_flask"
        ).query_db(query, data)

        if not resultados:

            return None

        return cls(resultados[0])
