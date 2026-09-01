# Visitas — Práctica de sesiones en Flask

Aplicación Flask que cuenta la cantidad de veces que un cliente ha visitado
el sitio, usando `session` de Flask.

## Cómo correrlo

```bash
pip install -r requirements.txt
python app.py
```

Luego abre: http://127.0.0.1:5000/

## Rutas

- `GET /` → muestra la cantidad de visitas y la cantidad de veces que se ha
  reiniciado el contador.
- `GET /destruir_sesion` → elimina toda la sesión (`session.clear()`) y
  redirige a `/`.
- `GET /sumar_dos` → suma 2 al contador de visitas (bonus plata).
- `GET /reiniciar` → reinicia el contador de visitas a 0 y aumenta el
  contador de reinicios (bonus plata + bonus oro).
- `POST /sumar_personalizado` → recibe un número desde un formulario y lo
  suma al contador de visitas (bonus oro).

## Conceptos practicados

- Comprobar existencia de una propiedad en `session` (`in session`).
- Inicializar valores en sesión.
- Editar/actualizar valores existentes en sesión.
- Eliminar sesión completa con `session.clear()`.
- Formularios HTML con método POST y `request.form`.