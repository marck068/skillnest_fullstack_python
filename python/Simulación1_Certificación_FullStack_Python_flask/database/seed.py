"""Carga los datos de ejemplo del wireframe de BookHub.

Uso (desde la carpeta raíz del proyecto, con la BD ya creada con bookhub.sql):
    python database/seed.py          # pide confirmación antes de borrar los datos actuales
    python database/seed.py --yes    # sin preguntar

Después de ejecutarlo puedes iniciar sesión como Ana:
    email: ana@bookhub.com      contraseña: 12345678
(todos los usuarios de ejemplo usan la misma contraseña).
"""
import os
import sys
from datetime import datetime, timedelta

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PASSWORD = "12345678"

# --- Usuarios --------------------------------------------------------------
# Los 6 primeros salen en el wireframe. El resto son usuarios de relleno: el libro
# "El alquimista" tiene 30 favoritos y la restricción UNIQUE(usuario_id, libro_id)
# obliga a que existan 30 usuarios distintos.
USUARIOS_PRINCIPALES = [
    ("Ana", "García", "ana@bookhub.com"),
    ("Carlos", "Rojas", "carlos@bookhub.com"),
    ("Laura", "Fuentes", "laura@bookhub.com"),
    ("Miguel", "Soto", "miguel@bookhub.com"),
    ("Sofía", "Vargas", "sofia@bookhub.com"),
    ("Daniel", "Pérez", "daniel@bookhub.com"),
]
NOMBRES_RELLENO = [
    "Valentina", "Mateo", "Camila", "Benjamín", "Isidora", "Tomás", "Javiera", "Felipe",
    "Antonia", "Joaquín", "Fernanda", "Nicolás", "Catalina", "Sebastián", "Constanza",
    "Diego", "Martina", "Vicente", "Florencia", "Cristóbal", "Josefa", "Matías",
    "Agustina", "Ignacio",
]

# --- Libros ----------------------------------------------------------------
# (título, autor, género, fecha, descripción, email del dueño, total de favoritos)
# Se insertan del MÁS ANTIGUO al MÁS NUEVO en created_at; las listas se muestran
# con ORDER BY created_at DESC, así que el orden en pantalla queda igual al wireframe.
LIBROS_ANA = [  # orden en pantalla: Cien años, El principito, 1984, Orgullo
    ("Orgullo y prejuicio", "Jane Austen", "Romance", "2024-08-02",
     "Clásico de la literatura inglesa sobre Elizabeth Bennet y el señor Darcy, "
     "una historia de amor, prejuicios y diferencias sociales.", 9),
    ("1984", "George Orwell", "Ciencia Ficción", "2024-07-15",
     "Novela distópica sobre un estado totalitario que vigila y controla "
     "cada aspecto de la vida de sus ciudadanos.", 15),
    ("El principito", "Antoine de S.", "Fábula", "2024-06-21",
     "Un piloto conoce a un pequeño príncipe que viaja de planeta en planeta y "
     "le enseña lo esencial de la amistad y la vida.", 8),
    ("Cien años de soledad", "Gabriel García Márquez", "Novela", "2024-05-10",
     "Una obra maestra del realismo mágico que narra la historia de la familia Buendía...", 12),
]
LIBROS_COMUNIDAD = [  # orden en pantalla: Dune, Hábitos Atómicos, El alquimista
    ("El alquimista", "Paulo Coelho", "Novela", "2024-06-18",
     "Santiago, un joven pastor andaluz, viaja hacia Egipto en busca de un tesoro "
     "y descubre su leyenda personal.", "miguel@bookhub.com", 30),
    ("Hábitos Atómicos", "James Clear", "Desarrollo Personal", "2024-06-01",
     "Un método práctico para crear buenos hábitos y eliminar los malos "
     "a través de pequeños cambios constantes.", "laura@bookhub.com", 18),
    ("Dune", "Frank Herbert", "Ciencia Ficción", "2024-04-12",
     "Épica de ciencia ficción en el desértico planeta Arrakis, donde la "
     "especia melange es el recurso más valioso del universo.", "carlos@bookhub.com", 25),
]

