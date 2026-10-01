-- BookHub - Script de creación de la base de datos (MySQL 8+ / MariaDB 10.4+)
CREATE DATABASE IF NOT EXISTS bookhub
  CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE bookhub;

CREATE TABLE IF NOT EXISTS usuarios (
  id         INT UNSIGNED NOT NULL AUTO_INCREMENT,
  nombre     VARCHAR(50)  NOT NULL,
  apellido   VARCHAR(50)  NOT NULL,
  email      VARCHAR(120) NOT NULL,
  password   VARCHAR(100) NOT NULL,            -- hash Bcrypt, nunca texto plano
  created_at TIMESTAMP    NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  UNIQUE KEY uq_usuarios_email (email)
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS libros (
  id                INT UNSIGNED NOT NULL AUTO_INCREMENT,
  titulo            VARCHAR(150) NOT NULL,
  autor             VARCHAR(100) NOT NULL,
  genero            VARCHAR(50)  NOT NULL,
  fecha_publicacion DATE         NOT NULL,
  descripcion       TEXT         NOT NULL,
  imagen            VARCHAR(255) NULL,
  usuario_id        INT UNSIGNED NOT NULL,
  created_at        TIMESTAMP    NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  KEY idx_libros_usuario (usuario_id),
  CONSTRAINT fk_libros_usuario FOREIGN KEY (usuario_id)
    REFERENCES usuarios (id) ON DELETE CASCADE
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS favoritos (
  id         INT UNSIGNED NOT NULL AUTO_INCREMENT,
  usuario_id INT UNSIGNED NOT NULL,
  libro_id   INT UNSIGNED NOT NULL,
  created_at TIMESTAMP    NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  UNIQUE KEY uq_favorito (usuario_id, libro_id),   -- evita favoritos duplicados
  CONSTRAINT fk_fav_usuario FOREIGN KEY (usuario_id)
    REFERENCES usuarios (id) ON DELETE CASCADE,
  CONSTRAINT fk_fav_libro FOREIGN KEY (libro_id)
    REFERENCES libros (id) ON DELETE CASCADE
) ENGINE=InnoDB;
