# BookHub

Plataforma web (Flask + MySQL) donde los usuarios se registran, administran sus libros, exploran los de la comunidad, consultan detalles y los agregan a favoritos. Sigue el wireframe de las 6 pantallas: Login/Registro, Mis Libros, Detalle, Nuevo, Editar y Mis Favoritos.

## Tecnologías
Python 3, Flask, MySQL, PyMySQL, Jinja2, Bootstrap 5 (+ Bootstrap Icons), Bcrypt, HTML5/CSS3/JS, sesiones y mensajes flash de Flask.

## Estructura
```
BookHub/
├── app.py                      # Crea la app, registra blueprints, CSRF y errores
├── config/database.py          # Configuración MySQL centralizada + helpers PyMySQL
├── controllers/                # Rutas (C): auth, libros, favoritos
├── models/                     # Consultas SQL (M): usuario, libro, favorito
├── utils/                      # login_required y validaciones de backend
├── templates/                  # Vistas Jinja2 (V): base, auth, libros, favoritos, errors
├── static/css|js/              # style.css, script.js
├── database/bookhub.sql        # Script de creación de la BD
├── resources/BookHub_ERD.png   # ERD (se regenera con resources/generar_erd.py)
├── requirements.txt  .env.example  .gitignore
```

## Instalación y ejecución
```bash
python -m venv venv
venv\Scripts\activate          # Linux/Mac: source venv/bin/activate
pip install -r requirements.txt
```
1. **Crear la base de datos:** `mysql -u root -p < database/bookhub.sql`
2. **Configurar MySQL:** copia `.env.example` a `.env` y completa `DB_HOST`, `DB_USER`, `DB_PASSWORD`, `DB_NAME` y `SECRET_KEY`.
3. **Ejecutar:** `python app.py` y abre http://localhost:5000

## Autenticación
- Registro con validación de campos, email válido y único, contraseña ≥ 8 caracteres y confirmación igual.
- La contraseña se guarda como hash **Bcrypt** (`bcrypt.hashpw`) y el login usa `bcrypt.checkpw`.
- Al iniciar sesión se guarda `session["usuario_id"]` (y el nombre) y se redirige a `/libros`. `/logout` limpia la sesión.
- El decorador `@login_required` protege todas las rutas privadas: sin sesión redirige al login con un mensaje flash.

## CRUD de libros
- `/libros` muestra **Mis Libros** (solo los del usuario) y **Libros de la Comunidad** (de otros). `/explorar` lista la comunidad.
- `/libros/nuevo`, `/libros/editar/<id>`, `/libros/eliminar/<id>` (POST con modal de confirmación) y `/libros/<id>` (detalle).
- El libro se asocia siempre al usuario de la sesión; nunca se acepta un `usuario_id` del formulario.

## Favoritos
- `POST /libros/<id>/favorito` crea la relación usuario–libro; la restricción `UNIQUE(usuario_id, libro_id)` y una comprobación previa evitan duplicados.
- El detalle muestra el total y la lista de usuarios (leída de MySQL) y reemplaza el botón por «En tus favoritos» si ya lo agregaste. `/favoritos` lista tus favoritos.

## Relaciones entre tablas
`usuarios 1:N libros`, `usuarios 1:N favoritos`, `libros 1:N favoritos` (relación N:M entre usuarios y libros resuelta con `favoritos`). Todas con claves foráneas `ON DELETE CASCADE`. ERD en `resources/BookHub_ERD.png`.

## Validaciones (backend, `utils/validaciones.py`)
Campos vacíos, longitudes, formato de email, email duplicado, contraseñas iguales, género dentro de la lista, descripción ≥ 10 caracteres, fecha válida y **no pasada** (regla del wireframe; al editar se permite conservar la fecha original), existencia y propiedad del libro.

## Seguridad
Bcrypt, consultas parametrizadas (sin SQL Injection), verificación de propiedad en el backend al editar/eliminar (el `WHERE` también incluye `usuario_id`), token CSRF en todos los POST, Jinja2 con autoescape, credenciales fuera del código (`.env`), páginas de error 400/404/500.

## Arquitectura MVC
Modelos (`models/`) = SQL; Controladores (`controllers/`, Blueprints) = lógica y rutas; Vistas (`templates/`) = Jinja2 + Bootstrap. `config/` y `utils/` dan soporte compartido.
