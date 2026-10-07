"""Modelo Tarea con consultas para dashboard, detalle y estadísticas."""
from config.database import execute, fetch_all, fetch_one


def crear(usuario_id, datos):
    return execute(
        """INSERT INTO tareas
           (titulo, categoria_id, prioridad, fecha_limite, estado, descripcion, usuario_id)
           VALUES (%s,%s,%s,%s,'Pendiente',%s,%s)""",
        (
            datos["titulo"], datos["categoria_id"], datos["prioridad"],
            datos["fecha_limite"], datos["descripcion"], usuario_id
        ),
        return_id=True,
    )


def actualizar(tarea_id, usuario_id, datos):
    return execute(
        """UPDATE tareas SET titulo=%s, categoria_id=%s, prioridad=%s,
           fecha_limite=%s, descripcion=%s
           WHERE id=%s AND usuario_id=%s""",
        (
            datos["titulo"], datos["categoria_id"], datos["prioridad"],
            datos["fecha_limite"], datos["descripcion"], tarea_id, usuario_id
        ),
    )


def eliminar(tarea_id, usuario_id):
    return execute("DELETE FROM tareas WHERE id=%s AND usuario_id=%s", (tarea_id, usuario_id))


def marcar_completada(tarea_id, usuario_id):
    return execute(
        "UPDATE tareas SET estado='Completada' WHERE id=%s AND usuario_id=%s",
        (tarea_id, usuario_id),
    )


def obtener_por_id(tarea_id, usuario_id):
    return fetch_one(
        """SELECT t.*, c.nombre AS categoria_nombre, u.nombre AS usuario_nombre
           FROM tareas t
           JOIN categorias c ON c.id=t.categoria_id
           JOIN usuarios u ON u.id=t.usuario_id
           WHERE t.id=%s AND t.usuario_id=%s""",
        (tarea_id, usuario_id),
    )


def listar(usuario_id, filtros):
    sql = """SELECT t.*, c.nombre AS categoria_nombre
             FROM tareas t
             JOIN categorias c ON c.id=t.categoria_id
             WHERE t.usuario_id=%s"""
    params = [usuario_id]

    if filtros.get("q"):
        sql += " AND t.titulo LIKE %s"
        params.append(f"%{filtros['q']}%")
    if filtros.get("categoria"):
        sql += " AND t.categoria_id=%s"
        params.append(filtros["categoria"])
    if filtros.get("estado"):
        sql += " AND t.estado=%s"
        params.append(filtros["estado"])
    if filtros.get("prioridad"):
        sql += " AND t.prioridad=%s"
        params.append(filtros["prioridad"])

    sql += """ ORDER BY
               CASE WHEN t.estado='Completada' THEN 1 ELSE 0 END,
               t.fecha_limite ASC, t.id ASC"""
    return fetch_all(sql, tuple(params))


def proximas(usuario_id):
    return fetch_all(
        """SELECT t.id, t.titulo, t.fecha_limite,
                  DATEDIFF(t.fecha_limite, CURDATE()) AS dias_restantes
           FROM tareas t
           WHERE t.usuario_id=%s AND t.estado<>'Completada'
           ORDER BY t.fecha_limite ASC LIMIT 5""",
        (usuario_id,),
    )


def resumen(usuario_id):
    row = fetch_one(
        """SELECT
           COUNT(*) AS total,
           SUM(estado='Pendiente') AS pendientes,
           SUM(estado='En progreso') AS en_progreso,
           SUM(estado='Completada') AS completadas
           FROM tareas WHERE usuario_id=%s""",
        (usuario_id,),
    )
    return {
        "total": row["total"] or 0,
        "pendientes": row["pendientes"] or 0,
        "en_progreso": row["en_progreso"] or 0,
        "completadas": row["completadas"] or 0,
    }
