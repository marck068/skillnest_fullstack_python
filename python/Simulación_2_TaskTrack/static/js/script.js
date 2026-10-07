document.addEventListener("DOMContentLoaded", () => {
    // Autocierre suave de mensajes flash después de unos segundos.
    window.setTimeout(() => {
        document.querySelectorAll(".flash-alert").forEach((alerta) => {
            if (window.bootstrap) {
                bootstrap.Alert.getOrCreateInstance(alerta).close();
            }
        });
    }, 4500);
});

function confirmarEliminacion(titulo) {
    return window.confirm(`¿Seguro que quieres eliminar "${titulo}"? Esta acción no se puede deshacer.`);
}
