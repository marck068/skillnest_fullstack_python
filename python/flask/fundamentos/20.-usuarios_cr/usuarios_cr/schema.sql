-- Crea el esquema y la tabla (si aún no los tienes del módulo de MySQL)
CREATE SCHEMA IF NOT EXISTS esquema_usuarios;
USE esquema_usuarios;

CREATE TABLE IF NOT EXISTS usuarios (
    id INT NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(45),
    apellido VARCHAR(45),
    email VARCHAR(45),
    created_at DATETIME,
    updated_at DATETIME,
    PRIMARY KEY (id)
);

-- Si la tabla ya existía sin AUTO_INCREMENT, ejecuta:
-- ALTER TABLE usuarios MODIFY id INT NOT NULL AUTO_INCREMENT;

-- Datos de ejemplo (como en el wireframe)
INSERT INTO usuarios (nombre, apellido, email, created_at, updated_at) VALUES
('Ricky','Martin','ricky@codingdojo.com',NOW(),NOW()),
('Enrique','Iglesias','enrique@codingdojo.com',NOW(),NOW()),
('Celia','Cruz','celia@codingdojo.com',NOW(),NOW()),
('Ricardo','Montaner','ricardo@codingdojo.com',NOW(),NOW());

SELECT * FROM usuarios;