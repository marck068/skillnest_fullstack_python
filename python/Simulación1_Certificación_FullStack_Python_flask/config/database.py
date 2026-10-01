"""Configuración centralizada de MySQL y helpers de consulta (PyMySQL)."""
import os

import pymysql
from pymysql.cursors import DictCursor

try:  # carga el archivo .env si python-dotenv está instalado
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = int(os.getenv("DB_PORT", "3306"))
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "1234")
DB_NAME = os.getenv("DB_NAME", "bookhub")
SECRET_KEY = os.getenv("SECRET_KEY", "clave-solo-para-desarrollo")


def get_connection():
    """Abre una conexión nueva a MySQL."""
    return pymysql.connect(
        host=DB_HOST, port=DB_PORT, user=DB_USER, password=DB_PASSWORD,
        database=DB_NAME, charset="utf8mb4", cursorclass=DictCursor,
    )


def fetch_all(sql, params=()):
    """Devuelve todas las filas de un SELECT como lista de diccionarios."""
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute(sql, params)
            return cur.fetchall()
    finally:
        conn.close()


def fetch_one(sql, params=()):
    """Devuelve una fila (diccionario) o None."""
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute(sql, params)
            return cur.fetchone()
    finally:
        conn.close()


def execute(sql, params=(), return_id=False):
    """Ejecuta INSERT/UPDATE/DELETE con commit. Devuelve el id nuevo o las filas afectadas."""
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute(sql, params)
            resultado = cur.lastrowid if return_id else cur.rowcount
        conn.commit()
        return resultado
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()
