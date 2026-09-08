# ==========================================================
# MODELO MASCOTA
# ==========================================================
#
# Este archivo representa la tabla "mascotas"
# mediante una clase de Python.
#
# ==========================================================


# Importamos la función encargada de crear
# una conexión con MySQL.

from mysqlconnection import connectToMySQL


# ==========================================================
# CLASE MASCOTA
# ==========================================================

class Mascota:
    """
    Representa un registro de la tabla mascotas.
    """

    def __init__(self, data):
        """
        Recibe un diccionario proveniente de MySQL
        y transforma sus datos en atributos del objeto.
        """

        self.id = data["id"]

        self.nombre = data["nombre"]

        self.tipo = data["tipo"]

        self.color = data["color"]

        self.created_at = data["created_at"]

        self.updated_at = data["updated_at"]


    # ======================================================
    # OBTENER TODAS LAS MASCOTAS
    # ======================================================

    @classmethod
    def get_all(cls):
        """
        Consulta todas las mascotas almacenadas
        en la base de datos.

        Retorna una lista de objetos Mascota.
        """

        # --------------------------------------------------
        # Consulta SQL
        # --------------------------------------------------

        query = """
            SELECT *
            FROM mascotas;
        """


        # --------------------------------------------------
        # Ejecutar consulta
        # --------------------------------------------------

        resultados = connectToMySQL(
            "primera_flask"
        ).query_db(query)


        # --------------------------------------------------
        # Crear lista de objetos
        # --------------------------------------------------

        mascotas = []


        # --------------------------------------------------
        # Convertir cada diccionario en Mascota
        # --------------------------------------------------

        for mascota in resultados:

            mascotas.append(
                cls(mascota)
            )


        # --------------------------------------------------
        # Retornar resultado
        # --------------------------------------------------

        return mascotas


    # ======================================================
    # OBTENER UNA MASCOTA POR ID (DESAFÍO)
    # ======================================================

    @classmethod
    def get_by_id(cls, id):
        """
        Busca una mascota específica según su id.

        Recibe:
            id -> identificador de la mascota (int).

        Retorna:
            Una instancia de Mascota si existe el registro,
            o None si no se encontró ninguna coincidencia.
        """

        # --------------------------------------------------
        # Consulta SQL parametrizada
        # --------------------------------------------------

        query = """
            SELECT *
            FROM mascotas
            WHERE id = %(id)s;
        """


        # --------------------------------------------------
        # Datos que reemplazan al placeholder %(id)s
        # --------------------------------------------------

        data = {
            "id": id
        }


        # --------------------------------------------------
        # Ejecutar consulta
        # --------------------------------------------------

        resultados = connectToMySQL(
            "primera_flask"
        ).query_db(query, data)


        # --------------------------------------------------
        # Si hubo un error o no se encontró el registro
        # --------------------------------------------------

        if not resultados:

            return None


        # --------------------------------------------------
        # Como el id es único, tomamos el primer resultado
        # y lo convertimos en un objeto Mascota.
        # --------------------------------------------------

        return cls(resultados[0])
