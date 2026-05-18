from pathlib import Path
import sqlite3
from flask import Flask, render_template, request, redirect, url_for, flash, session, g

app = Flask(__name__, static_folder="static", template_folder="templates")
app.secret_key = "cambio_esta_clave_por_una_segura"

DB_PATH = Path(__file__).resolve().parent / "users_messages.db"


def get_db():
    if "db" not in g:
        connection = sqlite3.connect(DB_PATH)
        connection.row_factory = sqlite3.Row
        g.db = connection
    return g.db


@app.teardown_appcontext
def close_db(error=None):
    db = g.pop("db", None)
    if db is not None:
        db.close()


def require_login():
    if not session.get("user_id"):
        flash("Debe iniciar sesión para acceder.", "error")
        return False
    return True


def require_admin():
    if session.get("user_role") != "Administrador":
        flash("Solo los administradores pueden acceder a esta página.", "error")
        return False
    return True


@app.route("/")
def index():
    if session.get("user_id"):
        return redirect(url_for("dashboard"))
    return render_template("index.html")


@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip().lower()
    password = request.form.get("password", "")
    confirm_password = request.form.get("confirmPassword", "")

    if not name or not email or not password or not confirm_password:
        flash("Complete todos los campos.", "error")
        return redirect(url_for("index"))

    if password != confirm_password:
        flash("Las contraseñas no coinciden.", "error")
        return redirect(url_for("index"))

    db = get_db()
    try:
        db.execute(
            "INSERT INTO usuarios (nombre, email, contrasena, tipo_usuario) VALUES (?, ?, ?, ?)",
            (name, email, password, "Usuario"),
        )
        db.commit()
    except sqlite3.IntegrityError:
        flash("El correo ya está registrado.", "error")
        return redirect(url_for("index"))

    flash("Registro exitoso. Inicie sesión.", "success")
    return redirect(url_for("index"))


@app.route("/login", methods=["POST"])
def login():
    email = request.form.get("loginEmail", "").strip().lower()
    password = request.form.get("loginPassword", "")

    db = get_db()
    user = db.execute(
        "SELECT id, nombre, tipo_usuario FROM usuarios WHERE email = ? AND contrasena = ?",
        (email, password),
    ).fetchone()

    if not user:
        flash("Correo o contraseña incorrectos.", "error")
        return redirect(url_for("index"))

    session["user_id"] = user["id"]
    session["user_name"] = user["nombre"]
    session["user_role"] = user["tipo_usuario"]

    if user["tipo_usuario"] == "Administrador":
        return redirect(url_for("dashboard_admin"))

    return redirect(url_for("dashboard"))


@app.route("/logout")
def logout():
    session.clear()
    flash("Sesión cerrada.", "success")
    return redirect(url_for("index"))


@app.route("/dashboard")
def dashboard():
    if not require_login():
        return redirect(url_for("index"))

    db = get_db()
    users = db.execute(
        "SELECT id, nombre, email, tipo_usuario FROM usuarios ORDER BY id"
    ).fetchall()
    return render_template(
        "dashboard.html",
        user_name=session.get("user_name"),
        users=users,
    )


@app.route("/dashboard_admin")
def dashboard_admin():
    if not require_login() or not require_admin():
        return redirect(url_for("index"))

    db = get_db()
    users = db.execute(
        "SELECT id, nombre, email, tipo_usuario FROM usuarios ORDER BY id"
    ).fetchall()
    return render_template(
        "dashboard_admin.html",
        user_name=session.get("user_name"),
        users=users,
    )


@app.route("/new_user", methods=["GET", "POST"])
def new_user():
    if not require_login() or not require_admin():
        return redirect(url_for("index"))

    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")
        confirm_password = request.form.get("confirmPassword", "")
        role = request.form.get("role", "Usuario")

        if not name or not email or not password or not confirm_password:
            flash("Complete todos los campos.", "error")
            return redirect(url_for("new_user"))

        if password != confirm_password:
            flash("Las contraseñas no coinciden.", "error")
            return redirect(url_for("new_user"))

        db = get_db()
        try:
            db.execute(
                "INSERT INTO usuarios (nombre, email, contrasena, tipo_usuario) VALUES (?, ?, ?, ?)",
                (name, email, password, role),
            )
            db.commit()
        except sqlite3.IntegrityError:
            flash("El correo ya está registrado.", "error")
            return redirect(url_for("new_user"))

        flash("Usuario creado correctamente.", "success")
        return redirect(url_for("dashboard_admin"))

    return render_template("usuario_nuevo.html", user_name=session.get("user_name"))


@app.route("/edit_user/<int:user_id>", methods=["GET", "POST"])
def edit_user(user_id):
    if not require_login() or not require_admin():
        return redirect(url_for("index"))

    db = get_db()
    user = db.execute("SELECT * FROM usuarios WHERE id = ?", (user_id,)).fetchone()
    if not user:
        flash("Usuario no encontrado.", "error")
        return redirect(url_for("dashboard_admin"))

    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")
        confirm_password = request.form.get("confirmPassword", "")
        role = request.form.get("role", "Usuario")

        if not name or not email:
            flash("Complete todos los campos.", "error")
            return redirect(url_for("edit_user", user_id=user_id))

        if password != confirm_password:
            flash("Las contraseñas no coinciden.", "error")
            return redirect(url_for("edit_user", user_id=user_id))

        update_query = "UPDATE usuarios SET nombre = ?, email = ?, tipo_usuario = ?"
        params = [name, email, role]

        if password:
            update_query += ", contrasena = ?"
            params.append(password)

        update_query += " WHERE id = ?"
        params.append(user_id)

        try:
            db.execute(update_query, params)
            db.commit()
        except sqlite3.IntegrityError:
            flash("El correo ya está registrado.", "error")
            return redirect(url_for("edit_user", user_id=user_id))

        flash("Usuario actualizado correctamente.", "success")
        return redirect(url_for("dashboard_admin"))

    return render_template("usuario_editar.html", user=user, user_name=session.get("user_name"))


@app.route("/delete_user/<int:user_id>", methods=["POST"])
def delete_user(user_id):
    if not require_login() or not require_admin():
        return redirect(url_for("index"))

    db = get_db()
    db.execute("DELETE FROM usuarios WHERE id = ?", (user_id,))
    db.commit()
    flash("Usuario eliminado correctamente.", "success")
    return redirect(url_for("dashboard_admin"))


if __name__ == "__main__":
    app.run(debug=True)
