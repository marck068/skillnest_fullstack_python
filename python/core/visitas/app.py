from flask import Flask, render_template, session, redirect, url_for, request

app = Flask(__name__)
# Clave secreta necesaria para poder usar sesiones en Flask
app.secret_key = 'clave_secreta_super_segura_123'


@app.route('/')
def index():
    # --- Nivel 1: comprobar si existe la sesión de visitas ---
    if 'visitas' not in session:
        # Si no existe, la inicializamos en 0
        session['visitas'] = 0

    # --- Nivel 3 (bonus oro): comprobar si existe el contador de reinicios ---
    if 'reinicios' not in session:
        session['reinicios'] = 0

    # Solo contamos una "visita" nueva si el usuario llegó a "/" navegando
    # de verdad (escribiendo la URL, recargando, etc). Si llegó aquí porque
    # venimos de un redirect de sumar_dos, reiniciar o sumar_personalizado,
    # la bandera 'accion' estará presente y NO sumamos visita extra, para
    # que sumar +2 sume exactamente +2 y no +3.
    if 'accion' in session:
        session.pop('accion')
    else:
        session['visitas'] += 1

    return render_template(
        'index.html',
        visitas=session['visitas'],
        reinicios=session['reinicios']
    )


@app.route('/destruir_sesion')
def destruir_sesion():
    # Elimina TODA la información guardada en sesión
    session.clear()
    return redirect(url_for('index'))


@app.route('/sumar_dos')
def sumar_dos():
    # --- Nivel 2 (bonus plata): botón que suma +2 a las visitas ---
    if 'visitas' in session:
        session['visitas'] += 2
    else:
        session['visitas'] = 2

    # Marcamos que este redirect viene de una acción, no de una visita real
    session['accion'] = True
    return redirect(url_for('index'))


@app.route('/reiniciar')
def reiniciar():
    # --- Nivel 2 (bonus plata): botón que reinicia visitas a 0 ---
    session['visitas'] = 0

    # --- Nivel 3 (bonus oro): contamos cuántas veces se ha reiniciado ---
    if 'reinicios' in session:
        session['reinicios'] += 1
    else:
        session['reinicios'] = 1

    session['accion'] = True
    return redirect(url_for('index'))


@app.route('/sumar_personalizado', methods=['POST'])
def sumar_personalizado():
    # --- Nivel 3: formulario que suma una cantidad ingresada por el usuario ---
    cantidad = request.form.get('cantidad', 0)

    try:
        cantidad = int(cantidad)
    except ValueError:
        cantidad = 0

    if 'visitas' in session:
        session['visitas'] += cantidad
    else:
        session['visitas'] = cantidad

    session['accion'] = True
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)