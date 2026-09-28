-- ============================================================
-- esquema_canciones: usuarios N:N canciones (tabla favoritos)
-- ============================================================
CREATE SCHEMA IF NOT EXISTS `esquema_canciones`
    DEFAULT CHARACTER SET utf8mb4;

USE `esquema_canciones`;

CREATE TABLE IF NOT EXISTS `usuarios` (
    `id`         INT          NOT NULL AUTO_INCREMENT,
    `nombre`     VARCHAR(45)  NULL,
    `email`      VARCHAR(45)  NULL,
    `contrasena` VARCHAR(45)  NULL,
    `created_at` DATETIME     NULL DEFAULT CURRENT_TIMESTAMP,
    `updated_at` DATETIME     NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (`id`)
) ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `canciones` (
    `id`         INT          NOT NULL AUTO_INCREMENT,
    `titulo`     VARCHAR(45)  NULL,
    `artista`    VARCHAR(45)  NULL,
    `created_at` DATETIME     NULL DEFAULT CURRENT_TIMESTAMP,
    `updated_at` DATETIME     NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (`id`)
) ENGINE = InnoDB;

-- Tabla intermedia: la PK compuesta impide favoritos duplicados.
CREATE TABLE IF NOT EXISTS `favoritos` (
    `usuario_id` INT NOT NULL,
    `cancion_id` INT NOT NULL,
    PRIMARY KEY (`usuario_id`, `cancion_id`),
    INDEX `fk_favoritos_canciones_idx` (`cancion_id`),
    CONSTRAINT `fk_favoritos_usuarios`
        FOREIGN KEY (`usuario_id`) REFERENCES `usuarios` (`id`)
        ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT `fk_favoritos_canciones`
        FOREIGN KEY (`cancion_id`) REFERENCES `canciones` (`id`)
        ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB;
