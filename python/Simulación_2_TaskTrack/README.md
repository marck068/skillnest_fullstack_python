# TaskTrack

Aplicación web de gestión de tareas desarrollada con Flask, MySQL, PyMySQL, Jinja2 y Bootstrap 5.

## Diseño

La interfaz está basada en el wireframe entregado:
- login y registro en dos columnas;
- barra superior oscura;
- dashboard "Mis Tareas";
- buscador y filtros;
- tabla de tareas con prioridad, estado y acciones;
- sección "Próximas tareas";
- panel "Resumen";
- detalle de tarea con nota amarilla;
- formularios de nueva/edición;
- gestión de categorías.

Los dos proyectos ZIP usados como referencia se tomaron principalmente como referencia de estructura Flask, MVC modular, conexión MySQL, autenticación, validaciones, plantillas Jinja2 y estilo tipo wireframe.

## Funcionalidades

- Registro e inicio de sesión con contraseña cifrada con bcrypt.
- Protección de rutas con decorador `login_required`.
- Protección CSRF básica para formularios POST.
- CRUD de tareas.
- Filtros por título, categoría, estado y prioridad.
- Orden ascendente por fecha límite.
- Resumen de tareas.
- Próximas tareas.
- CRUD de categorías propias.
- Detalle de tarea.
- Marcar tarea como completada.
- Comentarios de las tareas propias.
- Validaciones de backend.
- Restricción de datos por usuario.

## Estructura

```text
TaskTrack/
├── app.py
├── config/
│   └── database.py
├── controllers/
│   ├── auth_controller.py
│   ├── categorias_controller.py
│   └── tareas_controller.py
├── models/
│   ├── usuario.py
│   ├── categoria.py
│   ├── tarea.py
│   └── comentario.py
├── templates/
├── static/
├── database/
│   └── tasktrack.sql
├── resources/
├── requirements.txt
├── .env.example
└── README.md
```

## Instalación

1. Crear un entorno virtual:
   `python -m venv venv`
2. Activarlo.
3. Instalar:
   `pip install -r requirements.txt`
4. Iniciar MySQL (por ejemplo, MySQL de XAMPP). La aplicación crea automáticamente la base de datos `tasktrack`, sus tablas y una cuenta demo.
5. `.env` es opcional: solo úsalo si tu MySQL tiene usuario/contraseña diferentes a `root` sin contraseña.
6. Ejecutar:
   `python app.py`
7. Abrir:
   `http://localhost:5000`

## Cuenta demo

- E-mail: `marcelo@tasktrack.cl`
- Contraseña: `password`

## Nota

Si se desea usar el proyecto en GitHub, no se debe subir `.env`. Utiliza `.env.example` como plantilla.
