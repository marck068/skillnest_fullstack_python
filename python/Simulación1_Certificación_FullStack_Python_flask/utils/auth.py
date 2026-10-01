"""Decorador para proteger rutas privadas."""
from functools import wraps

from flask import flash, redirect, session, url_for

from models import usuario as Usuario


def login_required(vista):
    @wraps(vista)
    def envoltura(*args, **kwargs):
        usuario_id = session.get("usuario_id")
        if not usuario_id:
            flash("Debes iniciar sesión para acceder.", "danger")
            return redirect(url_for("auth.login"))
        if Usuario.obtener_por_id(usuario_id) is None:  # usuario borrado o sesión inválida
            session.clear()
            flash("Debes iniciar sesión para acceder.", "danger")
            return redirect(url_for("auth.login"))
        return vista(*args, **kwargs)
    return envoltura
