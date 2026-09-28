-- Base de datos para el proyecto Flask de Login y Registro (Flask-Bcrypt)
-- Uso: mysql -u root -p < esquema_loginreg.sql
-- (o ejecútalo desde MySQL Workbench)

DROP SCHEMA IF EXISTS esquema_loginreg;

CREATE SCHEMA esquema_loginreg
    DEFAULT CHARACTER SET utf8mb4
    DEFAULT COLLATE utf8mb4_unicode_ci;

USE esquema_loginreg;

CREATE TABLE usuarios (
    id          INT UNSIGNED NOT NULL AUTO_INCREMENT,
    nombre      VARCHAR(45)  NOT NULL,
    apellido    VARCHAR(45)  NOT NULL,
    email       VARCHAR(100) NOT NULL,
    -- Un hash de bcrypt mide 60 caracteres; 255 deja margen si cambias de algoritmo
    password    VARCHAR(255) NOT NULL,
    created_at  DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at  DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    -- Evita registrar dos usuarios con el mismo correo
    UNIQUE KEY uq_usuarios_email (email)
) ENGINE = InnoDB;