# Favoritos de Ana, del primero al último que agregó. "Mis Favoritos" usa
# ORDER BY created_at DESC, por eso se ve: Dune, Hábitos, El alquimista, 1984.
FAVORITOS_ANA = ["1984", "El alquimista", "Hábitos Atómicos", "Dune"]


def construir_datos():
    """Devuelve (usuarios, libros, favoritos) listos para insertar. No toca la BD."""
    usuarios = list(USUARIOS_PRINCIPALES)
    for i, nombre in enumerate(NOMBRES_RELLENO, start=1):
        usuarios.append((nombre, "Demo", f"usuario{i}@bookhub.com"))

    base = datetime(2024, 9, 1, 10, 0, 0)
    libros = []  # (titulo, autor, genero, fecha, descripcion, email_dueno, created_at)
    todos = [(t, a, g, f, d, "ana@bookhub.com", n) for (t, a, g, f, d, n) in LIBROS_ANA]
    todos += LIBROS_COMUNIDAD
    totales = {}
    for i, (t, a, g, f, d, dueno, n) in enumerate(todos):
        libros.append((t, a, g, f, d, dueno, base + timedelta(hours=i)))
        totales[t] = n

    # Favoritos: para cada libro se toman usuarios distintos a Ana (Carlos, Laura,
    # Miguel, Sofía y Daniel primero, como en el detalle) hasta llegar al total.
    otros = [u[2] for u in usuarios if u[2] != "ana@bookhub.com"]
    inicio_fav = datetime(2024, 9, 10, 9, 0, 0)
    favoritos = []  # (email, titulo, created_at)
    for titulo, total in totales.items():
        con_ana = titulo in FAVORITOS_ANA
        for j, email in enumerate(otros[: total - (1 if con_ana else 0)]):
            favoritos.append((email, titulo, inicio_fav + timedelta(minutes=j)))
    for k, titulo in enumerate(FAVORITOS_ANA):
        favoritos.append(("ana@bookhub.com", titulo, inicio_fav + timedelta(days=1 + k)))
    return usuarios, libros, favoritos


def main():
    import bcrypt
    from config.database import get_connection

    if "--yes" not in sys.argv:
        r = input("Esto BORRA usuarios, libros y favoritos actuales. ¿Continuar? (s/N): ")
        if r.strip().lower() not in ("s", "si", "sí", "y", "yes"):
            print("Cancelado.")
            return

    usuarios, libros, favoritos = construir_datos()
    hash_pw = bcrypt.hashpw(PASSWORD.encode(), bcrypt.gensalt()).decode()

    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute("SET FOREIGN_KEY_CHECKS = 0")
            for tabla in ("favoritos", "libros", "usuarios"):
                cur.execute(f"TRUNCATE TABLE {tabla}")
            cur.execute("SET FOREIGN_KEY_CHECKS = 1")

            ids_usuario = {}
            for nombre, apellido, email in usuarios:
                cur.execute(
                    "INSERT INTO usuarios (nombre, apellido, email, password) VALUES (%s,%s,%s,%s)",
                    (nombre, apellido, email, hash_pw))
                ids_usuario[email] = cur.lastrowid

            ids_libro = {}
            for titulo, autor, genero, fecha, desc, dueno, creado in libros:
                cur.execute(
                    """INSERT INTO libros (titulo, autor, genero, fecha_publicacion, descripcion,
                                           usuario_id, created_at)
                       VALUES (%s,%s,%s,%s,%s,%s,%s)""",
                    (titulo, autor, genero, fecha, desc, ids_usuario[dueno], creado))
                ids_libro[titulo] = cur.lastrowid

            for email, titulo, creado in favoritos:
                cur.execute(
                    "INSERT INTO favoritos (usuario_id, libro_id, created_at) VALUES (%s,%s,%s)",
                    (ids_usuario[email], ids_libro[titulo], creado))
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()

    print(f"Listo: {len(usuarios)} usuarios, {len(libros)} libros, {len(favoritos)} favoritos.")
    print(f"Ingresa con ana@bookhub.com / {PASSWORD}")


if __name__ == "__main__":
    main()
