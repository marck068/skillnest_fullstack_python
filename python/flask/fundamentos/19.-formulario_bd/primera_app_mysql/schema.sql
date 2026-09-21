CREATE DATABASE IF NOT EXISTS primera_flask;
USE primera_flask;

CREATE TABLE IF NOT EXISTS mascotas (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255),
    tipo VARCHAR(255),
    color VARCHAR(255),
    created_at DATETIME DEFAULT NOW(),
    updated_at DATETIME DEFAULT NOW() ON UPDATE NOW()
);

-- Datos de ejemplo (opcional)
INSERT INTO mascotas (nombre, tipo, color, created_at, updated_at)
VALUES ('Firulais', 'Perro', 'Café', NOW(), NOW()),
       ('Michi', 'Gato', 'Negro', NOW(), NOW());

DESCRIBE mascotas;
SELECT * FROM mascotas;