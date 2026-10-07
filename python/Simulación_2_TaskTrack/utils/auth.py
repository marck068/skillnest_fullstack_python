"""Decorador para proteger las rutas privadas."""
from functools import wraps
from flask import flash, redirect, session, url_for
from models.usuario import obtener_por_id


def login_required(vista):
    @wraps(vista)
    def envoltura(*args, **kwargs):
        usuario_id = session.get("usuario_id")
        if not usuario_id or not obtener_por_id(usuario_id):
            session.clear()
            flash("Debes iniciar sesión para acceder.", "danger")
            return redirect(url_for("auth.login"))
        return vista(*args, **kwargs)
    return envoltura
