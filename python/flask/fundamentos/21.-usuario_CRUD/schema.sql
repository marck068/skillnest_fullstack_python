-- ==========================================================
-- ESQUEMA: esquema_usuarios
-- ==========================================================

CREATE DATABASE IF NOT EXISTS esquema_usuarios;

USE esquema_usuarios;

-- ==========================================================
-- TABLA: usuarios
-- ==========================================================

CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(45) NOT NULL,
    apellido VARCHAR(45) NOT NULL,
    email VARCHAR(45) NOT NULL,
    created_at DATETIME NOT NULL,
    updated_at DATETIME NOT NULL
);

-- Verificar estructura:
-- DESCRIBE usuarios;
-- SHOW CREATE TABLE usuarios;
-- SELECT * FROM usuarios;