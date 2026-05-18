import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent / "users_messages.db"

schema = """
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    contrasena TEXT NOT NULL,
    tipo_usuario TEXT NOT NULL CHECK(tipo_usuario IN ('Administrador', 'Usuario')) DEFAULT 'Usuario',
    creado_en TEXT DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS mensajes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario_id INTEGER NOT NULL,
    contenido TEXT NOT NULL,
    creado_en TEXT DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS comentarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    mensaje_id INTEGER NOT NULL,
    usuario_id INTEGER NOT NULL,
    contenido TEXT NOT NULL,
    creado_en TEXT DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (mensaje_id) REFERENCES mensajes(id) ON DELETE CASCADE,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE CASCADE
);
"""

sample_data = [
    ("Patricia", "patricia@codingdojo.com", "admin123", "Administrador"),
    ("Andrea", "andrea@codingdojo.com", "user123", "Usuario"),
    ("Katya", "katya@codingdojo.com", "user123", "Usuario"),
]

with sqlite3.connect(DB_PATH) as conn:
    cursor = conn.cursor()
    cursor.executescript(schema)
    cursor.executemany(
        "INSERT OR IGNORE INTO usuarios (nombre, email, contrasena, tipo_usuario) VALUES (?, ?, ?, ?);",
        sample_data,
    )
    cursor.execute(
        "INSERT OR IGNORE INTO mensajes (usuario_id, contenido) VALUES (?, ?);",
        (2, "Mensaje de ejemplo para Andrea."),
    )
    cursor.execute(
        "INSERT OR IGNORE INTO comentarios (mensaje_id, usuario_id, contenido) VALUES (?, ?, ?);",
        (1, 1, "Comentario de Patricia."),
    )
    conn.commit()

print(f"Base de datos creada en: {DB_PATH}")
