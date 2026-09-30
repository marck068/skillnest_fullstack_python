import re
from datetime import date, datetime
from flask_app.config.mysqlconnection import MySQLConnection

EMAIL_REGEX = re.compile(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$")
SOLO_LETRAS = re.compile(r"^[A-Za-zÁÉÍÓÚáéíóúÑñÜü ]+$")


class Usuario:

    # ---------- Consultas a la base de datos ----------
    @classmethod
    def crear(cls, datos):
        query = """INSERT INTO usuarios (nombre, apellido, email, password, fecha_nacimiento)
                   VALUES (%(nombre)s, %(apellido)s, %(email)s, %(password)s, %(fecha_nacimiento)s)"""
        return MySQLConnection.query_db(query, datos)  # devuelve el id nuevo

    @classmethod
    def obtener_por_email(cls, email):
        r = MySQLConnection.query_db("SELECT * FROM usuarios WHERE email = %s", (email,))
        return r[0] if r else None

    @classmethod
    def obtener_por_id(cls, id_usuario):
        r = MySQLConnection.query_db("SELECT * FROM usuarios WHERE id = %s", (id_usuario,))
        return r[0] if r else None

    @classmethod
    def email_existe(cls, email):
        return cls.obtener_por_email(email) is not None

    # ---------- Validaciones (se ejecutan en Python) ----------
    @staticmethod
    def validar_registro(form):
        """Devuelve una lista de mensajes de error (vacía si todo es válido)."""
        errores = []
        nombre = form.get("nombre", "").strip()
        apellido = form.get("apellido", "").strip()
        email = form.get("email", "").strip().lower()
        password = form.get("password", "")
        confirmar = form.get("confirmar_password", "")
        fecha = form.get("fecha_nacimiento", "").strip()

        for etiqueta, valor in (("nombre", nombre), ("apellido", apellido)):
            if len(valor) < 2:
                errores.append(f"El {etiqueta} debe tener al menos 2 caracteres.")
            elif not SOLO_LETRAS.match(valor):
                errores.append(f"El {etiqueta} solo puede contener letras.")

        if not email:
            errores.append("El e-mail es obligatorio.")
        elif not EMAIL_REGEX.match(email):
            errores.append("El formato del e-mail no es válido.")
        elif Usuario.email_existe(email):
            errores.append("Ese e-mail ya está registrado.")

        # Contraseña segura (bonus plata)
        if len(password) < 8:
            errores.append("La contraseña debe tener al menos 8 caracteres.")
        if not re.search(r"[A-Z]", password):
            errores.append("La contraseña debe incluir al menos una mayúscula.")
        if not re.search(r"\d", password):
            errores.append("La contraseña debe incluir al menos un número.")
        if password != confirmar:
            errores.append("Las contraseñas no coinciden.")

        # Mayoría de edad (bonus oro)
        if not fecha:
            errores.append("La fecha de nacimiento es obligatoria.")
        else:
            try:
                nacimiento = datetime.strptime(fecha, "%Y-%m-%d").date()
                hoy = date.today()
                edad = hoy.year - nacimiento.year - (
                    (hoy.month, hoy.day) < (nacimiento.month, nacimiento.day))
                if nacimiento > hoy:
                    errores.append("La fecha de nacimiento no puede ser futura.")
                elif edad < 18:
                    errores.append("Debes tener 18 años o más para registrarte.")
            except ValueError:
                errores.append("La fecha de nacimiento no es válida.")

        return errores
