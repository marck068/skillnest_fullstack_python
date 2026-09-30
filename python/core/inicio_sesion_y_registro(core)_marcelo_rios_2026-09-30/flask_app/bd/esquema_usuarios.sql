-- Ejecutar con: mysql -u root -p < flask_app/bd/esquema_usuarios.sql
CREATE DATABASE IF NOT EXISTS sistem_users
  CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

USE sistem_users;

DROP TABLE IF EXISTS usuarios;

CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    fecha_nacimiento DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);