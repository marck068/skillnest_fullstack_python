import re

from flask import flash

from flask_app.config.mysqlconnection import connectToMySQL

EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$")
ESQUEMA = "esquema_loginreg"


class Usuario:
    def __init__(self, data):
        self.id = data["id"]
        self.nombre = data["nombre"]
        self.apellido = data["apellido"]
        self.email = data["email"]
        self.password = data["password"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def guardar(cls, datos):
        query = (
            "INSERT INTO usuarios(nombre, apellido, email, password) "
            "VALUES(%(nombre)s, %(apellido)s, %(email)s, %(password)s)"
        )
        # Regresa el id del nuevo registro
        return connectToMySQL(ESQUEMA).query_db(query, datos)

    @classmethod
    def buscar_por_email(cls, datos):
        query = "SELECT * FROM usuarios WHERE email = %(email)s"
        resultados = connectToMySQL(ESQUEMA).query_db(query, datos)
        if resultados and len(resultados) == 1:
            return cls(resultados[0])
        return False

    @classmethod
    def buscar_por_id(cls, datos):
        query = "SELECT * FROM usuarios WHERE id = %(id)s"
        resultados = connectToMySQL(ESQUEMA).query_db(query, datos)
        if resultados and len(resultados) == 1:
            return cls(resultados[0])
        return False

    @staticmethod
    def validar_registro(form):
        es_valido = True

        if len(form["nombre"].strip()) < 2:
            flash("El nombre debe tener al menos 2 caracteres", "registro")
            es_valido = False
        if len(form["apellido"].strip()) < 2:
            flash("El apellido debe tener al menos 2 caracteres", "registro")
            es_valido = False

        if not EMAIL_REGEX.match(form["email"]):
            flash("E-mail inválido", "registro")
            es_valido = False
        elif Usuario.buscar_por_email({"email": form["email"]}):
            flash("Ese e-mail ya está registrado", "registro")
            es_valido = False

        if len(form["password"]) < 8:
            flash("La contraseña debe tener al menos 8 caracteres", "registro")
            es_valido = False
        if form["password"] != form["confirmar_password"]:
            flash("Las contraseñas no coinciden", "registro")
            es_valido = False

        return es_valido
