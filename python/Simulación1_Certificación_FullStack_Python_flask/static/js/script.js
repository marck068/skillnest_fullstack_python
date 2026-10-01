// Rellena el modal de confirmación de borrado con el libro elegido
document.addEventListener("DOMContentLoaded", () => {
  const modal = document.getElementById("modalEliminar");
  if (!modal) return;
  modal.addEventListener("show.bs.modal", (evento) => {
    const enlace = evento.relatedTarget;
    document.getElementById("formEliminar").action = enlace.dataset.url;
    document.getElementById("tituloEliminar").textContent = enlace.dataset.titulo;
  });
});
