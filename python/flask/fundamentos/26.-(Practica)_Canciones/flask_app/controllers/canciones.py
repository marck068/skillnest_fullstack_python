from flask import flash, redirect, render_template, request, url_for

from flask_app import app
from flask_app.models.cancion import Cancion
from flask_app.models.favorito import Favorito
from flask_app.models.usuario import Usuario


def _campo(nombre):
    """Lee un campo del formulario sin espacios sobrantes."""
    return request.form.get(nombre, "").strip()


# ==========================================================
# USUARIOS
# ==========================================================

@app.route("/")
def inicio():
    return redirect(url_for("usuarios"))


@app.route("/usuarios")
def usuarios():
    """Formulario de nuevo usuario + listado de todos los usuarios."""
    return render_template("usuarios.html", usuarios=Usuario.get_all())


@app.route("/usuarios/crear", methods=["POST"])
def crear_usuario():
    nombre = _campo("nombre")
    email = _campo("email")
    contrasena = _campo("contrasena")

    if not nombre or not email or not contrasena:
        flash("Todos los campos son obligatorios.", "danger")
        return redirect(url_for("usuarios"))

    if max(len(nombre), len(email), len(contrasena)) > 45:
        flash("Ningún campo puede superar los 45 caracteres.", "danger")
        return redirect(url_for("usuarios"))

    resultado = Usuario.save({
        "nombre": nombre,
        "email": email,
        "contrasena": contrasena,
    })

    if resultado is False:
        flash("No fue posible crear el usuario.", "danger")
    else:
        flash("Usuario creado correctamente.", "success")

    # Patrón Post/Redirect/Get: evita reenvíos al refrescar.
    return redirect(url_for("usuarios"))


@app.route("/usuarios/<int:id>")
def mostrar_usuario(id):
    """Un usuario, sus canciones favoritas y el select para agregar más."""
    usuario = Usuario.get_by_id_with_favorites({"id": id})

    if usuario is None:
        return "Usuario no encontrado", 404

    return render_template(
        "mostrar_usuario.html",
        usuario=usuario,
        canciones=Cancion.get_all(),
    )


# ==========================================================
# CANCIONES
# ==========================================================

@app.route("/canciones")
def canciones():
    """Formulario de nueva canción + listado de todas las canciones."""
    return render_template("canciones.html", canciones=Cancion.get_all())


@app.route("/canciones/crear", methods=["POST"])
def crear_cancion():
    titulo = _campo("titulo")
    artista = _campo("artista")

    if not titulo or not artista:
        flash("Título y artista son obligatorios.", "danger")
        return redirect(url_for("canciones"))

    if max(len(titulo), len(artista)) > 45:
        flash("Ningún campo puede superar los 45 caracteres.", "danger")
        return redirect(url_for("canciones"))

    resultado = Cancion.save({"titulo": titulo, "artista": artista})

    if resultado is False:
        flash("No fue posible crear la canción.", "danger")
    else:
        flash("Canción creada correctamente.", "success")

    return redirect(url_for("canciones"))


@app.route("/canciones/<int:id>")
def mostrar_cancion(id):
    """Una canción, los usuarios que la tienen y el select (BONUS)."""
    cancion = Cancion.get_by_id_with_users({"id": id})

    if cancion is None:
        return "Canción no encontrada", 404

    return render_template(
        "mostrar_cancion.html",
        cancion=cancion,
        usuarios=Cancion.get_users_not_favorited({"cancion_id": id}),
    )


# ==========================================================
# FAVORITOS
# ==========================================================

@app.route("/favoritos/agregar", methods=["POST"])
def agregar_favorito():
    """
    Crea la relación usuario-canción. El campo oculto "origen"
    indica a qué página volver (usuario o cancion).
    """
    origen = request.form.get("origen")

    try:
        usuario_id = int(request.form.get("usuario_id", ""))
        cancion_id = int(request.form.get("cancion_id", ""))
    except ValueError:
        flash("Debes seleccionar una opción válida.", "danger")
        return redirect(url_for("usuarios"))

    if Usuario.get_by_id(usuario_id) is None:
        flash("El usuario seleccionado no existe.", "danger")
        return redirect(url_for("usuarios"))

    if Cancion.get_by_id(cancion_id) is None:
        flash("La canción seleccionada no existe.", "danger")
        return redirect(url_for("canciones"))

    data = {"usuario_id": usuario_id, "cancion_id": cancion_id}

    if Favorito.existe(data):
        flash("Esta canción ya está entre los favoritos del usuario.", "warning")
    elif Favorito.agregar(data) is False:
        flash("No fue posible agregar el favorito.", "danger")
    else:
        flash("Favorito agregado correctamente.", "success")

    if origen == "usuario":
        return redirect(url_for("mostrar_usuario", id=usuario_id))

    if origen == "cancion":
        return redirect(url_for("mostrar_cancion", id=cancion_id))

    return redirect(url_for("usuarios"))
