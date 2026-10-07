"""Conexión MySQL de TaskTrack.

La aplicación funciona con una configuración simple por defecto:
MySQL en localhost, puerto 3306, usuario root y contraseña vacía.
Si el usuario tiene otra configuración, puede definirla en .env, pero .env
NO es obligatorio para ejecutar el proyecto con la configuración habitual de XAMPP/WAMP.
"""
import os
import pymysql
from pymysql.cursors import DictCursor

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = int(os.getenv("DB_PORT", "3306"))
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")
DB_NAME = os.getenv("DB_NAME", "tasktrack")
SECRET_KEY = os.getenv("SECRET_KEY", "tasktrack-clave-desarrollo")


# Esquema mínimo necesario para que TaskTrack arranque sin importar un SQL manualmente.
SCHEMA = [
    """CREATE TABLE IF NOT EXISTS usuarios (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(50) NOT NULL,
        apellido VARCHAR(50) NOT NULL,
        email VARCHAR(120) NOT NULL UNIQUE,
        password VARCHAR(255) NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    ) ENGINE=InnoDB""",
    """CREATE TABLE IF NOT EXISTS categorias (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(50) NOT NULL,
        usuario_id INT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        UNIQUE KEY uq_categoria_usuario (usuario_id, nombre),
        CONSTRAINT fk_categoria_usuario FOREIGN KEY (usuario_id)
            REFERENCES usuarios(id) ON DELETE CASCADE
    ) ENGINE=InnoDB""",
    """CREATE TABLE IF NOT EXISTS tareas (
        id INT AUTO_INCREMENT PRIMARY KEY,
        titulo VARCHAR(120) NOT NULL,
        categoria_id INT NOT NULL,
        prioridad ENUM('Alta','Media','Baja') NOT NULL DEFAULT 'Media',
        fecha_limite DATE NOT NULL,
        estado ENUM('Pendiente','En progreso','Completada') NOT NULL DEFAULT 'Pendiente',
        descripcion TEXT NOT NULL,
        usuario_id INT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        INDEX idx_tareas_usuario_fecha (usuario_id, fecha_limite),
        CONSTRAINT fk_tarea_categoria FOREIGN KEY (categoria_id)
            REFERENCES categorias(id) ON DELETE RESTRICT,
        CONSTRAINT fk_tarea_usuario FOREIGN KEY (usuario_id)
            REFERENCES usuarios(id) ON DELETE CASCADE
    ) ENGINE=InnoDB""",
    """CREATE TABLE IF NOT EXISTS comentarios (
        id INT AUTO_INCREMENT PRIMARY KEY,
        tarea_id INT NOT NULL,
        usuario_id INT NOT NULL,
        texto VARCHAR(500) NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        CONSTRAINT fk_comentario_tarea FOREIGN KEY (tarea_id)
            REFERENCES tareas(id) ON DELETE CASCADE,
        CONSTRAINT fk_comentario_usuario FOREIGN KEY (usuario_id)
            REFERENCES usuarios(id) ON DELETE CASCADE
    ) ENGINE=InnoDB""",
]


def _server_connection():
    """Conecta a MySQL sin seleccionar todavía la base de datos."""
    return pymysql.connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASSWORD,
        charset="utf8mb4",
        cursorclass=DictCursor,
        autocommit=True,
    )


def ensure_database():
    """Crea la BD/tablas y datos demo si todavía no existen."""
    conn = _server_connection()
    try:
        with conn.cursor() as cur:
            cur.execute(
                f"CREATE DATABASE IF NOT EXISTS `{DB_NAME}` "
                "CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci"
            )
    finally:
        conn.close()

    conn = get_connection()
    try:
        with conn.cursor() as cur:
            for statement in SCHEMA:
                cur.execute(statement)

            # Cuenta demo. Password: password
            cur.execute("SELECT id FROM usuarios WHERE email=%s", ("marcelo@tasktrack.cl",))
            usuario = cur.fetchone()
            if not usuario:
                cur.execute(
                    "INSERT INTO usuarios (nombre, apellido, email, password) VALUES (%s,%s,%s,%s)",
                    (
                        "Marcelo", "Rios", "marcelo@tasktrack.cl",
                        "$2a$10$N9qo8uLOickgx2ZMRZoMyeIjZAgcfl7p92ldGxad68LJZdL17lhWy",
                    ),
                )
                usuario_id = cur.lastrowid
                for nombre in ("Estudios", "Trabajo", "Salud", "Personal"):
                    cur.execute(
                        "INSERT INTO categorias (nombre, usuario_id) VALUES (%s,%s)",
                        (nombre, usuario_id),
                    )
                cur.execute("SELECT id FROM categorias WHERE nombre='Estudios' AND usuario_id=%s", (usuario_id,))
                estudios = cur.fetchone()["id"]
                cur.execute(
                    "INSERT INTO tareas (titulo,categoria_id,prioridad,fecha_limite,estado,descripcion,usuario_id) "
                    "VALUES (%s,%s,'Alta',DATE_ADD(CURDATE(),INTERVAL 3 DAY),'Pendiente',%s,%s)",
                    (
                        "Estudiar Flask", estudios,
                        "Repasar las rutas, modelos y controladores para el proyecto final de certificación.",
                        usuario_id,
                    ),
                )
    finally:
        conn.close()


def get_connection():
    """Abre una conexión a la base de datos TaskTrack."""
    return pymysql.connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME,
        charset="utf8mb4",
        cursorclass=DictCursor,
        autocommit=False,
    )


def fetch_all(sql, params=()):
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute(sql, params)
            return cur.fetchall()
    finally:
        conn.close()


def fetch_one(sql, params=()):
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute(sql, params)
            return cur.fetchone()
    finally:
        conn.close()


def execute(sql, params=(), return_id=False):
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute(sql, params)
            result = cur.lastrowid if return_id else cur.rowcount
        conn.commit()
        return result
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()
