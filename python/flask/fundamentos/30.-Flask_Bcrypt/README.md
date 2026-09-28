# Login y Registro con Flask + Flask-Bcrypt + MySQL

## Puesta en marcha
1. Crear la base de datos:
   `mysql -u root -p < esquema_loginreg.sql`
2. Instalar dependencias:
   `pipenv install`
3. (Opcional) Configurar credenciales de MySQL, por defecto root/root en localhost:
   `export DB_USER=root DB_PASSWORD=tu_clave DB_HOST=localhost`
4. Ejecutar:
   `pipenv run python server.py` y abrir http://localhost:5000

## Estructura
- `server.py`: punto de entrada
- `flask_app/__init__.py`: crea la app y la secret_key
- `flask_app/config/mysqlconnection.py`: conexión a MySQL (PyMySQL)
- `flask_app/models/usuario.py`: consultas y validaciones
- `flask_app/controllers/usuarios.py`: rutas (/, /registrar, /login, /dashboard, /logout)
- `flask_app/templates/`: index.html y dashboard.html
