"""Genera resources/BookHub_ERD.png (requiere matplotlib)."""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle

TABLAS = {
    "USUARIOS": (0.5, 1.2, ["PK  id", "     nombre", "     apellido", "UQ  email", "     password (hash Bcrypt)", "     created_at"]),
    "LIBROS": (6.4, 1.2, ["PK  id", "     titulo", "     autor", "     genero", "     fecha_publicacion", "     descripcion", "     imagen", "FK  usuario_id", "     created_at"]),
    "FAVORITOS": (12.3, 2.2, ["PK  id", "FK  usuario_id", "FK  libro_id", "     created_at", "UQ  (usuario_id, libro_id)"]),
}
ANCHO, ALTO_FILA, ALTO_TIT = 3.6, 0.42, 0.55

fig, ax = plt.subplots(figsize=(17, 6.5))
ax.set_xlim(0, 17); ax.set_ylim(0, 6.2); ax.axis("off")
centros = {}
for nombre, (x, y, campos) in TABLAS.items():
    alto = ALTO_TIT + ALTO_FILA * len(campos)
    ax.add_patch(Rectangle((x, y), ANCHO, alto, fc="white", ec="#333", lw=1.6))
    ax.add_patch(Rectangle((x, y + alto - ALTO_TIT), ANCHO, ALTO_TIT, fc="#333", ec="#333"))
    ax.text(x + ANCHO / 2, y + alto - ALTO_TIT / 2, nombre, color="white", ha="center", va="center", fontsize=13, fontweight="bold")
    for i, c in enumerate(campos):
        yy = y + alto - ALTO_TIT - ALTO_FILA * (i + 0.5)
        peso = "bold" if c[:2] in ("PK", "FK", "UQ") else "normal"
        ax.text(x + 0.2, yy, c, fontsize=10.5, va="center", family="monospace", fontweight=peso)
    centros[nombre] = (x, y, alto)

def relacion(x1, x2, y, etiqueta1, etiqueta2, texto):
    ax.annotate("", xy=(x2, y), xytext=(x1, y), arrowprops=dict(arrowstyle="-", lw=1.8, color="#1f5fbf"))
    ax.text(x1 + 0.12, y + 0.12, etiqueta1, color="#1f5fbf", fontsize=12, fontweight="bold")
    ax.text(x2 - 0.45, y + 0.12, etiqueta2, color="#1f5fbf", fontsize=12, fontweight="bold")
    ax.text((x1 + x2) / 2, y - 0.3, texto, ha="center", fontsize=9.5, color="#1f5fbf")

ux = TABLAS["USUARIOS"][0] + ANCHO; lx = TABLAS["LIBROS"][0]
relacion(ux, lx, 3.6, "1", "N", "crea (usuario_id)")
lx2 = TABLAS["LIBROS"][0] + ANCHO; fx = TABLAS["FAVORITOS"][0]
relacion(lx2, fx, 3.6, "1", "N", "es marcado (libro_id)")

# USUARIOS 1:N FAVORITOS (línea por debajo)
ax.plot([2.3, 2.3, 14.1, 14.1], [1.2, 0.6, 0.6, 2.2], color="#1f5fbf", lw=1.8)
ax.text(2.4, 0.75, "1", color="#1f5fbf", fontsize=12, fontweight="bold")
ax.text(14.2, 1.9, "N", color="#1f5fbf", fontsize=12, fontweight="bold")
ax.text(8.2, 0.3, "agrega a favoritos (usuario_id)", ha="center", fontsize=9.5, color="#1f5fbf")

ax.text(8.5, 5.95, "BookHub - Modelo Entidad-Relación", ha="center", fontsize=16, fontweight="bold")
os.makedirs(os.path.dirname(os.path.abspath(__file__)), exist_ok=True)
fig.savefig(os.path.join(os.path.dirname(os.path.abspath(__file__)), "BookHub_ERD.png"), dpi=150, bbox_inches="tight")
