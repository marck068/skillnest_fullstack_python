"""Crea datos demo adicionales. Ejecuta desde la raíz del proyecto con Flask instalado."""
import bcrypt
from config.database import execute, fetch_one

EMAIL = "marcelo@tasktrack.cl"
PASSWORD = "password"

usuario = fetch_one("SELECT id FROM usuarios WHERE email=%s", (EMAIL,))
if usuario:
    print("El usuario demo ya existe.")
else:
    uid = execute(
        "INSERT INTO usuarios (nombre, apellido, email, password) VALUES (%s,%s,%s,%s)",
        ("Marcelo", "Rios", EMAIL, bcrypt.hashpw(PASSWORD.encode(), bcrypt.gensalt()).decode()),
        return_id=True,
    )
    for nombre in ("Estudios", "Trabajo", "Salud", "Personal"):
        execute("INSERT INTO categorias (nombre, usuario_id) VALUES (%s,%s)", (nombre, uid))
    print("Usuario demo creado:", EMAIL, "/ contraseña:", PASSWORD)
