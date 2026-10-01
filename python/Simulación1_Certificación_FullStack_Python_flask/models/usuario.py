"""Modelo Usuario: acceso a la tabla `usuarios`."""
from config.database import execute, fetch_one


def crear(nombre, apellido, email, password_hash):
    return execute(
        "INSERT INTO usuarios (nombre, apellido, email, password) VALUES (%s, %s, %s, %s)",
        (nombre, apellido, email, password_hash), return_id=True,
    )


def obtener_por_email(email):
    return fetch_one("SELECT * FROM usuarios WHERE email = %s", (email,))


def obtener_por_id(usuario_id):
    return fetch_one("SELECT * FROM usuarios WHERE id = %s", (usuario_id,))
