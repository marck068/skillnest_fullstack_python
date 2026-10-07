"""Conexión centralizada a MySQL usando PyMySQL."""
import os
import pymysql
from pymysql.cursors import DictCursor

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

DB_HOST = os.getenv("DB_HOST", os.getenv("MYSQL_HOST", "localhost"))
DB_PORT = int(os.getenv("DB_PORT", os.getenv("MYSQL_PORT", "3306")))
DB_USER = os.getenv("DB_USER", os.getenv("MYSQL_USER", "root"))
DB_PASSWORD = os.getenv("DB_PASSWORD", os.getenv("MYSQL_PASSWORD", "1234"))
DB_NAME = os.getenv("DB_NAME", "tasktrack")
SECRET_KEY = os.getenv("SECRET_KEY", "tasktrack-clave-desarrollo")


def get_connection():
    """Abre una conexión nueva a la base de datos."""
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
