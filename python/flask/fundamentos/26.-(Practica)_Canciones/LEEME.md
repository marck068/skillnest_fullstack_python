# canciones_app

Flask + MySQL (PyMySQL), arquitectura MVC. Relación N:N usuarios ↔ canciones mediante `favoritos`.

## Puesta en marcha
1. Ejecuta `resources/esquema_canciones.sql` en MySQL Workbench (crea `esquema_canciones`).
2. `pipenv install flask pymysql` (genera el `Pipfile.lock`).
3. Ajusta credenciales si hace falta: variables `DB_HOST`, `DB_USER`, `DB_PASSWORD`.
4. `pipenv run python server.py` y abre http://127.0.0.1:5000/usuarios

## Pendiente antes de entregar
- Guardar el ERD (`resources/esquema_canciones_erd.mwb`) desde Workbench: Database → Reverse Engineer.
- Subir a GitHub con `Pipfile.lock` y una captura de la app funcionando.
